# Binary tree using python list
# will not use the index 0 in the list
# root is say x
# left child is 2x
# right child is then 2x+1

class BinaryTree():
    def __init__(self, size):
        self.lst= [None] * size
        self.maxSize= size
        self.lastIdx= 0
    def insert(self, value):
        if self.lastIdx + 1 == self.maxSize:
            return "tree is full"
        else:
            self.lst[self.lastIdx + 1] = value
            self.lastIdx+=1
            return "item added successfully"
    def searchBT(self, value):
        for i in range(len(self.lst)):
            if self.lst[i] == value:
                return "found at" + i
            else:
                return "not found"
    def preOrderTraversal(self, index):
        if index > self.lastIdx: return
        else:
            print(self.lst[index])
            self.preOrderTraversal(index * 2)
            self.preOrderTraversal(index * 2 + 1)
    def inOrderTraversal(self, index):
        if index > self.lastIdx: return
        else:
            self.preOrderTraversal(index * 2)
            print(self.lst[index])
            self.preOrderTraversal(index * 2 + 1)
    def postOrderTraversal(self, index):
        if index > self.lastIdx: return
        else:
            self.preOrderTraversal(index * 2)
            self.preOrderTraversal(index * 2 + 1)
            print(self.lst[index])
    def levelOrderTraversal(self, index):
        for i in range(index, self.lastIdx + 1): print(self.lst[i])
    def deleteNode(self, value):
        if self.lastIdx == 0: return "not found"
        else:
            for i in range(1, self.lastIdx + 1):
                if self.lst[i] == value:
                    self.lst[i] = self.lst[self.lastIdx]
                    self.lst[self.lastIdx] = None
                    self.lastIdx-= 1
                    return "successfully deleted"
    def deleteTree(self):
        self.lst = None
        return "tree is deleted"



bt= BinaryTree(10)
bt.insert("Drinks")
bt.insert("Hot")
bt.insert("Cold")
bt.insert("Tea")
bt.insert("Coffee")
bt.insert("Coke")
bt.insert("Ginger Ale")
print(bt.lst)
bt.deleteNode("Tea")
bt.levelOrderTraversal(1)
print(bt.lst)