class Stack():
    def __init__(self, max_size):
        self.lst= list()
        self.max_size= max_size

    def __str__(self):
        # values= self.lst.reverse()
        values= list(map(str, self.lst))
        return "\n____\n".join(values)
    def is_full(self):
        # print(self.lst, self.max_size)
        return len(self.lst)== int(self.max_size)
    def is_empty(self):
        if self.lst==[]: 
            return True
        else: 
            return False
    def popS(self):
        if self.is_empty():
            return "Empty Stack"
        else:
            return self.lst.pop(0)
    def pushS(self, value):
        if self.is_full(): 
            return "Stack Full"
        else: 
            self.lst= [value] + self.lst
            return
    def peek(self):
        if self.lst is []: return "empty list found"
        return self.lst[-1:]

stck= Stack(5)
stck.pushS(2)
stck.pushS(3)
stck.pushS(5)
stck.pushS(20)
stck.pushS(10)
print(stck)
stck.popS()
print("after poping:")
stck.pushS(30)
print(stck.pushS(30))
print(stck.pushS(30))
print(stck.pushS(30))
print(stck)