# Intro to Shell 

## Where am I?
To find out where you are in the filesystem use the command: 
```shell
pwd 
```
`pwd` is short for <strong>P</strong>rint <strong>W</strong>orking <strong>D</strong>irectory.
Which prints out the absolute path of your current working directory. <br>

## How to identify files and directories? 

To find out what is present in the current working directory type  `ls` to list the content 
of your current directory. <br>
To see the listing of a specific location use `ls` followed by path. 
`ls /Users/joseservin/DataCamp` will show you the directories and or files that are in this path. 

## Relative vs Absolute Path

<mark>Absolute Path:</mark> specifies the location starting from the root directory. <br>
```shell
/User/joseservin/DataCamp/Course/PP_Writting_Function/notes.py
```
<mark>Relative Path:</mark> specified location in reference to current directory. 
```shell
DataCamp/PP_Writing_Functions/notes.py
```
## How to move to another directory?
To move to another directory use the ``cd`` command. <br>

For example, we start in the parent directory
```shell
/users/joseservin
```
Now we list out what is in this joseservin directoy. 
```shell
ls 
```
Finally, we `cd` into DataCamp and check content with ls.
```shell
cd DataCamp 
ls 
```
## How can I move up a directory?
* To move up to the parent directory of your current location use the `cd ..` command. <br>
* To move and or list out the home directory use the `ls ~` and `cd ~`

## How can I copy and or move files?

`cp original.txt duplicate.txt` will create a copy of the original file. If duplicate.txt already exists it
will be overwritten. <br>
To copy two or more files from a directory into another directory use the following command syntax.
```shell
cp directoryone/file.py directoryone/file.py directorytwo 
```
To move a file use the `mv` command following the same logic as `cp`.

## How to rename files?
Use the same `mv` command to rename files. For example to rename a file inside the DataCamp directory. 
```shell
mv original.py new_name.py 
```
This will change the name of the file original.py to new_name.py. 


## How to delete files?
To delete file use the "remove" command `rm`. <br>
`rm` can be given a file name or path (relative or absolute). 
```shell
rm thesis.py directory/thesis_two.csv 
```
This permanently deletes both the file these and the one inside the directory called directory. 

## How to create and delete directories?
To create a directory use `mkdir directory_name`. 
For example, to make a parent directory and child directory do the following: 
```shell
mkdir parent 
mkdir parent/child
```
You can rename a directory using `mv DataCamp DataCampMaster` which will rename the DatCamp directory to DataCampMaster.
To delete a directory you use `rmdir` but you must first delete the files in the directory before you can delete the whole directory.
