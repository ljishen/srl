#!/bin/bash -e

if [ "$#" -ne 3 ]; then
    cat <<-ENDOFMESSAGE
This script parsese all verification test results to file alltests.csv 
Usage: ./parse_all.sh <script folder> <test results folder> <base machine>
ENDOFMESSAGE
    exit
fi

benchmark_list=('blogbench' 'compilebench' 'fhourstones' 'himeno' 'interbench' 'nbench' 'pybench' 'ramsmp' 'stockfish-7')
experiment_index=2

for bm in "${benchmark_list[@]}"; do
    all_reses=(`ls "$2/$bm/$experiment_index" | grep "with.*prof$"`)
    
    # Removes shortest match from array,
    # see http://www.tldp.org/LDP/abs/html/arrays.html
    all_ref_reses=(${all_reses[@]#without_$3*prof})

    for ref_res in "${all_ref_reses[@]}"; do
        bn=`basename "$ref_res" .prof`
        index=`echo "$bn" | cut -d _ -f 3`
        
        "$1"/"$bm"/parse.sh "$2"/$bm/$experiment_index/without_${3}_${index}.prof "$2"/$bm/$experiment_index/$ref_res alltests.csv
    done
done
