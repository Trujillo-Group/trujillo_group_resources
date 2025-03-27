#! /usr/bin/env python3

# Author: Tim Renningholtz
# Date: 26.03.2025

# Description: This script reads the conformational ensemble obtained from a
# conformer search and filters the conformers based on their RMSD. A symmetry
# corrected RMSD algorithm can be used to account for symmetry equivalent
# conformers. The filtered conformers are written to a new file.

# import modules

from platform import java_ver
from spyrmsd import molecule, rmsd
import warnings
from spyrmsd.parallel import prmsdwrapper
import numpy as np
import os
import pandas as pd
from ase import Atoms
from ase.io import read, write
from ase.data import vdw_radii, atomic_numbers, covalent_radii
import argparse
from itertools import product
from scipy.spatial import Voronoi


def get_voronoi_neighbourlist(
    atoms: Atoms,
    tolerance: float,
) -> np.ndarray:
    """Get connectivity list from Voronoi analysis, considering periodic boundary conditions.
    To have two atoms connected, these must satisfy two conditions:
    1. They must share a Voronoi facet
    2. The distance between them must be less than the sum of their covalent radii (plus a tolerance)

    Args:
        atoms (Atoms): ase Atoms object.
        scaling_factor (float): Scaling factor for covalent radii of metal atoms.
        tolerance (float): Tolerance for second condition.

    Returns:
        np.ndarray: N_edges x 2 array with the connectivity list. COO format.

    Notes:
        The array contains all the edges just in one direction!
    """
    # First condition to have two atoms connected: They must share a Voronoi facet
    coords_arr = np.copy(atoms.get_positions())
    coords_arr = np.expand_dims(coords_arr, axis=0)
    coords_arr = np.repeat(coords_arr, 27, axis=0)
    mirrors = [-1, 0, 1]
    mirrors = np.asarray(list(product(mirrors, repeat=3)))
    mirrors = np.expand_dims(mirrors, 1)
    mirrors = np.repeat(mirrors, coords_arr.shape[1], axis=1)
    corrected_coords = np.reshape(
        coords_arr + mirrors,
        (coords_arr.shape[0] * coords_arr.shape[1], coords_arr.shape[2]),
    )
    corrected_coords = np.dot(corrected_coords, atoms.get_cell())
    translator = np.tile(np.arange(coords_arr.shape[1]), coords_arr.shape[0])
    vor_bonds = Voronoi(atoms.get_positions())
    pairs_corr = translator[vor_bonds.ridge_points]
    pairs_corr = np.unique(np.sort(pairs_corr, axis=1), axis=0)
    true_arr = pairs_corr[:, 0] == pairs_corr[:, 1]
    true_arr = np.argwhere(true_arr)
    pairs_corr = np.delete(pairs_corr, true_arr, axis=0)
    # Second condition for two atoms to be connected: Their distance must be smaller than the sum of their
    # covalent radii plus a tolerance.
    dst_d = {}
    pairs_lst = []
    for pair in pairs_corr:
        distance = atoms.get_distance(
            pair[0], pair[1], mic=True
        )  # mic=True for periodic boundary conditions
        atomic_num_1 = atomic_numbers[atoms[pair[0]].symbol]
        atomic_num_2 = atomic_numbers[atoms[pair[1]].symbol]
        elem_pair = (atoms[pair[0]].symbol, atoms[pair[1]].symbol)
        fr_elements = frozenset(elem_pair)
        if fr_elements not in dst_d:
            dst_d[fr_elements] = (
                covalent_radii[atomic_num_1] * 1.2
                + covalent_radii[atomic_num_2] * 1.2
                + tolerance
            )
        if distance <= dst_d[fr_elements]:
            pairs_lst.append(pair)
    if len(pairs_lst) == 0:
        return np.array([])
    else:
        return np.sort(np.array(pairs_lst), axis=1)


