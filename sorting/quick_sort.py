def quick_Sort(lst, low, high):
    if low<high:
        border= quick_sort_helper(lst, low, high)
        quick_sort_helper(lst, low, border-1)
        quick_sort_helper(lst, border+1, high)
    return lst



def find_median(lst, low, high):
    middle= (low+high)//2
    median_index=low
    if lst[low]<lst[middle]:
        if lst[middle]<lst[high]:
            median_index=middle
        elif lst[high]< lst[low]:
            median_index= low
        else:
            median_index=high
    return median_index

def quick_sort_helper(lst, low, high):
    median_index= find_median(lst, low, high)
    lst[low], lst[median_index]= lst[median_index], lst[low]
    border=low
    for i in range(low, high+1):
        if lst[i]<lst[median_index]:
            border+=1
            lst[i], lst[border]= lst[border], lst[i]
        lst[low], lst[border]= lst[border], lst[low]
    return border


lst=[2,4,3,6,9,8,1]
print(quick_Sort(lst, 0, len(lst)-1))
        



    