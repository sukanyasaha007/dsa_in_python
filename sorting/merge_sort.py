# https://www.youtube.com/watch?v=Nso25TkBsYI
def mergeSort(lst, first, last):
    if first<last:
        middle = (first+last)//2
        mergeSort(lst, first, middle)
        mergeSort(lst, middle+1, last)
        merge(lst, first,middle, last)
        return lst

def merge(lst, first, middle, last):
    L=lst[first:middle+1]
    R=lst[middle+1:last+1]
    L.append(99999999999)
    R.append(99999999999)
    i=j=0
    for k in range(first, last+1):
        if L[i]<=R[j]:
            lst[k]=L[i]
            i+=1
        else:
            lst[k]=R[j]
            j+=1
    
import random
lst= [20,1,40,10,35,15,8,3]
print(lst)
lst=mergeSort(lst, 0, len(lst)-1)
print(lst)
