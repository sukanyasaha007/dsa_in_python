def capitalizeFirst(arr, targetArr=[]):
    
    if len(arr)<=1 : return targetArr + [str(arr[0]).title()]
    else: return capitalizeFirst((arr[1:]), targetArr + [arr[0].title()])

# print(capitalizeFirst(["cat", "rat", "bat"]))

#   Created by Elshad Karimov 
#   Copyright © AppMillers. All rights reserved.

# nestedEvenSum Solution
print(len([[1,2], [3,4, 5]]))