# Automation

## Description

This project is a file arrangement automation process.

It allow the user to sort out his files from a specified directory to a corresponding destination determined by 
it's name.

Let's say you have your download File with the location ~/Downloads and your main repository named ~/Documents.
The ~/Documents/ Folder then contains subfolders like Images/ , Music/, Videos/, etc.

What the algorithm will do is find files corresponding to:
- An image and stores them into Images/
- A video and stores them into Videos/
- etc.

Also it will look for the name of the file that is supposed to be a map.
The syntax supported for now is A_B_C.* it will then store the file following this scheme belows:
`A/
|
--B/
  |
  --A_B_C.*`
Where A is the name of the parent directory, B the name of destination directory and C the name of the file.

## Usage

To execute the script you will need to give him the origin folder and the destination 
one just like this: 

`./organize.sh ~/origin/path ~/Destination/path`

## State

Ready to use.