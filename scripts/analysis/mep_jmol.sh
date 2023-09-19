#!/bin/bash
file=$1
name=$(echo $file | cut -d '.' -f 1) 
n=0
n_sphere=0

# Read lines from the critical points document
while IFS= read line
do
	n=$((n+1))
	palabra=`echo "$line" | awk '{print $4}'`
	if [ "$palabra" = maxima: ]
	then
		max=$n
	fi
done < "${name}_CRIT.txt"

# Separate the max and min critical points in two files
head -n $((max-2)) ${name}_CRIT.txt | tail -n +3 > min.txt 
tail -n +$((max+2)) ${name}_CRIT.txt > max.txt

sed -i 's/*/ /g' min.txt

sed -i 's/*/ /g' max.txt

# find min val
min_val=`sort -nk 2 min.txt | \
    head -n 1 | \
    awk -v col=2 '{print $col}'`

# find max val
max_val=`sort -nrk 2 max.txt | \
    head -n 1 | \
    awk -v col=2 '{print $col}'`

# Start writing the jmol script
echo "load ${name}_DENS.cube" > $name".jmol"
echo "isosurface vdwden cutoff 0.001 ${name}_DENS.cube color absolute ${min_val} ${max_val} ${name}_MEP.cube" >> $name".jmol"
echo "color \$vdwden translucent" >> $name".jmol"
echo "color background white" >> $name".jmol"

while IFS= read line_min
do
	n_sphere=$((n_sphere+1))
	mep=`echo $line_min | awk '{print $2}'`
	x=`echo $line_min | awk '{print $5}'`
	y=`echo $line_min | awk '{print $6}'`
	z=`echo $line_min | awk '{print $7}'`

	echo "draw sphere$n_sphere diameter 0.4 {$x $y $z} color cyan #MEP in a.u. $mep" >> $name.jmol

done < "./min.txt"

while IFS= read line_max
do
	n_sphere=$((n_sphere+1))
	mep=`echo $line_max | awk '{print $2}'`
	x=`echo $line_max | awk '{print $5}'`
	y=`echo $line_max | awk '{print $6}'`
	z=`echo $line_max | awk '{print $7}'`

	echo "draw sphere$n_sphere diameter 0.4 {$x $y $z} color black  #MEP in a.u. $mep" >> $name.jmol

done < "./max.txt"

rm max.txt
rm min.txt
