import random
import sys
sys.stdout.reconfigure(encoding='utf-8')

def chaosKeyWord(key,ln):
    n=len(key)
    res="/"
    newIndex=random.sample(range(n), n)
    for i in newIndex:
        if(key[i]==' '):
            res+='_'
            ln-=1
        else:
            res+=key[i]
        res+='/'
    return res,ln

def questionHidedKey(ques,key):
    start=ques.find(key)
    if start>=0:
        subques=list(ques)
        n=len(key)    
        for i in range(start,start+n):
            subques[i]='*'
        return ( "".join(subques))     
    else: return ("")

def choiceClue(key):
    spl=key.split()
    clue=spl[random.randrange(0,len(spl))]
    return clue

def checkAns(key,ans):
    if key==ans:
        return True
    return False


def processQuestion(stt,key,ln):
    res="CÂU HỎI " +str(stt)+" :\n"
    res+="-Từ khoá có "+str(ln)+" chữ.\n\t\t "+key
    return res



def listQuestion(filepath):
    listques=[]
    f = open(filepath,"r",encoding="utf8").read().splitlines()
    n = int(f[0])
    for i in range(n):
        stt=i+1
        ans =f[2*i+1]        
        keyAns=f[2*i+2]
        lnAns=len(keyAns)
        tmp=chaosKeyWord(keyAns,lnAns)
        key=tmp[0]
        lnAns=tmp[1]
        clue1="Gợi ý:\n"+questionHidedKey(ans,keyAns)
        clue2="\nCó chứa từ: "+choiceClue(keyAns)
        ques=processQuestion(stt,key,lnAns)
        listques.append([ques,ans,keyAns,[clue1,clue2]])
    return listques


# l=listQuestion("ques.txt")
# print(l[0])


        
        
            



