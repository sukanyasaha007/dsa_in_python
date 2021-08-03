
from random import randint
class Node():
    def __init__(self, value=None):
        self.value= value
        self.next= None
    def __str__(self):
        return str(self.value)

class QueueLL():
    def __init__(self,  values=None):
        self.head=None
        self.tail=None
        
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

    def enq(self, value):
        newNode= Node(value)
        if self.head == None:
            self.head, self.tail = newNode, newNode
        self.tail.next= newNode
        self.tail= newNode
        return

    def deQ(self):
        if self.isEmpty(): return "empty Q"
        else:
            head= self.head
            self.head= self.head.next
            return head

    def peek(self):
        if self.isEmpty(): "stack is empty"
        else: return self.head.value

    def delete(self):
        self.head= None
 
ll= QueueLL(10)
ll.enq(1)
ll.enq(2)
ll.enq(3)
ll.enq(4)
print(ll)
ll.deQ()
print("after deQing",ll)