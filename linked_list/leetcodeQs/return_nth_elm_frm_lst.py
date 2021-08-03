from LL import LinkedList

def return_nth_lst(ll, n):
    p1,p2= ll.head, ll.head
    if p1 is None:
        return None
    else:
        for i in range(n):
            p2= p2.next
        
        while p2:
            p2= p2.next
            p1= p1.next
        return p1

ll= LinkedList()
ll.generate(10, 100, 10)
print(ll)
print(return_nth_lst(ll, 7))