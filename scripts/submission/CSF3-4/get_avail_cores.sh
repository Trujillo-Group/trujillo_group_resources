#!/bin/bash

######################################################################################
# Script Name: get_avail_cores.sh
# Description: This script gets the max number of idle cores for not fully occupied    # nodes. This function can be stored in your .bashrc file and called from the command
# line.
# Author: Tim Renningholtz
# Created: September 25, 2023
# Version: 1.0
######################################################################################

get_nodes_with_free_cores() {
    # Get the list of nodes with their CPU information
    node_list=$(sinfo --Node --partition=multicore --format="%N %C")

    # Loop through each line in the node list
    while IFS= read -r line; do
        node_name=$(echo "$line" | awk '{print $1}')
        cpu_info=$(echo "$line" | awk '{print $2}')
        idle_cores=$(echo "$cpu_info" | awk -F'/' '{print $2}')
        
        # Check if the node has 4 or more idle cores
        if [[ $idle_cores -ge 4 ]]; then
            echo "$node_name has $idle_cores idle cores"
        fi
    done <<< "$node_list"
}