# get command line arguments
def get_args() -> argparse.Namespace:
    """Parse command line arguments"""
    parser = argparse.ArgumentParser(description="Filter conformers based on RMSD")
    parser.add_argument(
        "--input", "-i", type=str, required=True, help=".xyz file with conformers"
    )
    parser.add_argument(
        "--output",
        "-o",
        type=str,
        required=True,
        help="Name of the output file, format will be .xyz",
        default="filtered_conformers",
    )
    parser.add_argument(
        "--threshold",
        "-t",
        type=float,
        required=True,
        help="RMSD threshold for filtering",
    )
    parser.add_argument(
        "--no_sym", action="store_false", help="Do not use symmetry correction"
    )
    parser.add_argument(
        "--backend",
        "-b",
        type=str,
        help="Graph backend, e.g. networkx or rustworkx",
        default="rustworkx",
    )
    parser.add_argument(
        "--no_strip",
        action="store_false",
        help="Do not strip hydrogens from the conformers",
    )
    parser.add_argument(
        "--no_center",
        action="store_false",
        help="Do not center the conformers at origin",
    )
    parser.add_argument(
        "--no_minimize", action="store_false", help="Do not calculate minimum RMSD"
    )

    parser.add_argument(
        "--print_ensemble_properties",
        "-prop",
        action="store_true",
        help="Print ensemble",
    )
    parser.add_argument(
        "--population_threshold_conformers",
        "-pop",
        type=float,
        help="Conformer structures with cummulative population below this threshold.",
        default=None,
        required=False,
    )

    parser.add_argument(
        "--population_temperature_conformers",
        "-temp",
        type=float,
        help="Temperature for population calculation in [K]",
        default=298.15,
        required=False,
    )

    parser.add_argument(
        "--connect_atoms",
        "-ca",
        type=str,
        help="""List of atom indices to connect with a bond starting at 0. If multiple atoms need to be connected,
            every other atom index is the atom to connect to. The first atom is the atom to connect from.
            Example: --connect_atoms 0,1,2,3 connects atom 0 to atom 1 and atom 2 to atom 3.
            """,
        default=None,
        required=False,
    )

    parser.add_argument(
        "--n_cores",
        "-n",
        type=int,
        help="Number of cores to use for RMSD calculation",
        default=1,
        required=False,
    )

    parser.add_argument(
        "--rmsd_mat", action="store_true", help="Store RMSD matrix as csv"
    )

    parser = parser.parse_args()
    if parser.connect_atoms is not None:
        con_atoms = parser.connect_atoms.split(",")
        assert len(con_atoms) % 2 == 0, "Number of atoms to connect must be even"

    return parser


# Print settings
def print_settings(parsed_args):
    """Print settings from argument parser"""

    print("#" * 80)
    print("*" * 35, "Settings", "*" * 35)
    print("Input file: ", parsed_args.input)
    print("Output file: ", parsed_args.output)
    print("RMSD threshold: ", parsed_args.threshold)
    print("Symmetry correction: ", parsed_args.no_sym)
    print("Graph backend: ", parsed_args.backend)
    print("Strip hydrogens: ", parsed_args.no_strip)
    print("Center conformers: ", parsed_args.no_center)
    print("Minimize RMSD: ", parsed_args.no_minimize)
    print("Print ensemble properties: ", parsed_args.print_ensemble_properties)
    if parsed_args.connect_atoms:
        print("Connect atoms: ", parsed_args.connect_atoms)
    if parsed_args.population_threshold_conformers:
        print(
            "Population threshold for conformers: ",
            parsed_args.population_threshold_conformers,
        )
        print(
            "Temperature for population calculation: ",
            parsed_args.population_temperature_conformers,
        )
        print(
            f"Conformers with a cumulative population of {parsed_args.population_threshold_conformers} % or below will be printed."
        )
    print("#" * 80)

    if (
        any(
            [
                parsed_args.print_ensemble_properties,
                parsed_args.population_threshold_conformers,
            ]
        )
        and not parsed_args.population_temperature_conformers
    ):
        parsed_args.warning(
            "Temperature for population calculation is required if ensemble properties are printed or conformers are filtered based on population. The default temperature is 298.15 K"
        )


def coo_to_adjacency_matrix(coo_matrix: np.ndarray, n_atoms: int) -> np.ndarray:
    """Convert COO matrix to adjacency matrix

    Args:
        coo_matrix (np.ndarray): COO matrix
        n_atoms (int): number of atoms

    Returns:
        np.ndarray: adjacency matrix
    """
    adjacency_matrix = np.zeros((n_atoms, n_atoms), dtype=np.int8)
    for i in range(coo_matrix.shape[0]):
        adjacency_matrix[coo_matrix[i, 0], coo_matrix[i, 1]] = 1
    return adjacency_matrix


def get_energy_from_commentline(commentline: str) -> float:
    import re

    re_pattern = re.compile(r"-?\d+\.\d+")
    for i in commentline:
        if re.findall(re_pattern, i):
            return i
        else:
            continue
    warnings.warn(
        "No energy value found in comment line. Energy set to 0.0",
        UserWarning,
        stacklevel=1,
    )
    return 0.0


