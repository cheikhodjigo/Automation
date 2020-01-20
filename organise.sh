#!/bin/bash

# check if argument given
if [ "$#" -ne 2 ]; then
    echo "Illegal number of parameters"
    exit 2
fi

FILES_TO_DELETE=()
IMAGES=()

delete_files(){
    arr=("$@")
    printf '%s\n' "$(basename -- ${arr[@]})"
    echo "Are you sure you want to delete all these files ?:"
    read response
    if [[ "$response" =~ "[y,Y][e,E][s,S]" ]];then 
        rm "${arr[@]}"
        echo "Files deleted"
    elif [[ "$response" =~ "[N,n][O,o]" ]];then
        echo "Files not deleted"
    fi      
}
echo "$1"
for FILE in "$1"/*
do
    echo "$FILE"
    f="$(basename -- $FILE)"
    case $f in
    *.tgz | *.zip | *.html | *.pptx | *.mp3 | *.htm )   # Find file with these extentions
        FILES_TO_DELETE+=("$FILE")
    ;;
    *.jpg | *.jpeg | *.png | *.JPG)                     # Move the pictures in a specific
        mv "$FILE" "$2"
        echo "$f moved"
    ;;
    *)
        if [[ "$f" =~ ^[C,c][V,v].* ]]; then
            #printf "\n"
        fi
    ;;
    esac
done

if [ ${#FILES_TO_DELETE[@]} -gt 0 ] ;then
    delete_files "${FILES_TO_DELETE[@]}"
fi  
