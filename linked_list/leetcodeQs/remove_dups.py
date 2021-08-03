import LL

ll= LL.LinkedList()

def remove_duplicates(ll):
    if ll is None:
        return "emplty ll"
    else:
        currNode= ll.head
        values= set([currNode.value])
        while currNode.next:
            if currNode.next.value in values:
                currNode.next= currNode.next.next
            else:
                values.add(currNode.next.value)
                currNode= currNode.next
        return ll

ll.generate(10, 100, 10)
print(ll)
remove_duplicates(ll)
print(ll)