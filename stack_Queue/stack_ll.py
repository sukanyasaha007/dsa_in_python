
from random import randint
class Node():
    def __init__(self, value=None):
        self.value= value
        self.next= None
    def __str__(self):
        return str(self.value)

class StackLL():
    def __init__(self, max_size, values=None):
        self.head=None
        self.tail=None
        self.max_size= max_size
    def __iter__(self):
        currNode= self.head
        while currNode:
            yield currNode
            currNode= currNode.next
    def __str__(self):
        values= [str(x.value) for x in self]
        return "\n____\n".join(values)
    def len_ll(self):
        len_ll=0
        currNode= self.head
        while currNode:
            len_ll+=1
            currNode= currNode.next
        return len_ll
    def generate(self, n, max_no, min_no):
        self.head= None
        self.tail= None
        for i in range(n):
            self.add(randint(min_no, max_no))
        return self
    def isEmpty(self):
        return self.head== None
    def isFull(self):
        return self.len_ll() == self.max_size
    def push(self, value):
        if self.isFull():
            return "stack is full"
        else:
            newNode= Node(value)
            newNode.next= self.head
            self.head= newNode
            return
    def pop(self):
        if self.isEmpty(): return "empty stack"
        else:
            self.head= self.head.next
            return
    def peek(self):
        if self.isEmpty(): "stack is empty"
        else: return self.head.value
    def delete(self):
        self.head= None
 
ll= StackLL(10)
ll.push(1)
ll.push(2)
ll.push(3)
ll.push(4)
print(ll)
ll.pop()
print("after pop",ll)