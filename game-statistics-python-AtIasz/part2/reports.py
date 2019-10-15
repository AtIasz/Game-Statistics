
# Report functions
path="game_stat.txt"

def get_most_played(file_name):
    statfile=open(file_name,"r")
    n=0
    name=""
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            if len(lisalisa[0])!=0:
                if n<float(lisalisa[1]):
                    n=float(lisalisa[1])
                    name=lisalisa[0]
            r=l.readline()
            lisalisa=r.split("\t")
    return name
def sum_sold(file_name):
    statfile=open(file_name,"r")
    n=0
    name=""
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            if len(lisalisa[0])!=0:
                
                n+=float(lisalisa[1])
            r=l.readline()
            lisalisa=r.split("\t")
    return n
def get_selling_avg(file_name):
    statfile=open(file_name,"r")
    n=0
    cnt=1
    name=""
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        
        while r:
            cnt+=1
            if len(lisalisa[0])!=0:
                
                n+=float(lisalisa[1])
            r=l.readline()
            lisalisa=r.split("\t")
    return n/cnt
def count_longest_title(file_name):
    statfile=open(file_name,"r")
    listli=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listli.append(lisalisa[0])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            
            if len(lisalisa[0])!=0:
                listli.append(lisalisa[0])
    listli.remove(listli[-1])
    word=""
    ll=0
    for i in range(len(listli)):
        if len(listli[i])>len(word):
            ll=int(len(listli[i]))
            word=listli[i]
    return ll
def get_date_avg(file_name):
    statfile=open(file_name,"r")
    listli=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listli.append(lisalisa[2])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            
            if len(lisalisa[0])!=0:
                listli.append(lisalisa[2])
    listli.remove(listli[-1])
    sm=0
    for i in range(len(listli)):
        sm+=int(listli[i])
    
    return round(sm/len(listli))
def get_game(file_name, title):
    statfile=open(file_name,"r")
    with open(file_name)as l:
        t=0
        i=0
        r=0
        g=0
        p=0
        li="["
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            z=lisalisa[-1]
            w=""
            if "\n" in z:     
                for i in range(len(z)-1):
                    w+=z[i]        
            lisalisa[-1]=w
            if len(lisalisa[0])!=0:
                if title==lisalisa[0]:
                    li+='"'+str(lisalisa[0])+'", '
                    li+=str(float(lisalisa[1]))+', '
                    li+=str(int(lisalisa[2]))+', '
                    li+='"'+str(lisalisa[3])+'", '
                    li+='"'+str(lisalisa[4])+'"]'
            r=l.readline()
            lisalisa=r.split("\t")
    return li                    
def count_grouped_by_genre(file_name):    
    statfile=open(file_name,"r")
    listgen=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listgen.append(lisalisa[3])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            
            if len(lisalisa[0])!=0:
                listgen.append(lisalisa[3])
    listgen.remove(listgen[-1])
    lest=[]
    for i in range(len(listgen)):
        if listgen[i] not in lest:
            lest.append(listgen[i])
    thisdict={}
    nums=[0,0,0,0,0,0,0]
    
    for i in range(len(listgen)):
        if listgen[i] ==lest[0]:
            nums[0]+=1
        if listgen[i] ==lest[1]:
            nums[1]+=1
        if listgen[i] ==lest[2]:
            nums[2]+=1
        if listgen[i] ==lest[3]:
            nums[3]+=1
        if listgen[i] ==lest[4]:
            nums[4]+=1
        if listgen[i] ==lest[5]:
            nums[5]+=1
        if listgen[i] ==lest[6]:
            nums[6]+=1
    for i in range(len(nums)):
        thisdict.update({lest[i]:nums[i]})
    return thisdict      
def get_date_ordered(file_name):
    statfile=open(file_name,"r")
    listgen=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listgen.append(lisalisa[0])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            
            if len(lisalisa[0])!=0:
                listgen.append(lisalisa[0])
    listgen.remove(listgen[-1])
    lest=[]
    for i in range(len(listgen)):
        if listgen[i] not in lest:
            lest.append(listgen[i])
    return listgen[::-1]


text=open("part2/export.py","a")
text.write("'''")
text.write("\n")
text.write(str(get_most_played(path)))
text.write("\n")
text.write(str(sum_sold(path)))
text.write("\n")
text.write(str(get_selling_avg(path)))
text.write("\n")
text.write(str(count_longest_title(path)))
text.write("\n")
text.write(str(get_date_avg(path)))
text.write("\n")
text.write(str(get_game(path, "Terraria")))
text.write("\n")
text.write(str(count_grouped_by_genre(path)))
text.write("\n")
text.write(str(get_date_ordered(path)))
text.write("\n")
text.write("'''")