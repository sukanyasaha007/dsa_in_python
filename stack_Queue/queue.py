class Queue():
    def __init__(self, max_size):
        self.lst= list()
        self.max_size= max_size

    def __str__(self):
        values= list(map(str, self.lst))
        return "\n____\n".join(values)

    def is_full(self):
        return len(self.lst)== int(self.max_size)

    def is_empty(self):
        return self.lst==[]

    def dequeue(self): #------------------------------------time complexity O(n)--------------------------------------
        if self.is_empty():
            return "Empty Q"
        else:
            return self.lst.pop(0)

    def enqueue(self, value):#------------------------------------time complexity O(n)--------------------------------------
        if self.is_full(): 
            return "Q Full"
        else: 
            self.lst= self.lst + [value]
            return

    def peek(self):
        if self.lst is []: return "empty list found"
        return self.lst[0]

q= Queue(5)
q.enqueue(2)
q.enqueue(3)
q.enqueue(5)
q.enqueue(20)
q.enqueue(10)
print(q)
q.dequeue()
q.enqueue(30)
print(q.enqueue(30))
print(q.enqueue(30))
print(q.enqueue(30))
print("after actions")
print(q)