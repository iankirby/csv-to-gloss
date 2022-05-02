import re, subprocess, os, datetime, csv, sys
from urllib.request import urlopen



def print_out_array(ex,tex):


    #find the date and time that the script was called
    d=datetime.datetime.utcnow()
    dm="{:%h%d}".format(d)
    dm=dm+"-"
    hm="{:%H%M}".format(d)
    time_got=dm+hm
    

    out_name="Output/output_"+time_got+".tex"

    tex_out=open(out_name,"a",encoding="utf8")
    # tex_out.truncate(0)

    

    template="./Tex_Templates/"+tex
    file=open(template,'r',encoding="utf8")
    template=file.read()
    file.close()
    template=re.sub(r'\\end{document}',"",template) #strip off the end of the document
    # print(template)


    tex_out.write(template+"\n")

    i=0
    while(i<len(ex)):
        curr=ex[i]
        tex_out.write(curr[0]+"\n"+curr[1]+"\n"+curr[2]+"\n\n")
        # # top=curr[0]
        # middle=curr[1]
        # bottom=curr[2]
        i=i+1
    tex_out.write("\\"+"end{document"+"}")
    tex_out.close()

    print("Script written by Ian Kirby.  Thank you for using it.")

# def format_examples_and_add(ex,tex):

def check_glossKey():
    print("this is not complete yet")


#This is a loop that does most of the work here...
def temp_read_examples(examples,tkey,template):
    examples=sys.argv[1]
    file=open(examples,"r",encoding="utf8")
    examples=file.read()
    file.close()
    # print(examples)

    examples=re.split("\n",examples)
    new_ex=[]
    i=0
    while (i<len(examples)):
        curr_line=examples[i]
        curr_line=re.split(",",curr_line)
        # print(curr_line)
        if (len(curr_line)>1):
            new_ex.append(curr_line)
            # print(curr_line)
        i=i+1
    
    


    transcription_key="./Keys/"+tkey
    file=open(transcription_key,"r",encoding="utf8")
    transcription_key=file.read()
    file.close()
    transcription_key=re.split("\n",transcription_key)
    # print(transcription_key)
    i=0
    transcription_new=[]
    while (i<len(transcription_key)):
        curr=transcription_key[i]
        if(len(curr)>1):
            curr=re.split(",",curr)

            #get rid of any empty spaces at the beginning of the string...
            tmp=curr[1]
            if(tmp[0]==' '):
                tmp=tmp[1:]
                curr.pop(1)
                curr.append(tmp)
            #now check to see if the element ends in braces.  Add them around the whole thing if not.

            tmp=curr[1]
            if(tmp[-1]!="}"):
                curr.pop(1)
                tmp="{"+tmp+"}"
                curr.append(tmp)
            transcription_new.append(curr)
        i=i+1
    # print(transcription_new)

    ex=[]
    i=0
    while (i<len(new_ex)):
        
        out_ex=[]
        curr_ex=new_ex[i]
        jdg=curr_ex[0]
        if (len(jdg)!=0 and jdg=="#"):
            jdg="\\#"
        top_line=curr_ex[1]
        # print(top_line)
        if ((len(top_line)!=0) and top_line[0]==' '):
            top_line=top_line[1:]
        top_line="\\exg."+jdg+top_line+"\\\\"
        # print(top_line)

        #Here is where I will need to deal with transcription stuff
        j=0
        while (j<len(transcription_new)):
            curr_trns=transcription_new[j]
            pat, repl =curr_trns[0], repr(curr_trns[1])
            top_line=re.sub(pat, repl,top_line)
            # print(x)
            j=j+1
        top_line=re.sub('\'','',top_line)
        out_ex.append(top_line)
        # print(top_line)


        middle_line=curr_ex[2]
        #get rid of first space, if there is one
        if(len(middle_line)>1 and middle_line[0]==' '):
            middle_line=middle_line[1:]
        
        middle_as_array=re.split("(\W)",middle_line)
        # print(middle_as_array)
      
        # print(middle_as_array)
        middle_new=""
        j=0
        while (j<len(middle_as_array)):
            curr_word=middle_as_array[j]
            if(str.isupper(curr_word)):
                curr_word="\\textsc{"+str.lower(curr_word)+"}"
            middle_new=middle_new+curr_word
            j=j+1
        middle_new=re.sub(' - ','-',middle_new)
        middle_new=re.sub(' = ','=',middle_new)
        middle_new=re.sub(' \. ', '.',middle_new)
        # print(middle_new)
        middle_new=middle_new+"\\\\"
        # middle_new=re.sub('(\w\w)', ' ', middle_new)
        # print(middle_new)
        out_ex.append(middle_new)


        bottom_line=curr_ex[3]
        if(len(bottom_line)>1 and bottom_line[0]==' '):
            bottom_line=bottom_line[1:]
        bottom_line="`"+bottom_line+"'"
        # print(bottom_line)
        out_ex.append(bottom_line)

        ex.append(out_ex)
        i=i+1
    print_out_array(ex,template)
    # print(ex)

