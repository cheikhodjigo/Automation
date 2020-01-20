#!/bin/bash

# check if argument given
if [ "$#" -ne 2 ]; then
    echo "Please enter the directory to sort and the destination !"
    exit 2
fi

py sortFiles/sort.py "$1" "$2"
