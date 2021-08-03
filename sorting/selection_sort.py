# https://www.youtube.com/watch?v=mI3KgJy_d7Y&t=0s

def selection_sort(lst):
    min_val, j= 0, 0
    for i in range(0, len(lst)-1):
        min_val= i
        # j=i+1
        for j in range(i+1, len(lst)-1):
            # print(j,lst[j])
            if lst[j]<lst[min_val]:
                # print(j,lst[j])
                min_val= j
            # j+=1
        lst[i], lst[min_val]= lst[min_val], lst[i]
    return lst

lst= [2,5,1,7,4,3,8,6]
print(lst)
lst= selection_sort(lst)
print(lst)