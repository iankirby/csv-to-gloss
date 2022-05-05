import re, subprocess, os, datetime, csv, sys


def write_to_tex(x,file):
    file.write(x)
    return file


def read_stuff_in(ex,gloss,translit,tex):

    file=open("./Tex_Templates/"+tex,'r',encoding='utf8')
    tex=file.read()
    file.close()
    tex=re.sub(r'\\end{document}','',tex) #remove \end{document}

    d=datetime.datetime.utcnow()
    dm="{:%h%d}".format(d)
    dm=dm+"-"
    hm="{:%H%M}".format(d)
    time_got=dm+hm

    out_file="Output/output_"+time_got+".tex"
    file_output=open(out_file,'a',encoding="utf8")
    file_output.write(tex)

    file=open(ex,'r',encoding='utf8')
    ex=file.read()
    file.close()
    
    ex=re.split('\n',ex)
    i=0
    while(i<len(ex)):
        output=write_to_tex(ex[i]+"\n",file_output)
        i=i+1

   
    # write_to_file("hello",tex)
 

#Check that the file is in the appropriate directory
def verify_file_present(fl,dir):
    i=0
    while(i<len(dir)):
        if(dir[i]==fl):
            break
        i=i+1
    else:
        sys.exit("I did not find file \""+fl+"\" in the directory.")

#Check that the system arguments have been entered properly and that they're in the right file directory
def check_sys_args():

    gloss="glossKey.txt"
    translit="transliterationKey.txt"
    tex="template.tex"

    error_message="The relevant tags are:\n -gkey \t (glossing keys; currently not active)\n -tkey \t(transliteration key)\n -tex \t (LaTeX template)"


    if((len(sys.argv)%2)!=0):
        sys.exit("Not enough arguments provided.\n"+error_message)
    elif(len(sys.argv)>1):
        ex=sys.argv[1]
        dir=os.listdir('.')
        verify_file_present(ex,dir)
    
    if(len(sys.argv)>2):
        i=2
        while(i<len(sys.argv)):
            curr=sys.argv[i]
            if(curr=="-gkey"):
                gloss=sys.argv[i+1]
                dir=os.listdir('./Glossing_Keys/')
                verify_file_present(gloss,dir)
            elif(curr=="-tkey"):
                translit=sys.argv[i+1]
                dir=os.listdir('./Transliteration_Keys/')
                verify_file_present(translit,dir)
            elif(curr=="-tex"):
                tex=sys.argv[i+1]
                dir=os.listdir('./Tex_Templates/')
                verify_file_present(tex,dir)

            else:
                sys.exit("I do not recognize \""+curr+"\" as a tag\n"+error_message)
            i=i+2
    read_stuff_in(ex,gloss,translit,tex)


def check_files():
    
    dir=os.listdir('.')
    glosses, transliteration, tex, output=False, False, False, False

    i=0
    while(i<len(dir)):
        if(dir[i]=="Glossing_Keys"):
            glosses=True
        if(dir[i]=="Transliteration_Keys"):
            transliteration=True
        if(dir[i]=="Tex_Templates"):
            tex=True
        if(dir[i]=="Output"):
            output=True
    
        i=i+1

    if(glosses==False):
        os.mkdir("Glossing_Keys")
        file=open("./Glossing_Keys/glossKey.txt",'a',encoding="utf8")
        file.close()
    if(transliteration==False):
        os.mkdir("Transliteration_Keys")
        file=open("./Transliteration_Keys/transliterationKey.txt",'a',encoding='utf8')
        file.close()
    if(tex==False):
        os.mkdir("Tex_Templates")
        file=open("./Tex_Templates/template.tex",'a',encoding='utf8')
        file.write("\\documentclass{article}\n\\usepackage[utf8]{inputenc}\n\\usepackage{tipa}\n\\usepackage{textgreek}\n\\usepackage{pifont}\n\\usepackage{linguex}\n\n\\begin{document}\n\n\\end{document}")
        file.close()
    if(output==False):
        os.mkdir("Output")

    if(len(sys.argv)>1):
        check_sys_args()
    else:
        sys.exit("No command line arguments provided.")
    


check_files()