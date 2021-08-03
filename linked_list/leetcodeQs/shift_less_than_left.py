from LL import LinkedList

def shift_less_thans(ll, n):
    p= ll.head
    ll.tail= ll.head
    while p:
        tempNode= p.next
        p.next= None
        if p.value< n:
            p.next= ll.head
            ll.head= p
        else:
            ll.tail.next= p
            ll.tail= p
        p= tempNode
    if ll.tail.next is not None:
        ll.tail.next= None
    # return ll

ll= LinkedList()
ll.generate(10, 99, 0)
print(ll)
shift_less_thans(ll, 30)
print(ll)