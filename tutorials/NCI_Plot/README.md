# NCI Plots

Guide for creating NCI plots using Multiwfn and VMD on MacOS systems.

### Requirements

- ORCA (https://www.faccts.de/docs/orca/6.1/manual/)
- Multiwfn (https://github.com/digital-chemistry-laboratory/homebrew-multiwfn)
- VMD (https://www.ks.uiuc.edu/Development/Download/download.cgi?PackageName=VMD)

### Recommendations

- Define `orca_2mklpath` parameter in `settings.ini`. This allows you to skip steps 2, 3, and 4 below.
  - To do this: (1) set environment variable `Multiwfnpath=${HOMEBREW_PREFIX}/etc/multiwfn` (2) Set the `orca_2mklpath` parameter in `${HOMEBREW_PREFIX}/etc/multiwfn/settings.ini` to your `orca_2mkl` path

### Initial Steps

1. Run ORCA calculation to generate .gbw file

Following steps required only if you have not defined orca_2mklpath in settings.ini

2. Convert .gbw to .wfx
   - One way to do this is to use `orca_2mkl` --> `orca_2mkl -molden filename` to generate .molden.input file
3. If using pseudopotentials: Edit .molden.input to include orca in title line
   - Example:
     ```
     [Title]
     orca
     [Molden Format]
     ...
     ```
4. Use Molden2Aim software or Multiwfn to convert .molden to .wfx

   - Using Multiwfn: `multiwfn filename.molden` --> Select option 19 (Generate wavefunction file) --> Select option 4 (.wfx format)

5. Use Multiwfn to generate NCI plot (20 1 3 3 0 0)
   - Use High-Quality Grid when possible.
   - Important files are `func1.cub` and `func2.cub`

The next steps are very user-dependant. I have included the exact pathways for the folders in my MacOS system, but you may need to adjust them for your own system. The main goal is to get the `func1.cub` and `func2.cub` files into the same folder as the VMDlauncher executable and then run the RDGfill.vmd script with VMD open.

### VMD Steps

6. Copy `func1.cub` and `func2.cub` over to `/Applications/VMD\ 2.0.0a7-pre2.app/Contents/MacOS//Applications/VMD\ 2.0.0a7-pre2.app/Contents/MacOS/`
7. Execute `/Applications/VMD\ 2.0.0a7-pre2.app/Contents/MacOS//Applications/VMD\ 2.0.0a7-pre2.app/Contents/MacOS/VMDlauncher`
8. In VMD terminal run cd `/Applications/VMD\ 2.0.0a7-pre2.app/Contents/MacOS/`
9. In VMD terminal run `source /Applications/VMD\ 2.0.0a7-pre2.app/Contents/MacOS/RDGfill.vmd`

If having issues with reading the .cub files, make sure they are named func1.cub and func2.cub and in the folder you are in, where the RDGfill.vmd script is and VMDlauncher.exe
