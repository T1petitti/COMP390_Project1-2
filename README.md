Tyler Petitti
COMP390-001
AS OF DECEMBER 23rd, 2023

GITHUB LINK: https://github.com/T1petitti/COMP390_Project1-2

Packages needed for installation: 
os
pathlib
xlwt
datetime
pytest

*** Project Program Overview ***

- OPENS AND READS METEOR FILE 
- FILTERS AND EXTRACTS DATA OF METEORITE LANDING BASED ON USER INPUT 
- USER CHOICE OF FILTERING BY MASS OR YEAR OF METEORITE LANDING 
- DISPLAYS DESIRED DATA IN FORMATTED TABLE IN EITHER THE TERMINAL / A TXT FILE / AN EXCEL FILE

GUIDE:
1. Read "Welcome Message" for brief overview of program
2. Type the file name of the file containing meteor data (ex. 'meteorite_landings_data.txt')
3. Type the letter of the file mode you want to open the file with, reading is default and preferred (ex. 'r')
4. Type 1 to filter data from file based on Mass of meteor or....  
5. Type 2 to filter data from file based on Year of meteor landing
6. Enter Lower Limit of data you want to filter (ex. 10)
7. Enter Upper Limit of data you want to filter (ex. 100)
8. Enter Output option you would like the data to be visualized in; terminal, txt file, or Excel file
9. Finally, this will then create a formatted table of every meteor that matches your filter options in the output option of your choice.

*** No Unit Tests were created using pytest however there is error handling all throughout the program ***
