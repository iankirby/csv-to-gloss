import time, re, sys, os, subprocess,random, string

from numpy import character


def method_one():
    t0=time.time()
    print("Open at beginning and write all at once.")
    file=open("examples.csv",'r',encoding='utf8')
    examples=file.read()
    file.close()
    examples=re.split("\n",examples)
    
    ex=[]
    i=0
    while(i<len(examples)):
        ex.append(re.split(",",examples[i]))
        i=i+1

    # print(ex)

    file=open("transcriptionKey.txt",'r',encoding='utf8')
    key=file.read()
    file.close()

    key=re.split("\n",key)
    key2=[]
    i=0
    while(i<len(key)):
        key2.append(re.split(',',key[i]))
        i=i+1
    
    x=[]
    i=0
    while(i<len(ex)):
        words=ex[i]
        y=[]
        j=0
        while(j<len(words)):
            k=0
            per=words[j]
            while(k<len(key2)):
                key_item=key2[k]
                per=re.sub(key_item[0],key_item[1],per)
                k=k+1
            y.append(per)
            j=j+1
        x.append(y)
        i=i+1
    print(x)


    print(time.time()-t0)

def method_two():
    t0=time.time()

    file=open("examples.csv",'r',encoding='utf8')
    examples=file.read()
    file.close()
    examples=re.split("\n",examples)
    
    ex=[]
    i=0
    while(i<len(examples)):
        ex.append(re.split(",",examples[i]))
        i=i+1

    # print(ex)

    file=open("transcriptionKey.txt",'r',encoding='utf8')
    key=file.read()
    file.close()

    key=re.split("\n",key)
    key2=[]
    i=0
    while(i<len(key)):
        key2.append(re.split(',',key[i]))
        i=i+1


    # print(time.time()-t0)


def save_thing(x,name,time_start):

    file=open(name,"a",encoding="utf8")
    i=0
    while(i<len(x)):
        curr=x[i]
        file.write(curr[0]+", "+curr[1]+"\n")
        i=i+1
    file.close()
    time_end=time.time()
    print("Time: "+str(time_start-time_end))
    

def make_list():
    t1=time.time()
    #Make the list of things that I'm going to save it to 
    i=0
    a=[]
    while(i<30):
        b=[]
        letters=string.ascii_letters
        b.append(''.join(random.choice(letters) for k in range (1)))
        b.append(''.join(random.choice(letters) for k in range (1)))
        a.append(b)
        i=i+1
    # print(a)
    # save_thing(a,"transcriptionKey.txt",t1)
        


def make_examples():
    t0=time.time()

    x=[]
    i=0
    while (i<500):
        y=[]
        a=random.randint(1,10)
        j=0
        while(j<a):
            b=random.randint(1,10)
            letters=string.ascii_letters
            y.append(''.join(random.choice(letters) for k in range(b)))
            j=j+1
        # print(y)
        x.append(y)
        i=i+1

    file=open("examples.csv",'a',encoding='utf8')
    i=0
    while(i<len(x)):
        curr=x[i]
        j=0
        while(j<(len(curr)-1)):
            file.write(curr[j]+", ")
            j=j+1
        else:
            file.write(curr[-1]+"\n")
        i=i+1
    else:
        t1=time.time()
        print("time elapsed: "+ str(t1-t0))
   

method_one()

# make_examples()
# make_list()

