#!/usr/bin/env python3

# Author: Inigo Iribarren
# Date: 30-03-2020

# This script extracts all the important information from the *log files in the folder.

# Import modules
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import sys
import glob
import csv

# Personal module, in the same folder
import myfunctions as mf

# Select the desired files by argument and look for them
try:
	search = '*'+str(sys.argv[2])+'*log'
except IndexError:
	search = '*log'

num_log_files = len(glob.glob(search))
log_files = glob.glob(search)

if (num_log_files == 0):
    print("There is no log files in the folder")
    
dat_file = open(sys.argv[1]+".csv", mode="w")
dat_writer = csv.writer(dat_file, delimiter=',')

dat_writer.writerow(['PG', 'ImFreq', 'SCFEnergy', 'MP2Energy', 'ZPE', 'TotalEnergy', 'ThermCorrect', 'FreeEnergy', 'Dipole', 'State', 'Name'])
#print('PG;ImFreq;SCFEnergy;MP2Energy;ZPE;;TotalEnergy;ThermCorrect;;FreeEnergy;Dipole;State;Name')

log_files.sort()

# Iterate all the files and extract the information
    
for file in log_files:
    
    # Load the text files:
    logfile = open(file, 'r')
    text = logfile.readlines()
    logfile.close()

    # Calculate variables
    
    name = file.split(".")[0]
    
    try:
        sym = text[mf.last_find(text, 'point group')].split()[3]
    except (IndexError, UnboundLocalError):
        sym = "?"
        
    try:
        frq = mf.all_find(text, 'Frequencies')
        frq[0][0]
        frq = str(frq).replace('--','').count('-')
    except IndexError:
        frq = "?"

    try:    
        scf = text[mf.last_find(text, 'SCF Done')].split()[4]
    except (IndexError, UnboundLocalError):
        scf = "?"
    
    try:
        zpe = text[mf.last_find(text, 'Zero-point cor')].split()[2]
    except (IndexError, UnboundLocalError):
        zpe = "?"
        
    try:
        nrg = text[mf.last_find(text, 'Sum of electronic and zero')].split()[6]
    except (IndexError, UnboundLocalError):
        nrg = "?"
  
    try: 
        dpl = text[mf.last_find(text, 'Tot=')].split()[7]
    except (IndexError, UnboundLocalError):
        dpl = "?"
        
    try:
        th = text[mf.last_find(text, 'Thermal correction to Gibbs Free Energy')].split()[6]
    except (IndexError, UnboundLocalError):
        th = "?"
        
    try:
        dG = text[mf.last_find(text, 'Sum of electronic and thermal Free Energies')].split()[7]
    except (IndexError, UnboundLocalError):
        dG = "?"
        
    try:
        mp2_raw =text[mf.last_find(text, 'EUMP2')].split()[5].split('D')
        mp2 = "{:.8f}".format(float(mp2_raw[0])*10**int(mp2_raw[1]))
    except (IndexError, UnboundLocalError):
        mp2 = "?"
    
    # Calculate state of the file
    end_text = text[-5:]
    
    try:
        end_text[mf.last_find(end_text, ' Normal termination')]
        state = 'OK'
    except:
        try:
            end_text[mf.last_find(end_text, ' Error')]
            state = 'ERR'
        except:
            state = 'RUN'
    
    dat_writer.writerow([str(sym), str(frq), str(scf), str(mp2), str(zpe), str(nrg), str(th), str(dG), str(dpl),  state, name])

dat_file.close()
