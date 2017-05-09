def Binary_Counter(alist):
    counterlist=[]
    last=-1                     #initialize first start last=-1  ,last+1 
    while(last+1<len(alist)):
        item=alist[last+1]                      #item to search for 
        first=last+1                            #the start position for item
        last=Search_Right(alist,first,item)     #the end position
        num=last-first+1                        #occurance of item
        counterlist.append([item,num])  
    return counterlist
    

def Search_Right(alist,first,item):
    #making a binary search
    low=first
    high=len(alist)
    mid=(high+low)//2
    while(high>=low and low<len(alist)):

        #if found item search again recursivley 
        if alist[mid]==item:
            if mid+1<len(alist) and item!=alist[mid+1]:
                return mid
            x=Search_Right(alist,mid+1,item)
            if x==-1:
                return mid
            return x
        if alist[mid] < item:
            low=mid+1
        if alist[mid]>item:
            high=mid-1
        mid=(high+low)//2

        
    return -1

###  testing  ###
if __name__=="__main__":
    alist=[1,1,1,1,3,3,4,5,5,5,5,6,6,6,6,7,7,7,7]
    #index[1,2,3,4,5,6,7,8,9,10]
    print(len(alist))
    counterlist=Binary_Counter(alist)
    print(counterlist)
