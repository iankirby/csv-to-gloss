import re, subprocess, os, datetime, csv, sys

def check_subdir():

def check_sysargs():

    if(len(sys.argv)==1):
        examples=ask_for_examples("Example",'.')

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
    
    check_sysargs()


check_files()