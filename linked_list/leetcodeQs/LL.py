from random import randint
class Node():
    def __init__(self, value=None):
        self.value= value
        self.next= None
        self.prev= None
    def __str__(self):
        return str(self.value)

class LinkedList():
    def __init__(self, values=None):
        self.head=None
        self.tail=None
    def __iter__(self):
        currNode= self.head
        while currNode:
            yield currNode
            currNode= currNode.next
    def __str__(self):
        values= [str(x.value) for x in self]
        return "->".join(values)
    def len_ll(self):
        len_ll=0
        currNode= self.head
        while currNode:
            len_ll+=1
            currNode= currNode.next
        return len_ll
    def add(self, value):
        newNode= Node(value)
        if self.head is None:
            self.head= newNode
            self.tail= newNode
        else:
            self.tail.next= newNode
            self.tail= self.tail.next
        return self.tail
    def generate(self, n, max_no, min_no):
        self.head= None
        self.tail= None
        for i in range(n):
            self.add(randint(min_no, max_no))
        return self
 