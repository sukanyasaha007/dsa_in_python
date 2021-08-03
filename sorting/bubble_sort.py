# https://www.youtube.com/watch?v=YHm_4bVOe1s
def bubble_sort(lst):
    for i in range(0, len(lst)-1):
        for j in range(0, len(lst)-1 - i):
            if lst[j]>lst[j+1]:
                lst[j], lst[j+1] = lst[j+1], lst[j]
    return lst


lst= [2,4,6,4,8,1]
print(bubble_sort(lst))