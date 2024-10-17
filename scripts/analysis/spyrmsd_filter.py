#! /usr/bin/env python3

# Author: Tim Renningholtz
# Date: 21.08.2024

# Description: This script reads the conformational ensemble obtained from a
# conformer search and filters the conformers based on their RMSD. A symmetry
# corrected RMSD algorithm can be used to account for symmetry equivalent
# conformers. The filtered conformers are written to a new file.

# import modules

import spyrmsd
from spyrmsd import rmsd, molecule
import numpy as np
import os
import pandas as pd
from pymatgen.io.babel import BabelMolAdaptor
from openbabel import pybel
import argparse

# parse command line arguments

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
    "--threshold", "-t", type=float, required=True, help="RMSD threshold for filtering"
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
    "--no_center", action="store_false", help="Do not center the conformers at origin"
)
parser.add_argument(
    "--no_minimize", action="store_false", help="Do not calculate minimum RMSD"
)

parser.add_argument(
    "--print_ensemble_properties", "-prop", action="store_true", help="Print ensemble"
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

parsed_args = parser.parse_args()


# Print settings
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
    parser.warning(
        "Temperature for population calculation is required if ensemble properties are printed or conformers are filtered based on population. The default temperature is 298.15 K"
    )


# read conformers from file and create openbabel molecules
openbabel_mols = BabelMolAdaptor.from_file(parsed_args.input, return_all_molecules=True)
openbabel_mols = [mol.openbabel_mol for mol in openbabel_mols]
print("Read ", len(openbabel_mols), " conformers from file")

# convert to pybel molecules
pybel_mols = [pybel.Molecule(mol) for mol in openbabel_mols]

# try get energy from pybel molecule
try:
    energy_dict = {}
    for i, mol in enumerate(pybel_mols):
        energy = float(mol.title.split()[0])
        # energy = (energy - min_energy) * 627.509
        energy_dict[i] = float(energy)
except ValueError:
    energy_dict = None

# set spyrmsd backend
if spyrmsd.get_backend() != parsed_args.backend:
    spyrmsd.set_backend(parsed_args.backend)

# create RMSD matrix and fill it
rmsd_matrix = np.zeros((len(pybel_mols), len(pybel_mols)))
print("Use symmetry correction: ", parsed_args.no_sym)
for i in range(len(pybel_mols)):
    for j in range(len(pybel_mols)):
        mol1 = molecule.Molecule.from_obabel(pybel_mols[i])
        mol2 = molecule.Molecule.from_obabel(pybel_mols[j])
        x = rmsd.rmsdwrapper(
            mol1,
            mol2,
            symmetry=parsed_args.no_sym,
            strip=parsed_args.no_strip,
            center=parsed_args.no_center,
            minimize=parsed_args.no_minimize,
            cache=False,
        )
        # print("RMSD between ", i, " and ", j, " is ", x[0])
        rmsd_matrix[i, j] = x[0]
max_rmsd = np.max(rmsd_matrix)
print("Maximum RMSD: ", max_rmsd)
# find i,j indices where rmsd is less than threshold
triu_rmsd_matrix = np.triu(rmsd_matrix)
# get indices of rmsd smaller than threshold, i.e. conformers to delete
indices_smaller = np.where(
    (triu_rmsd_matrix < parsed_args.threshold) & (triu_rmsd_matrix > 0)
)
# create new dataframe with i,j indices and rmsd values
df_smaller = pd.DataFrame(
    {
        "i": indices_smaller[0],
        "j": indices_smaller[1],
        "rmsd": triu_rmsd_matrix[indices_smaller],
    }
)
df_smaller["d_energy"] = df_smaller.apply(
    lambda x: (energy_dict[x["i"]] - energy_dict[x["j"]]) * 627.5, axis=1
)

df_smaller.to_csv(parsed_args.output + "_rmsd_matrix.csv", index=False)

# get unique conformers
filtered_structures = []
to_delete = set()  # indices of conformers to delete, i.e. conformers below threshold
for i in range(len(df_smaller)):
    if df_smaller["i"][i] not in to_delete and df_smaller["j"][i] not in to_delete:
        to_delete.add(df_smaller["j"][i])


print(f"Structures to delete: {[str(i) for i in to_delete]}")
for i in range(len(pybel_mols)):
    if i not in to_delete:
        filtered_structures.append(pybel_mols[i])

print("Number of conformers above RMSD threshold: ", len(filtered_structures))

# write filtered conformers to file
if os.path.exists(parsed_args.output + ".xyz"):
    os.remove(parsed_args.output + ".xyz")
if parsed_args.output[-4:] == ".xyz":
    parsed_args.output = parsed_args.output[:-4]
filtered_mol_out = pybel.Outputfile("xyz", parsed_args.output + ".xyz", overwrite=True)
for mol in filtered_structures:
    filtered_mol_out.write(mol)
filtered_mol_out.close()

print("Filtered conformers written to ", parsed_args.output + ".xyz")

######## print ensemble properties ########
if parsed_args.print_ensemble_properties or parsed_args.population_threshold_conformers:

    def get_population(df: pd.DataFrame, temp: float = 298.15) -> pd.DataFrame:
        """Add total and cumulative population columns to dataframe containing energy values

        Args:
            df (pd.DataFrame): dataframe containing energy values

        Returns:
            pd.DataFrame: dataframe extended with population columns
        """
        denominator = float()
        for i in range(len(df)):
            denominator += np.exp(-df["d_energy_kcal_mol"][i] / (0.0019872041 * 298.15))
        df["population"] = df["d_energy_kcal_mol"].apply(
            lambda x: np.exp(-x / (0.0019872041 * temp)) / denominator * 100
        )
        df["population"] = df["population"].round(1)
        df["cumulative_population"] = df["population"].cumsum()
        return df

    filtered_energy_df = pd.DataFrame(
        {
            "energy": [float(mol.title.split()[0]) for mol in filtered_structures],
            "conformer": [i for i in range(len(filtered_structures))],
        }
    )
    filtered_energy_df["d_energy_kcal_mol"] = (
        filtered_energy_df["energy"].astype(float)
        - filtered_energy_df["energy"].astype(float).min()
    ) * 627.509
    filtered_energy_df = get_population(
        filtered_energy_df, parsed_args.population_temperature_conformers
    )

    filtered_energy_df.to_csv(parsed_args.output + "_ensemble_properties.csv")
    if parsed_args.population_threshold_conformers:
        # get conformers with cumulative population below/equal to threshold
        filtered_energy_df = filtered_energy_df[
            filtered_energy_df["cumulative_population"]
            <= parsed_args.population_threshold_conformers
        ]
        # get conformers from filtered structures
        filtered_structures = [
            filtered_structures[i] for i in filtered_energy_df["conformer"]
        ]
        print(
            "Number of conformers below cumulative population threshold: ",
            len(filtered_structures),
        )
        # write filtered conformers to file
        if os.path.exists(
            parsed_args.output
            + "_populated_conformers_"
            + str(parsed_args.population_threshold_conformers)
            + ".xyz"
        ):
            os.remove(
                parsed_args.output
                + "_populated_conformers_"
                + str(parsed_args.population_threshold_conformers)
                + ".xyz"
            )
        filtered_mol_out = pybel.Outputfile(
            "xyz",
            parsed_args.output
            + "_populated_conformers_"
            + str(parsed_args.population_threshold_conformers).replace(".", "_")
            + ".xyz",
            overwrite=True,
        )
        for mol in filtered_structures:
            filtered_mol_out.write(mol)
        filtered_mol_out.close()
        print(
            "Filtered conformers written to ",
            parsed_args.output
            + "_populated_conformers_"
            + str(parsed_args.population_threshold_conformers).replace(".", "_")
            + ".xyz",
        )

# else terminate
else:
    pass
