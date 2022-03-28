# FeedbackGenerator
The Feedback Generator ist a script for creating feedback files for  computer science students at the Philipps University Marburg.
The output is a feedback file for each student listed in the member file. 

Version 2.2  
Author: Patrick Fock

**Syntax:**
```cmd
python feeback_generator.py <path of member file> <destination path> <points of exercise one> ... <points of exercise n> <points of bonus exercise>  
```
 The member file needs to be of string type. If <path of member file> is "" or "default", a single feedback file "Bewertung_.txt" will be generated.
If the last argument <points of bonus exercise> is a "0", the bonus exercise won't be created.
__________________________________________________________________________________________________________________________________________________________ 
Example call:
```cmd
python feeback_generator.py "members.txt" "C:\Documents" 2 3 8  
```
This creates the following file content:

AUFGABE 1  
\****************************************************************************************************  
Punkte: 0/2

AUFGABE 2  
\****************************************************************************************************  
Punkte: 0/3

BONUS  
\****************************************************************************************************  
Punkte: 0/8

\****************************************************************************************************  
GESAMT 0/5 + BONUS 0/8
