from queue_ll import QueueLL
class NodeBST():
    def __init__(self, data=None):
        self.data= data
        self.left= None
        self.right= None

# class BST():
#     def __init__(self, root):
#         self.rootNode= NodeBST(root)
def insert(rootNode, value):
    newNode= NodeBST(value)
    if rootNode.data is None:
        rootNode.data= value
    elif value <= rootNode.data:
        if rootNode.left is None:
            rootNode.left= newNode
        else:
            insert(rootNode.left, value)
    else:
        if rootNode.right is None:
            rootNode.right= newNode
        else:
            insert(rootNode.right, value)
    return "insert is successful"

def preOrderTraversal(root):
    if not root:
        return
    print(root.data)
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)

def inOrderTraversal(root):
    if not root:
        return
    preOrderTraversal(root.left)
    print(root.data)
    preOrderTraversal(root.right)

def PostOrderTraversal(root):
    if not root:
        return
    preOrderTraversal(root.left)
    preOrderTraversal(root.right)
    print(root.data)

def levelOrderTraversal(root):
    if not root:
        return
    else:
        q = QueueLL()
        q.enq(root)
        while not q.isEmpty():
            r= q.deQ()
            print(r.value.data)
            if r.value.left:
                q.enq(r.value.left)
            if r.value.right:
                q.enq(r.value.right)

def searchNode(root, value):
    if root.data == value:
        return "found"
    else:
        if value<= root.left.data:
            if root.left.data == value:
                return "found"
            else:
                searchNode(root.left, value)
        else:
            if root.right.data == value:
                return "found"
            else:
                searchNode(root.right, value)
        return "not found"

def findMinValue(rootNode):
    if rootNode is None:
        return rootNode
    else:
        while rootNode.left:
            rootNode= rootNode.left
        return rootNode

def deleteNode(rootNode, value):
    if not rootNode:
        return rootNode
    else:
        if value < rootNode.data:
            rootNode.left = deleteNode(rootNode.left, value)
        elif value > rootNode.data:
            rootNode.right= deleteNode(rootNode.right, value)
        else:
            if rootNode.left is None:
                temp= rootNode.right
                rootNode= None
                return temp
            if rootNode.right is None:
                temp= rootNode.left
                rootNode= None
                return temp
            # find success to root node here to replace rootnode. 
            # it should the minimum value in the right subtree
            temp= findMinValue(rootNode.right)
            rootNode.data= temp.data
            rootNode.right= deleteNode(rootNode.right, temp.data)
        return rootNode

root= NodeBST(50)
# print(root.data)
insert(root, 20)
insert(root, 30)
insert(root, 40)
insert(root, 80)
insert(root, 70)
insert(root, 100)
# print(root.left.data)
preOrderTraversal(root)
# levelOrderTraversal(root)
deleteNode(root, 70)
preOrderTraversal(root)

            
print(searchNode(root, 80))

