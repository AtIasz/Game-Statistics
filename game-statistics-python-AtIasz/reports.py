
# Report functions
path="game_stat.txt"

def count_games(file_name):
    statfile=open(file_name,"r")
    cnt=0
    with open(file_name)as l:
        line=l.readline()
        cnt+=1
        while line:
            line=l.readline()
            cnt+=1
    return cnt
def decide(file_name, year):
    statfile=open(file_name,"r")
    isthere=False
    with open(file_name)as l:
        line=l.readline()
        while line:
            if str(year) in line:
                isthere=True
                return isthere
            line=l.readline()
    return isthere
def get_latest(file_name):
    statfile=open(file_name,"r")
    latest=0
    lN=""
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            r=lisalisa[-1]
            w=""
            if "\n" in r:     
                for i in range(len(r)-1):
                    w+=r[i]       
            lisalisa[-1]=w
            if len(lisalisa[0])!=0:
                o=int(lisalisa[2])
                if o>latest:
                    latest=o
                    lN=lisalisa[0]
    return lN
def count_by_genre(file_name, genre):
    statfile=open(file_name,"r")
    cnt=0
    
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            r=lisalisa[-1]
            w=""
            if "\n" in r:     
                for i in range(len(r)-1):
                    w+=r[i]       
            lisalisa[-1]=w
            if len(lisalisa[0])!=0:
                if lisalisa[3]==genre:
                    cnt+=1
    return cnt
def get_line_number_by_title(file_name, title):
    statfile=open(file_name,"r")
    cnt=0
    
    with open(file_name)as l:
        r=l.readline()
        cnt+=1
        lisalisa=r.split("\t")
        while r:
            if title==lisalisa[0]:
                return cnt
            r=l.readline()
            cnt+=1
            lisalisa=r.split("\t")
            r=lisalisa[-1]
            w=""
            if "\n" in r:     
                for i in range(len(r)-1):
                    w+=r[i]       
            lisalisa[-1]=w
        raise ValueError
def sort_abc(file_name):
    statfile=open(file_name,"r")
    listli=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listli.append(lisalisa[0])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            listli.append(lisalisa[0])
    listli.remove(listli[-1])
    s="abcdefghijklmnopqrstuvwxyz 0123456789"
    return sorted(listli)
def get_genres(file_name):    
    statfile=open(file_name,"r")
    listli=[]
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        listli.append(lisalisa[3])
        while r:
            r=l.readline()
            lisalisa=r.split("\t")
            
            if len(lisalisa[0])!=0:
                listli.append(lisalisa[3])
    listli.remove(listli[-1])
    s="abcdefghijklmnopqrstuvwxyz 0123456789"
    
    return sorted(set(listli))
def when_was_top_sold_fps(file_name):
    statfile=open(file_name,"r")
    cnt=2020
    num=0
    with open(file_name)as l:
        r=l.readline()
        lisalisa=r.split("\t")
        while r:
            if len(lisalisa[0])!=0:
                if lisalisa[3]=="First-person shooter":
                    if float(num)<float(lisalisa[1]):
                        num=float(lisalisa[1])
                        cnt=int(lisalisa[2])
                r=l.readline()
                lisalisa=r.split("\t")
        if cnt!=2020:
            return cnt
        else:
            raise ValueError




text=open("export.py","a")
text.write("'''")
text.write("\n")
text.write(str(count_games(path)))
text.write("\n")
text.write(str(decide(path, 1996)))
text.write("\n")
text.write(str(get_latest(path)))
text.write("\n")
text.write(str(count_by_genre(path, "RPG")))
text.write("\n")
text.write(str(get_line_number_by_title(path, "Minecraft")))
text.write("\n")
text.write(str(sort_abc(path)))
text.write("\n")
text.write(str(get_genres(path)))
text.write("\n")
text.write(str(when_was_top_sold_fps(path)))
text.write("\n")
text.write("'''")

text.close()
