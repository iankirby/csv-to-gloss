import re, sys, os, subprocess, datetime,csv


#These are the default values.  Currently this only accepts a single command line argument, being the csv.
glossKey="./In/glossKey.csv"
template="./In/template.tex"
trnsKey="./in/trnsKey.csv"

if(len(sys.argv)>2):
    sys.exit("Multiple command line arguments not supported.  Dying")
elif(len(sys.argv)==2):
    examples="examples.csv"
else:
    examples="examples.csv"

with open(examples,encoding="utf8") as f:
    examples=f.read()+"\n"


examples=re.sub(",\s*",",",examples) #removes spaces after commas
examples=re.sub("[\s]*,",",",examples)#removes spaces before commas
examples=re.split("\n",examples)

print(len(examples))
ex=[]
i=0
while(i<len(examples)):
    temp=examples[i]
    print(temp)
    temp=re.split(",",temp)
    if(len(temp)>1):
        if(temp[0]==''):
            temp[0]=temp[0]+" "
        ex.append(temp)
    i+=1
print(ex)
# print(len(ex))

#read in the latex template that will be read
tex_in=open("./In/template.tex","r+",encoding="utf8")
x=tex_in.read()
tex_in.close()

# begin="%% Beginning of commands"
# end="\%\% End of commands"
# x=re.split(begin,x)

# head=x[0]+"\n"+begin

# begin_document="\\begin\{document\}"
# x=re.split(begin_document,x)

# head=x[0]+"\n"+begin_document
# tail=x[1]

end_document=r'\\end\{document\}'
head=re.split(end_document,x)
head=head[0]+"\n"


#Find the time that the script was called
d=datetime.datetime.utcnow()
dm="{:%h%d}".format(d)
dm=dm+"-"
hm="{:%H%M}".format(d)
time_got=dm+hm

out_name="./Out/outputfile_"+time_got+".tex"

tex_out=open(out_name,"a",encoding="utf8")
tex_out.truncate(0) #
tex_out.write(head+"\n")

# tex_out.write(head)
print(len(ex))
i=0
while(i<len(ex)):
    temp=ex[i]
    tex_out.write("\\exg."+temp[0]+temp[1]+"\\\\\n"+temp[2]+"\\\\\n"+"`"+temp[3]+"'\n\n")
    i=i+1
tex_out.write(end_document)




#This stuff is for later
##################################
# Read in the gloss key list
# gloss_in=open("./In/glossKey.csv","r",encoding="utf8")
# glossKey=gloss_in.read()
# gloss_in.close()



# glossKey=re.sub("\n\n","",glossKey) #Remove empty lines
# glossKey=re.sub(",\s*",",",glossKey) #remove any spaces after comma
# glossKey=re.split("\n",glossKey)


#This code is for adding special commands.  it's not ready yet
# glossKey2=[]
# i=0
# while(i<len(glossKey)):
#     temp=glossKey[i]
#     if(re.search(",",temp)==False):
#         temp=temp+","
#     temp=re.split(",",temp)
#     glossKey2.append(temp)
#     if(temp[1]!=''):
#         tex_out.write("\\newcommand{\\"+temp[0]+"}{"+temp[1]+"}")
#         tex_out.write("\n")
#     i=i+1