# read conformers from file and create openbabel molecules
def get_conformers(file: str, conn: str = None) -> list[Atoms, np.ndarray]:
    """Read conformers from file and create openbabel molecules

    Args:
        file (str): file with conformers
        conn (str, optional): list of atom indices to connect with a bond starting at 0. If multiple atoms need to be connected,
            every other atom index is the atom to connect to. The first atom is the atom to connect
            from. Example: "0,1,2,3" connects atom 0 to atom 1 and atom 2 to
            atom 3. Defaults to None, i.e. connectivit is not changed.

    Returns:
        list[Atoms, np.ndarray]: list of ASE atoms and adjacency matrices
    """
    mols = read(file, ":")
    adjacency_matrices = []
    for mol in mols:
        mol.info["energy"] = get_energy_from_commentline(mol.info.keys())
        coo_matrix = get_voronoi_neighbourlist(mol, 0.1)
        # add connectivity from command line
        if conn is not None:
            atoms_list = conn.split(",")
            for i in range(0, len(atoms_list), 2):
                coo_matrix = np.vstack(
                    [
                        coo_matrix,
                        np.array([int(atoms_list[i]), int(atoms_list[i + 1])]),
                    ]
                )
                coo_matrix = np.vstack(
                    [
                        coo_matrix,
                        np.array([int(atoms_list[i + 1]), int(atoms_list[i])]),
                    ]
                )
        ad_matrix = coo_to_adjacency_matrix(coo_matrix, len(mol))
        adjacency_matrices.append(ad_matrix)

    return [mols, adjacency_matrices]


def get_rmsd_matrix(
    mols: list[Atoms], adjacency_matrices: list[np.ndarray], **kwargs
) -> np.ndarray:
    """Get RMSD matrix from conformers

    Args:
        conformers (list[pybel.Molecule]): list of openbabel molecules
        energy_dict (dict): dictionary with energy values and indices of conformers

    Returns:
        np.ndarray: RMSD matrix
    """
    n_columns = len(mols)
    spy_mols = []
    for i in range(n_columns):
        adjacency_matrix = adjacency_matrices[i]
        mol = molecule.Molecule(
            atomicnums=mols[i].get_atomic_numbers(),
            coordinates=mols[i].get_positions(),
            adjacency_matrix=adjacency_matrix,
        )
        spy_mols.append(mol)
    rmsd_matrix = np.zeros((n_columns, n_columns), dtype=np.float16)

    for i in range(n_columns):
        mol = spy_mols[i]
        # only calculate lower triangle
        mols = [spy_mols[j] for j in range(n_columns) if j < i]
        if len(mols) == 0:
            continue
        result = prmsdwrapper(
            mol,
            mols,
            symmetry=kwargs["no_sym"],
            strip=kwargs["no_strip"],
            center=kwargs["no_center"],
            minimize=kwargs["no_minimize"],
            cache=False,
            num_workers=kwargs["n_cores"],
            chunksize=1,
        )
        j = len(mols)
        rmsd_matrix[i, :j] = result
    # mirror lower triangle to upper triangle
    rmsd_matrix = rmsd_matrix + rmsd_matrix.T

    if kwargs["rmsd_mat"]:
        np.savetxt(
            kwargs["output"] + "_all_rmsd_matrix.csv", rmsd_matrix, delimiter=","
        )
        print("RMSD matrix written to rmsd_matrix.csv")
    print("Minimum RMSD: ", np.min(rmsd_matrix[np.nonzero(rmsd_matrix)]))
    print("Maximum RMSD: ", np.max(rmsd_matrix))

    return rmsd_matrix


def get_to_delete_set(rmsd_matrix: np.ndarray, threshold: float) -> set:
    """Get set of conformers to delete

    Args:
        rmsd_matrix (np.ndarray): RMSD matrix
        threshold (float): RMSD threshold

    Returns:
        set: set of conformers to delete
    """
    to_delete = set()
    upper_triangle = np.triu(rmsd_matrix, k=1.0).astype(np.float16)
    indices_smaller_than_threshold = np.where(
        (upper_triangle < threshold) & (upper_triangle > 0)
    )
    array_smaller = np.array(
        [indices_smaller_than_threshold[0], indices_smaller_than_threshold[1]],
        dtype=np.int32,
    ).T
    for iter in range(array_smaller.shape[0]):
        if (
            array_smaller[iter, 0] not in to_delete
            and array_smaller[iter, 1] not in to_delete
        ):
            to_delete.add(array_smaller[iter, 1])
    return to_delete


def update_rmsd_matrix(rmsd_matrix: np.ndarray, to_delete: set) -> np.ndarray:
    """Delete rows and columns of indices in to_delete

    Args:
        rmsd_matrix (np.ndarray): RMSD matrix
        to_delete (set): set of conformers to delete

    Returns:
        np.ndarray: new RMSD matrix
    """
    # delete rows and columns of indices in to_delete
    new_matrix = np.delete(rmsd_matrix, list(to_delete), axis=0)
    new_matrix = np.delete(new_matrix, list(to_delete), axis=1)
    return new_matrix


