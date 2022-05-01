import re, subprocess, os, datetime, csv, sys, webbrowser


def check_command_line_args():

    #Check the command line arguments first...
    if (len(sys.argv)==1):
        sys.exit("You did not specify an example file.")
    elif (len(sys.argv)>1):
        x=sys.argv[1]
        if ((not len(x)>3) or (x[-4:]!=".csv")):
            print("hi")



#Verifying that the file structure includes In, Out
def check_file_structure():

    dir=os.listdir(".") #list of files in the current directory.

    check_in, check_out= False, False
    i=0
    while (i<len(dir)):
        if (dir[i]=="In"):
            check_in=True
        if (dir[i]=="Out"):
            check_out=True
        
        i=i+1
    if (check_in==False):
       
        webbrowser.open("https://github.com/iankirby/csv-to-gloss", new=2)
        sys.exit("You have called this program in a directory that does not contain the correct file structure!  Opening documentation...")

    if (check_out==False):
        os.mkdir("Out")
     

    # check_command_line_args()

check_file_structure()