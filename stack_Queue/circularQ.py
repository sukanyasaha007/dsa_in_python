class CircularQ():
    def __init__(self, max_size):
        self.lst= [None] * max_size
        self.max_size= max_size
        self.start, self.top= -1, -1

    def __str__(self):
        values= [str(x) for x in self.lst]
        return "\n____\n".join(values)

    def is_full(self):
        return (self.start==0 and self.top + 1 == self.max_size) or self.top+1 == self.start

    def is_empty(self):
        return self.top == -1

    def enQ(self, value):
        if self.is_full(): return "queue is full"
        else:
            if self.top+1 == self.max_size:
                self.top= 0
            else:
                self.top += 1
                if self.start == -1 :
                    self.start = 0
            self.lst[self.top] = value
            return "value is added"
    def deQ(self):
        if self.is_empty():
            return "the q is empty"
        else:
            start = self.start
            if self.top == self.start:
                self.top, self.start = -1, -1
            elif self.start + 1 == self.max_size:
                self.start= 0
            else:
                self.start+= 1
            self.lst[start] = None
            return "item removed"

    def peek(self):
        if self.is_empty(): return "empty q"
        else: return self.lst[self.start]

    def delete(self):
        self.lst= [None] * self.max_size
        self.start, self.top= -1, -1

q= CircularQ(5)
print(q.enQ(2))
print(q.enQ(3))
print(q.enQ(4))
# q.enQ(20)
# q.enQ(10)
# print(q)
print(q)
q.deQ()
# q.enQ(30)
# print(q.enQ(30))
# print(q.enQ(30))
# print(q.enQ(30))
# print("after actions")
print(q)