def update_mol_list(mol_list: list[Atoms], to_delete: set) -> list[Atoms]:
    """Delete conformers from list
    Args:
        mol_list (list[pybel.Molecule]): list of openbabel molecules
        to_delete (set): set of conformers to delete
    Returns:
        list[pybel.Molecule]: updated list of openbabel molecules
    """
    new_list = []
    for i in range(len(mol_list)):
        if i not in to_delete:
            new_list.append(mol_list[i])
    return new_list


def get_population(
    mol_list: list[Atoms], temp: float, threshold: float
) -> pd.DataFrame:
    """Add total and cumulative population columns to dataframe containing energy values

    Args:
        df (pd.DataFrame): dataframe containing energy values

    Returns:
        pd.DataFrame: dataframe extended with population columns
    """
    df = pd.DataFrame(
        {
            "energy": [mol.info["energy"] for mol in mol_list],
            "conformer": [i for i in range(len(mol_list))],
            "index": [i for i in range(len(mol_list))],
        }
    )
    df["d_energy_kcal_mol"] = (
        df["energy"].astype(float) - df["energy"].astype(float).min()
    ) * 627.509
    df["population"] = float()
    df["cumulative_population"] = float()
    denominator_sum = np.sum(np.exp(-df["d_energy_kcal_mol"] / (0.0019872041 * 298.15)))
    df["population"] = df["d_energy_kcal_mol"].apply(
        lambda x: np.exp(-x / (0.0019872041 * temp)) / denominator_sum * 100
    )
    df["population"] = df["population"].round(1)
    df["cumulative_population"] = df["population"].cumsum()
    return df


# main function
def main():
    args = get_args()
    print_settings(args)
    mols, adjacency_matrix = get_conformers(args.input, args.connect_atoms)
    print("Number of conformers: ", len(mols))
    rmsd_matrix = get_rmsd_matrix(mols, adjacency_matrix, **vars(args))
    to_delete = get_to_delete_set(rmsd_matrix, args.threshold)
    new_matrix = update_rmsd_matrix(rmsd_matrix, to_delete)
    filtered_structures = update_mol_list(mols, to_delete)
    print("Number of conformers to delete: ", len(to_delete))
    print("Conformers to delete: ", [str(i) for i in to_delete])
    print("Number of conformers above RMSD threshold: ", len(filtered_structures))
    # save new matrix as csv
    np.savetxt(args.output + "_filtered_rmsd_matrix.csv", new_matrix, delimiter=",")
    print(
        "RMSD matrix of filtered conformers written to ",
        args.output + "_filtered_rmsd_matrix.csv",
    )
    if os.path.exists(args.output + ".xyz"):
        os.remove(args.output + ".xyz")
    filtered_mol_out = args.output + f"{args.threshold}.xyz"
    for mol in filtered_structures:
        write(filtered_mol_out, mol, append=True)
    print("RMSD filtered conformers written to ", args.output + ".xyz")

    if args.population_threshold_conformers:
        # get conformers with cumulative population below/equal to threshold
        if len(filtered_structures) == 1:
            warnings.warn(
                "Only one conformer left for population analysis. Please adjust "
                "the RMSD threshold. The population analysis requires at least "
                "two conformers.",
                UserWarning,
                stacklevel=1,
            )
            quit()
        df = get_population(
            mol_list=filtered_structures,
            temp=args.population_temperature_conformers,
            threshold=args.population_threshold_conformers,
        )
        filtered_energy_df = df[
            df["cumulative_population"] <= args.population_threshold_conformers
        ]
        df.to_csv(
            args.output
            + f"_ensemble_population{args.population_temperature_conformers}.csv",
            index=False,
        )
        print(
            f"Ensemble properties written to {args.output}_ensemble_population{args.population_temperature_conformers}.csv"
        )
        # get conformers from filtered structures
        filtered_structures_pop = [
            filtered_structures[i] for i in filtered_energy_df["index"]
        ]
        print(
            "Number of conformers below cumulative population threshold: ",
            len(filtered_structures_pop),
        )
        # write filtered conformers to file
        if os.path.exists(
            args.output
            + "_populated_conformers_"
            + str(args.population_threshold_conformers)
            + ".xyz"
        ):
            os.remove(
                args.output
                + "_populated_conformers_"
                + str(args.population_threshold_conformers)
                + ".xyz"
            )
        filtered_mol_out = (
            args.output
            + "_populated_conformers_"
            + str(args.population_threshold_conformers).replace(".", "_")
            + ".xyz"
        )
        for mol in filtered_structures_pop:
            write(filtered_mol_out, mol, append=True)
        print(
            f"RMSD filtered conformers below population threshold @ {args.population_temperature_conformers} written to ",
            args.output
            + "_populated_conformers_"
            + str(args.population_threshold_conformers).replace(".", "_")
            + ".xyz",
        )


if __name__ == "__main__":
    main()
