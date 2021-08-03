from LL import Node
from LL import LinkedList

def sum_ll(ll1, ll2):
    sum, carry= 0, 0
    p1, p2= ll1.head, ll2.head
    ll_new= LinkedList()
    while p1 or p2 or carry!=0:
        sum= carry
        if p1:
            sum+= p1.value
            p1= p1.next
        if p2:
            sum+= p2.value
            p2= p2.next
        carry= int(sum // 10)
        sum= sum % 10
        ll_new.add(sum)
    return ll_new

ll1= LinkedList()
ll1.generate(4, 9, 1)
print("ll1: ", ll1)
ll2= LinkedList()
ll2.generate(3, 9, 1)
print("ll2: ", ll2)
print("ll3: ", sum_ll(ll1, ll2))
