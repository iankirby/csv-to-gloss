import re, subprocess, os, datetime, csv, sys


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

    #check to see that the right files are there, and if they're not, it will create the files.
    check_key, check_tex, check_out= False, False, False
    i=0
    while (i<len(dir)):
        if (dir[i]=="Tex_Templates"):
            check_in=True
        if (dir[i]=="Output"):
            check_out=True
        i=i+1
    
    if (check_key==False):
        os.mkdir("Keys")

    
    if (check_tex==False):

    if (check_out==False):
        os.mkdir("Out")
     

    # check_command_line_args()

check_file_structure()