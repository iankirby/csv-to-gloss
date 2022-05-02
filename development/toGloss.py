import re, sys, os, subprocess, datetime,csv

def check_for_examples(examples):
    
    dir=os.listdir('./')
    i=0
    while(i<len(dir)):
        if(dir[i]==examples):
            print("found in dir")
            break
        else:
            i=i+1
    dir=os.listdir('./In/')
    i=0
    while(i<len(dir)):
        if(dir[i]==examples):
            print("found in subdir")
            break
        else:
            i=i+1

def check_command_line_arguments():

    # These are the default files
    examples="examples.csv"
    glossKey="./In/glossKey.csv"
    template="./In/template.tex"
    trnsKey="./in/trnsKey.csv"

    # i=1
    # while(i<len(sys.argv)):
    #     if(sys.argv[i]==)



    if (len(sys.argv)>1):
        check_for_examples(sys.argv[1])
        read_examples(examples,glossKey,template,trnsKey)
    if(len(sys.argv)==1):
        examples="examples.csv"
    else:
        print("I couldn't find \""+examples+"\"")

    read_examples()




    
def read_examples(ex,gl,tmpl,trnsk):

    print(ex)
    print(gl)
    print(tmpl)
    print(trnsk)

    #Read in the csv file
    with open("test.csv",encoding="utf8") as f:
        var1=f.read()+"\n"
    
    var1=re.split("\n",var1)

    #remove empty line breaks...
    var2=[]
    i=0
    while(i<len(var1)):
        if():
            var2.append(var1[i])
        i=i+1
    
    examples=[]
    i=0
    while (i<len(var1)):
        temp=var1[i]
        temp=re.split(",",temp)

        # add to examples array only if there are three cells filled
        if(len(temp)>1):
           examples.append(temp)
        i+=1
    # print(examples)
    # print(len(examples))




def read_head():

    #Read in the the latex template file

    tex_in=open("./In/template.tex","r+",encoding="utf8")
    x=tex_in.read()
    tex_in.close()

    begin="%% Beginning of commands"
    # end="\%\% End of commands"
    x=re.split(begin,x)

    head=x[0]+"\n"+begin

    tex_out=open("./Out/test_out.tex","a",encoding="utf8")
    tex_out.truncate(0) #
    tex_out.write(head+"\n")

    # Read in the gloss key list
    gloss_in=open("./In/glossKey.csv","r",encoding="utf8")
    glossKey=gloss_in.read()
    gloss_in.close()


    glossKey=re.sub("\n\n","",glossKey) #Remove empty lines
    glossKey=re.sub(",\s*",",",glossKey) #remove any spaces after comma
    glossKey=re.split("\n",glossKey)

    glossKey2=[]
    i=0
    while(i<len(glossKey)):
        temp=glossKey[i]
        if(re.search(",",temp)==False):
            temp=temp+","
        temp=re.split(",",temp)
        glossKey2.append(temp)
        if(temp[1]!=''):
            tex_out.write("\\newcommand{\\"+temp[0]+"}{"+temp[1]+"}")
            tex_out.write("\n")
        i=i+1



    print(glossKey)
    print(len(glossKey))

    print(glossKey2)
    print(len(glossKey2))

check_command_line_arguments()


# read_head()