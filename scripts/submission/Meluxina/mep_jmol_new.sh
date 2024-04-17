#!/bin/bash

# This script will use filename_DENS.cube, filename_MEP.cube and filename_CRIT.txt in your working directory to generate a filename.jmol file 

# Iterate over files matching the specified patterns
for file in *_DENS.cube *_MEP.cube *_CRIT.txt; do
    # Extract the file name without extension
    name=$(echo "$file" | sed 's/_DENS\.cube//' | sed 's/_MEP\.cube//' | sed 's/_CRIT\.txt//')
    n=0
    n_sphere=0

    # Create a .jmol file with the specified content
    echo "load ${name}_DENS.cube" > "$name.jmol"
    echo "isosurface vdwden cutoff 0.001 ${name}_DENS.cube color absolute 0.03 0.24444 ${name}_MEP.cube" >> "$name.jmol"
    echo "color \$vdwden translucent" >> "$name.jmol"
    echo "color background white" >> "$name.jmol"

    # Process the *_CRIT.txt file
    if [ -f "${name}_CRIT.txt" ]; then
        while IFS= read -r line; do
            n=$((n+1))
            palabra=$(echo "$line" | awk '{print $4}')
            if [ "$palabra" = "maxima:" ]; then
                max=$n
            fi
        done < "${name}_CRIT.txt"

        head -n "$((max-2))" "${name}_CRIT.txt" | tail -n +3 > min.txt
        tail -n +"$((max+2))" "${name}_CRIT.txt" > max.txt

        sed 's/*/ /g' min.txt > min1.txt
        mv min1.txt min.txt

        sed 's/*/ /g' max.txt > max1.txt
        mv max1.txt max.txt

        # Process the min.txt file
        while IFS= read -r line_min; do
            n_sphere=$((n_sphere+1))
            mep=$(echo "$line_min" | awk '{print $2}')
            x=$(echo "$line_min" | awk '{print $5}')
            y=$(echo "$line_min" | awk '{print $6}')
            z=$(echo "$line_min" | awk '{print $7}')

            echo "#draw sphere$n_sphere diameter 0.4 {$x $y $z} color cyan #MEP in a.u. $mep" >> "$name.jmol"

        done < min.txt

        # Process the max.txt file
        while IFS= read -r line_max; do
            n_sphere=$((n_sphere+1))
            mep=$(echo "$line_max" | awk '{print $2}')
            x=$(echo "$line_max" | awk '{print $5}')
            y=$(echo "$line_max" | awk '{print $6}')
            z=$(echo "$line_max" | awk '{print $7}')

            echo "draw sphere$n_sphere diameter 0.4 {$x $y $z} color black  #MEP in a.u. $mep" >> "$name.jmol"
            echo "set echo sphere$n_sphere \$sphere$n_sphere" >> "$name.jmol"
            echo "echo $mep; color echo black; font echo 20" >> "$name.jmol"
            echo 'echo " ' "$mep"'"' >> "$name.jmol"

        done < max.txt

        # Cleanup temporary files
        rm -f min.txt max.txt
    fi
done
