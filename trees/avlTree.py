from queue_ll import QueueLL


class AVLTree():
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right= None
        self.height= 1

def preOderTraversal(rootnode):
    if not rootnode:
        return
    else:
        print(" ",rootnode.data)
    # print("--")
    if rootnode.left is not None:
        print("/")
        preOderTraversal(rootnode.left)
    if rootnode.right is not None:
        print("\\")
        preOderTraversal(rootnode.right)

def inOrderTraversal(rootnode):
    if not rootnode:
        return
    preOderTraversal(rootnode.left)
    print(rootnode.data)
    preOderTraversal(rootnode.right)

def PostOrderTraversal(rootnode):
    if not rootnode:
        return
    preOderTraversal(rootnode.left)
    preOderTraversal(rootnode.right)
    print(rootnode.data)

def levelOrderTraversal(rootnode):
    if not rootnode:
        return
    else:
        q= QueueLL()
        q.enq(rootnode)
        c=0
        while not (q.isEmpty()):
            root= q.deQ()
            # print(c,root.value.data, root.value.left, root.value.right)
            if root.value.left is not None:
                q.enq(root.value.left)
            if root.value.right is not None:
                q.enq(root.value.right)
                c+= 1

def getHeight(root):
    if not root:
        return 0
    else:
        return root.height

def leftRotate(root):
    newroot= root.right
    root.right= root.right.left
    newroot.left= root
    root.height= 1+ max(getHeight(root.left), getHeight(root.right))
    newroot.height= 1+ max(getHeight(newroot.left), getHeight(newroot.right))

def rightRotate(root):
    newroot= root.left
    root.right= root.left.right
    newroot.right= root
    root.height= 1+ max(getHeight(root.left), getHeight(root.right))
    newroot.height= 1+ max(getHeight(newroot.left), getHeight(newroot.right))

def getBalance(root):
    if not root:
        return 0
    else:
        return getHeight(root.left) - getHeight(root.right)

def insertNode(root, value):
    if not root:
        return AVLTree(value)
    elif value <= root.data:
        root.left= insertNode(root.left, value)
    else:
        root.right= insertNode(root.right, value)
    root.height= 1+ max(getHeight(root.left), getHeight(root.right))
    balance= getBalance(root)
    if balance > 1 and value < root.left.data:
        return rightRotate(root)
    if balance > 1 and value > root.left.data:
        root.left= leftRotate(root.left)
        return rightRotate(root)
    if balance < -1 and value < root.right.data:
        root.right= rightRotate(root.right)
        return leftRotate(root)
    if balance < -1 and value > root.right.data:
        return leftRotate(root)
    return root

def getMinValue(rootNode):
    if rootNode is None and rootNode.left is None:
        return rootNode
    else:  getMinValue(rootNode.left)

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
            temp= getMinValue(rootNode.right)
            rootNode.data= temp.data
            rootNode.right= deleteNode(rootNode.right, temp.data)
        balance= getBalance(rootNode)
        if balance > 1 and getBalance(rootNode.left) >= 0:
            return rightRotate(rootNode)
        if balance > 1 and getBalance(rootNode.left) < 1:
            rootNode.left= leftRotate(rootNode.left)
            return rightRotate(rootNode)
        if balance < -1 and getBalance(rootNode.right) > 0:
            rootNode.right= rightRotate(rootNode.right)
            return leftRotate(rootNode)
        if balance < -1 and getBalance(rootNode.right) <= 0:
            return leftRotate(rootNode)

        return rootNode

newAVL= AVLTree(5)
newAVL= insertNode(newAVL, 10)
newAVL= insertNode(newAVL, 20)
newAVL= insertNode(newAVL, 30)
newAVL= insertNode(newAVL, 40)

levelOrderTraversal(newAVL)