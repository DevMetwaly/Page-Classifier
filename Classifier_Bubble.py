### PAGES CLASSIFIER v1.3 ###
myfile=input("Please insert the file name. (ex: mytext.txt)\n .../")
verbs1=open('verbs1.txt','r').read().split('\n')        #Original Verbs (The Base)
verbs2=open('verbs2.txt','r').read().split('\n')        #Verb Past
verbs3=open('verbs3.txt','r').read().split('\n')        #Verb Past Participle
verbs4=open('verbs4.txt','r').read().split('\n')        #Verb +[es/s]
verbs5=open('verbs5.txt','r').read().split('\n')        #Verb +[ing]
txt=open(myfile+'.txt','r').read().lower().split()
Common=open("CommonWords.txt",'r').read().split(',')
print('\nWords found: ',len(txt))
Keywords=int(input('\nShow (n) of top keywords. Insert (n): '))
from Mapping import CorrectWord                         #The verbs database
import time
all_time = time.time()
start_time = time.time()


def Text_Cleaner(txt):                                  #Returns the clean text
    length=len(txt)
    i=0
    while(i<length):                                    #Checks the type of the verb
        WordLength=len(txt[i])
        if WordLength>2 and txt[i][-1]=='s' and (txt[i][-2]=="'" or txt[i][-2]=='’'):
            txt[i]=txt[i][:-2]
        elif WordLength>2 and (txt[i][-1]=="'" or txt[i][-1]=='’') and txt[i][-2]=="s":
            txt[i]=txt[i][:-2]
        elif ord(txt[i][0]) not in range(97,123):
            txt[i]=' '
        elif  ord(txt[i][-1]) not in range(97,123):
            txt[i]=txt[i][:-1]
        base_form=get_base_form(txt[i])                 #Searches for the original verb
        if base_form != False:
            txt[i]=base_form
        i+=1

        
def get_base_form(word):                                #Used in Text_Cleaner to return the verb
    ln=len(word)
    the_range=CorrectWord(word)
    if ln>2 and word[ln-3]=='i' and word[ln-2]=='n' and word[ln-1]=='g':
        for i in the_range:
            if word==verbs5[i]:
                return verbs1[i]
    if word[ln-1]=='s':
        for i in the_range:
           if word==verbs4[i]:
               return verbs1[i]
            

    else:
       for i in the_range:
            if word==verbs2[i]:
               return verbs1[i]
            elif word==verbs3[i]:
                return verbs1[i]
    return False


def smartBubbleSort(alist):
    n = len(alist)
    exchanges = True
    for passnum in range( n-1 , 0 , -1 ):
        if exchanges == False:
            break
        exchanges=False
        for i in range(passnum):
            if alist[i] > alist[i+1]:
                alist[i] , alist[i+1] = alist[i+1] , alist[i]
                exchanges = True

            
def Counter(alist):                     #Makes a list of lists of two elements, the word and number of it's clones
    CounterList=[]
    j,i=0,0
    length=len(alist)
    while(i<length):
        current=alist[i]
        CounterList.append([current,0])
        while(i<length and current==alist[i]):
            CounterList[j][1]+=1
            i+=1
        j+=1
    return CounterList


def get_Max(Max,Num,LastMax):
    if Num <= 0:                   #BASE CASE
        return
    value=[]
    for i in alist:
        if i[1]>=Max and i[1]<LastMax and (i[0] not in Common):
            if i[1]==Max and i[1]<LastMax:
                value.append(i[0])
            else:
                Max=i[1]
                value=[i[0]]
    LastMax=Max
    print(value,':',Max)
    Max=0
    get_Max(Max,Num-1,LastMax)


start_time = time.time()
Text_Cleaner(txt)
print('\nText_Cleaner:\t',"%s seconds" % (time.time() - start_time)) 
start_time = time.time()
smartBubbleSort(txt)
print('smartBubbleSort:\t',"%s seconds" % (time.time() - start_time)) 
start_time = time.time()
alist=Counter(txt)
print('Counter:\t',"%s seconds" % (time.time() - start_time)) 
start_time = time.time()

Max=0
print('\nTop Keywords:')
start_time = time.time()
get_Max(Max,Keywords,len(txt))
print('\nget_Max:\t',"%s seconds" % (time.time() - start_time))           
print('Total Time:\t',"%s seconds" % (time.time() - all_time))
