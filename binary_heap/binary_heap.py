class Heap():
    def __init__(self, size):
        self.lst= (size+1) * [None]
        self.maxsize= size+1
        self.heapsize= 0

def peekofHeap(heap):
    if heap is None: return
    else:
        return heap.lst[1]
def sizeofHeap(heap):
    if not heap: return
    else: return heap.heapsize

def levelOrderTraversal(heap):
    if not heap: return
    else: 
        for i in range(1, heap.heapsize+1):
            print(heap.lst[i])

def heapyfing(heap, index, heapType):
    parentIndex= int(index//2)
    if parentIndex < 1: return
    else:
        if heapType == "Min":
            if heap.lst[parentIndex] > heap.lst[index]:
                temp = heap.lst[parentIndex]
                heap.lst[parentIndex] = heap.lst[index] 
                heap.lst[index]= temp
            heapyfing(heap, parentIndex, heapType)
        elif heapType == "Max":
            if heap.lst[parentIndex] < heap.lst[index]:
                temp = heap.lst[parentIndex]
                heap.lst[parentIndex] = heap.lst[index] 
                heap.lst[index]= temp
            heapyfing(heap, parentIndex, heapType)            

def heapInsert(heap, value, heapType):
    if heap.heapsize + 1 == heap.maxsize:
        print("heap is full")
    else:
        heap.lst[heap.heapsize + 1] = value
        heap.heapsize += 1
        heapyfing(heap, heap.heapsize, heapType)
        return "Value is added to heap"

newHeap = Heap(5)
heapInsert(newHeap, 5, "Min")
heapInsert(newHeap, 3, "Min")
heapInsert(newHeap, 6, "Min")
heapInsert(newHeap, 2, "Min")
levelOrderTraversal(newHeap)
print(newHeap.lst)