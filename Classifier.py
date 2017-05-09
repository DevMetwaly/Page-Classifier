##############################################################################
##################################          ##################################
############################   PAGES CLASSIFIER   ############################
##################################          ##################################
##############################################################################

#myfile=input("Please insert the file name. (ex: mytext.txt)\n .../")
myfile="TestPage1"
verbs1=open('verbs1.txt','r').read().split('\n')        #Original Verbs (The Base)
verbs2=open('verbs2.txt','r').read().split('\n')        #Verb Past
verbs3=open('verbs3.txt','r').read().split('\n')        #Verb Past Participle
verbs4=open('verbs4.txt','r').read().split('\n')        #Verb +[es/s]
verbs5=open('verbs5.txt','r').read().split('\n')        #Verb +[ing]
txt=open(myfile+'.txt','r').read().lower().split()      #read the page
Common=open("CommonWords.txt",'r').read().split(',')    #common english words
print('\nWords found: ',len(txt))
#Keywords=int(input('\nShow (n) of top keywords. Insert (n): '))
Keywords=10
from BinaryCounter import Binary_Counter
from Mapping import CorrectWord                         #The verbs database
import time
all_time = time.time()
start_time = time.time()

#############################################################################################
##############function to:                                                ###################
##############clean the words from special chars , 's , s' , ing etc..... ###################
##############                                                            ###################
#############################################################################################
def Text_Cleaner(txt):                                                                      #                 
    length=len(txt)                                                                         #
    i=0                                                                                     #
    #check every word in the Page                                                           #
    while(i<length):                                                                        #
        WordLength=len(txt[i])                                                              #
    #check if the word in from "word's"                                                     #
        if WordLength>2 and txt[i][-1]=='s' and (txt[i][-2]=="'" or txt[i][-2]=='’'):       #
            txt[i]=txt[i][:-2]                                                              #
    #check if the word in from "words'"                                                     #
        elif WordLength>2 and (txt[i][-1]=="'" or txt[i][-1]=='’') and txt[i][-2]=="s":     #
            txt[i]=txt[i][:-2]                                                              #
    #remove the word if it doesn't start with a letter character                            #
        elif ord(txt[i][0]) not in range(97,123):                                           #
            txt[i]=' '      #actualy it doesn't remove words - it assign it with spaces     #
                            #the deleting is decreasing the performance                     #
    #words in case like Hey! ---- become ----> Hey                                          #
        elif  ord(txt[i][-1]) not in range(97,123):                                         #
            txt[i]=txt[i][:-1]      #remove last character if it's not a letter             #
                                                                                            #
        base_form=get_base_form(txt[i])         #Searches for the original verb             #
        if base_form :              #if get_base_form found a verb and didn't return False  #
            txt[i]=base_form        #assign the index to the new word => base form          #
        i+=1                                                                                #
#############################################################################################
def get_base_form(word):                #Used in Text_Cleaner to return the verb            #
    ln=len(word)                                                                            #
    the_range=CorrectWord(word)         #Gets the range of words to search within           #
    # verb+ing                                                                              #
    if ln>2 and word[ln-3]=='i' and word[ln-2]=='n' and word[ln-1]=='g':                    #
        for i in the_range:                                                                 #
            if word==verbs5[i]:                                                             #
                return verbs1[i]                                                            #
    #verb+s (or es)                                                                         #
    if word[ln-1]=='s':                                                                     #
        for i in the_range:                                                                 #
           if word==verbs4[i]:                                                              #
               return verbs1[i]                                                             #
                                                                                            #
    #checking if verb is in a past form                                                     #
    else:                                                                                   #
       for i in the_range:                                                                  #
            if word==verbs2[i]:                                                             #
               return verbs1[i]                                                             #
            elif word==verbs3[i]:                                                           #
                return verbs1[i]                                                            #
    return False                                                                            #
#############################################################################################

def mergeSort(alist):
    if len(alist)>1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        mergeSort(lefthalf)
        mergeSort(righthalf)
        i=0
        j=0
        k=0
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k]=lefthalf[i]
                i=i+1
            else:
                alist[k]=righthalf[j]
                j=j+1
            k=k+1
        while i < len(lefthalf):
            alist[k]=lefthalf[i]
            i=i+1
            k=k+1
        while j < len(righthalf):
            alist[k]=righthalf[j]
            j=j+1
            k=k+1


            
################################################################################
############## function to:                                 ####################
############## make alist of lists - every list contain     ####################
############## the word and it's occurance                  ####################
############## working lineary - Big O(n)                   ####################
############## improved lately to - Big O(logn)             ####################
############## in a function named Binary_Counter           ####################
##############                                              ####################
#############################################################################################################################            
def Counter(alist):  #Makes a list of lists of two elements, the word and number of it's clones - working lineary Big O(n)  #
    CounterList=[]          #New empty list                                                                                 #
    j,i=0,0                                                                                                                 #
    length=len(alist)                                                                                                       #
    current=alist[i]                                                                                                        #
    CounterList.append([current,0])                                                                                         #
    while(i<length):                                                                                                        #
        if(alist[i] != current):                                                                                            #
            j+=1                                                                                                            #
            current=alist[i]                                                                                                #
            CounterList.append([current,0])                                                                                 #
        CounterList[j][1]+=1                                                                                                #
        i+=1                                                                                                                #
    return CounterList                                                                                                      #
#############################################################################################################################



################################################################################
############## function to:                                 ####################
############## return top key words "working recursively"   ####################
##############                                              ####################
#############################################################################################################################
def get_Max(Num,LastMax):                                                                                                   #
    if Num <= 0:            #BASE CASE _ Num of keywords to print? If already all printed, Num=0                            #
        return                                                                                                              #
    value=[]                                                                                                                #
    Max=0                                                                                                                   #
    for i in alist:         #We will assign the Counted List (return of Counter) to list called alist                       #
        if i[1]>=Max and i[1]<LastMax and (i[0] not in Common):     #[[ 'word' , i ]] => i found a higher Max value?        #
            if i[1]==Max and i[1]<LastMax:                                                                                  #                          
                value.append(i[0])                                                                                          #
            else:                                                                                                           #                  
                Max=i[1]                                                                                                    #
                value=[i[0]]                                                                                                #
    LastMax=Max                                                                                                             #
    print(value,':',Max)                                                                                                    #
    get_Max(Num-1,LastMax)                                                                                                  #
#############################################################################################################################


start_time = time.time()
Text_Cleaner(txt)   #clean text
print('\nText_Cleaner:\t',"%s seconds" % (time.time() - start_time))
    
start_time = time.time()
mergeSort(txt)
print('mergeSorter:\t',"%s seconds" % (time.time() - start_time))

###################################################################
##########                                             ############
##########other implementation for the function Counter############
########## using binary searching                      ############
########## Big O(logn)                                 ############
########## uncomment to test the function              ############
##########                                             ############
###################################################################
#start_time = time.time()
#alist=Binary_Counter(txt)  #counting occurance big O(logn)
#print('binary Counter:\t',"%s seconds" % (time.time() - start_time))

start_time = time.time()
alist=Counter(txt)          #counting occurance big 0(n)
print('linear Counter:\t',"%s seconds" % (time.time() - start_time))



print('\nTop Keywords:')

start_time = time.time()
get_Max(Keywords,len(txt)) #print top keywords
print('\nget_Max:\t',"%s seconds" % (time.time() - start_time))

print('Total Time:\t',"%s seconds" % (time.time() - all_time))