# def check_key():
#     print("hi")

#Check to see if there are command line arguments, and if so, verify that they are in the file structure...
def check_command_line_args():
    
    dir=os.listdir('.')
    tex_dir=os.listdir('./Tex_Templates')
    key_dir=os.listdir('./Keys')

    #default location for key, etc
    tkey="transcriptionKey.csv"
    tex="template.tex"
    

    if (len(sys.argv)==1):
        sys.exit("You did not specify an example file.")
    elif (len(sys.argv)>1 and len(sys.argv[1])>4):
        x=sys.argv[1]
        i=0
        while (i<len(dir)):
            if (x==dir[i]):
                break
            else:
                i=i+1
        else:
            print("I did not find a file titled: \""+x+"\" in the current directory.  Please include your example spreadsheet in the same file as toGloss.py!")
            sys.exit()
    #Checking the other command line arguments.

    error="Mistake in command line arguments.  The relevant keys tags are:\n\"-tkey\" for your transcription key\n\"-tex\" for your tex template\n\"-gkey\" for glossing key.\n Alternatively, perhaps you forgot to enter the name of the file afterwards?"
    no_glossing_key="\nNote that the glossing key functionality is not currently active."
    error_bool=False
   
    if (len(sys.argv)>2):
        if((len(sys.argv)%2)!=0):
            sys.exit(error+no_glossing_key)
        else:
            i=2
            while (i<len(sys.argv)):
                if (sys.argv[i]=="-tkey"):
                    tkey=sys.argv[i+1]
                    j=0
                    while (j<len(key_dir)):
                        if (tkey==key_dir[j]):
                            break
                        else:
                            j=j+1
                    else:
                        print("I didn't not find \""+tkey+"\" in your Key subdirectory.  Perhaps you mistyped it or put it in another file?")
                        error_bool=True
                elif(sys.argv[i]=="-tex"):
                    tex=sys.argv[i+1]
                    j=0
                    while (j<len(tex_dir)):
                        if(tex==tex_dir[j]):
                            break
                        else:
                            j=j+1
                    else:
                        print("I did not find \""+tex+"\" in your Tex_Template subdirectory.  Perhaps you mistyped it or put it in another file?")
                        error_bool=True
                elif(sys.argv[i]=="-gkey"):
                    print(no_glossing_key+" So I am ignoring "+sys.argv[i]+" "+sys.argv[i+1])
                else:
                    print("I do not recognize tag \""+sys.argv[i]+"\"")
                    sys.exit(error+no_glossing_key)

                i=i+2
    if(error_bool==True):
        sys.exit()
    else:
        temp_read_examples(sys.argv[1],tkey,tex)
    #verify that this file is in the directory...    



#Verifying that the file structure includes proper subdirectories, create them if not.
def check_file_structure():

    dir=os.listdir(".") #list of files in the current directory.

    #check to see that the right files are there, and if they're not, it will create the files.
    check_key, check_tex, check_out= False, False, False
    i=0
    while (i<len(dir)):
        if (dir[i]=="Tex_Templates"):
            check_tex=True
        if (dir[i]=="Keys"):
            check_key=True
        if (dir[i]=="Output"):
            check_out=True
        i=i+1
    
    if (check_key==False):
        os.mkdir("Keys")
        file=open("./Keys/transcriptionKey.csv","a",encoding="utf8")
        file.close()
        file=open("./Keys/glossKey.csv","a",encoding="utf8")
        file.close()
        # print("See documentation on how to use keys.")
    if (check_out==False):
        os.mkdir("Output")

    
    if (check_tex==False):
        os.mkdir("Tex_Templates")

    texDir=os.listdir('./Tex_Templates')
    has_linguex=False
    i=0
    while (i<len(texDir)):
        if (texDir[i]=="template.tex"):
            has_linguex=True
        i=i+1
    if (has_linguex==False):

        file=open("Tex_Templates/template.tex","a", encoding="utf8")
        # file=file.read()
        template="\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{tipa}\n\\usepackage{textgreek}\n\\usepackage{pifont}\n\\usepackage{linguex}\n\n\\begin{document}\n\n\\end{document}"


        file.write(template)
        file.close() 

    check_command_line_args()
    # temp_read_examples()

check_file_structure()