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
cp directoryone/fileone.py directoryone/filetwo.py directorytwo 
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

## How to view a file's content?
The simplest way to view the content of a file is by using the `cat` command. 
```shell
cat user_info.txt
```
## How to view large files?
Use the `less` command to <strong>page</strong> the output of files. 
```shell
less user_info.txt
```
## How to view the head
Use the `head` command along with file path to see the first 10 lines of a file.
## How to control what commands do?
To control what a command can do, use a flag. 
```shell
head -n 5 user_txt.csv
```
This will now display the first 5 rows rather than the first 10 rows. 
## How to list everything below a directory?
To view everything that is underneath a directory you can use the flag `-R` which stands for recursive with the `ls` 
command. `ls -R` when used in the home directory will list all files and directories at every level. 

## How to select columns from a file?
To select columns from a file use the `cut` command. For example: `cut -f 2-5,8 -d , values.csv`.
* the `-f` flag "fields" 
* 2-5,8 means columns 2 through 5 and 8
* `-d ,` means use `,` as the delimiter

## How can I repeat commands?
There are various ways you can repeat commands in the shell/terminal.
1. `!<command> ` will re-run the most recent use of that command.
2. `history` will produce a list of commands plus a serial number of each command. 
```text
$ history
    1  head summer.csv
    2  cd seasonal
    3  head summer.csv
    4  history
```
3. `!<serial number>` will run the command attributed to the serial number specified. 

## How can I select lines containing specific values?
Use the `grep` command along with text and filepath. For example, `grep howdy DataCamp/message.txt` will search for 
"howdy" in the file message.txt. <br>

The `grep` has lots of useful flags:
```text
-c: print a count of matching lines rather than the lines themselves
-h: do not print the names of files when searching multiple files
-i: ignore case (e.g., treat "Regression" and "regression" as matches)
-l: print the names of files that contain matches, not the matches
-n: print line numbers for matching lines
-v: invert the match, i.e., only show lines that don't match
```
You can search in various files for example: `grep -c incisor seasonal/autumn.csv seasonal/winter.csv`. And you can 
invert the search, for example: `grep -v -n molar seasonal/spring.csv`.

## How to store a commands output in a file?
To save the output of a command you must redirect it. For example, the following command will save the head of the 
spring.csv file to a file called top.csv. 
```shell
head -n 5 seasonal/spring.csv > top.csv 
```
## A better way to combine commands
Redirection has two major drawbacks. 
1. it leaves intermediate files 
2. requires more commands typed out and in the history <br>

To accomplish the same you can use the <strong>pipe</strong> tool. Which tells the terminal to use the output from 
the left as an input for the command on the right. 
   
```shell
head -n 5 seasonal/winter.csv | tail -n 3
```
Example: select the first column of a csv file, remove the header line containing "Date" and select the first 10 
lines of actual data. 
```shell
cut -d , -f 1 path/to_file.csv | grep -v Date | head -n 10 
```
## How to count the records in a file?
The command `wc` "word count" prints the number of characters `-c`, words `-w` and lines `-l`. <br>
Example:count the number of line/records in `file.csv` have dates in "2017-07"
```shell
grep 2017-07 file/path.csv | wc -l 
```
## How can I specify many files at once? 
Use the wildcard character `*` which means "match zero or more characters". <br>
Example: if you are selecting all files from a directory you can use
```shell
cut -d , -f 1 directory/* 
```
Or to select all `.csv` files you can,
```shell
cut -d , -f 1 directory/*.csv 
```
Other wildcards include:
```text
? matches a single character, so 201?.txt will match 2017.txt or 2018.txt, but not 2017-01.txt.
[...] matches any one of the characters inside the square brackets, so 201[78].txt matches 2017.txt or 2018.txt, but not 2016.txt.
{...} matches any of the comma-separated patterns inside the curly brackets, so {*.txt, *.csv} matches any file whose name ends with .txt or .csv, but not files whose names end with .pdf.
```
## How can I sort lines of text?
Use the `sort` command along with flags `-n` which sort numerically, `-r` which is for reverse order, `-b` ignored 
leading blanks and `-f` folds cases (case-insensitive). By default, sort will display in ascending order. 
## How to remove duplicates?
Using the `uniq` command will remove duplicate lines. Specifically adjacent duplicate lines. 
## How to save the output of a pipe? 
You redirect the same way you saved before but ensuring the redirection is done at the end. 
```shell
cut -d , -f 2 seasonal/*.csv | grep -v Tooth > teeth-only.txt
> result.txt head -n 3 seasonal/winter.csv
```
## How to stop a programm from running?
Use the escape command `ctrl + c` to end it. Often written as `^C`. 
## How to find the file with the shortest amount of lines?
```shell
wc -l seasonal/*csv | grep -v total | sort -n | head -n 1
```
## Intro to Shell environment variables
* `HOME` returns user's home directory
* `PWD` returns present working directory
* `SHELL` returns which Shell program is being used 
* `USER` returns the user's ID
## How to print a variables value
To print a value use `echo` along with `$` when echoing variables. 
## How to define and access shell variables
To define your own shell variables use `variable=path/to_file.csv` and then check with `echo $variable`. 
## For loop in the terminal
The syntax for this is `for filetype in gif jpg png; do echo $filetype; done`. <br>
Also, `for filename in seasonal/*.csv; do echo $filename; done`. 
```shell
$ for f in seasonal/*.csv; do echo $f head -n 2 $f | tail -n 1; done
seasonal/autumn.csv head -n 2 seasonal/autumn.csv
seasonal/spring.csv head -n 2 seasonal/spring.csv
seasonal/summer.csv head -n 2 seasonal/summer.csv
seasonal/winter.csv head -n 2 seasonal/winter.csv
$
```
## How can I edit a file? 
To access a simple text editor in the terminal use `nano <filename>`. <br>
```text
Ctrl + K: delete a line.
Ctrl + U: un-delete a line.
Ctrl + O: save the file ('O' stands for 'output'). You will also need to press Enter to confirm the filename!
Ctrl + X: exit the editor.
```
## How to save commands and run later?
1. First save the commands to a file header.sh.
```shell
head -n 1 file/*.csv 
```
2. run the command by running the file using `bash`. 
```shell
bash header.sh
```
## How to write loops in the shell.
```shell
# Print the first and last data records of each file.
for filename in $@
do
    head -n 2 $filename | tail -n 1
    tail -n 1 $filename
done
```
