def insertion_sort(lst):
    for i in range(1,len(lst)):
        key=lst[i]
        j=i-1
        while(j>=0 and lst[j]>key):
            lst[j+1]=lst[j]
            j-=1
        lst[j+1]=key
    return lst

lst= [2,10,4,6,5,3,1,20,15]
lst=insertion_sort(lst)
print(lst)

