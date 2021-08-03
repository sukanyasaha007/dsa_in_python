from LL import LinkedList

def intersetion(ll1, ll2):
    if ll1.tail != ll2.tail:
        return "not intersected"
    else:
        len1= ll1.len_ll()
        len2= ll2.len_ll()
        # print("inside first else: ",ll1.len_ll(), len2)
        if len1 is not len2:
            if len1>len2: 
                shorter= ll2.head
                longer= ll1.head
                # print("inside if-if", shorter, longer)
            else: 
                shorter= ll1.head
                longer= ll2.head
            for _ in range(abs(len1-len2)):
                longer= longer.next
        else: shorter, longer= ll1.head, ll2.head
        while shorter and longer:
            if shorter is longer: return shorter
            else:
                shorter= shorter.next
                longer= longer.next
        return "not intersected"
def make_intersection(ll1, ll2, n):
    p= ll2.head
    for _ in range(n):
        p= p.next
    ll1.tail.next= p
    ll1.tail= ll2.tail

ll1, ll2= LinkedList(), LinkedList()
ll1.generate(4, 100, 0)
ll2.generate(8, 100, 0)
print(ll1, "\n", ll2)
make_intersection(ll1, ll2, 3)
print("after change\n",ll1, "\n", ll2)
print("after checking intersection", intersetion(ll1, ll2))
