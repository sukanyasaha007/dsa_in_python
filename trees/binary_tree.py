from queue_ll import QueueLL


class TreeNode():
    def __init__(self, data):
        self.data = data
        self.left= None
        self.right= None

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

def searchBT(rootnode, nodevalue):
    if not rootnode:
        return
    else:
        q= QueueLL()
        q.enq(rootnode)
        level=0
        while not (q.isEmpty()):
            root= q.deQ()
            if root.value.data == nodevalue:
                return "found " + nodevalue + " at node " + str(level)
            else:
                if root.value.left is not None:
                    q.enq(root.value.left)
                if root.value.right is not None:
                    q.enq(root.value.right)
                level+= 1
        return "not found"
def insertBT(rootnode, value):
    newNode= TreeNode(value)
    if not rootnode:
        rootnode.data= newNode
        return value + " Inserted successfully"
    else:
        q= QueueLL()
        q.enq(rootnode)
        while not q.isEmpty():
            root= q.deQ()
            if not root.value.left:
                root.value.left= newNode
                return value + " Inserted successfully"
            else:
                q.enq(root.value.left)
            if not root.value.right:
                root.value.right= newNode
                return value + " Inserted successfully"
            else:
                q.enq(root.value.right)
def getDeepestNode(rootNode):
    if not rootNode:
        return
    else:
        q= QueueLL()
        q.enq(rootNode)
        while not(q.isEmpty()):
            root = q.deQ()
            if (root.value.left is not None):
                q.enq(root.value.left)
            
            if (root.value.right is not None):
                q.enq(root.value.right)
        deepestNode = root.value
        return deepestNode

def deleteDeepestNode(rootNode, node_delte):
    if not rootNode:
        return
    else:
        q= QueueLL()
        q.enq(rootNode)
        while not(q.isEmpty()):
            root = q.deQ()
            if root.value.data is node_delte:
                root.value = None
                return
            if root.value.right:
                if root.value.right is node_delte:
                    root.value.right = None
                    return
                else:
                    q.enq(root.value.right)
            if root.value.left:
                if root.value.left is node_delte:
                    root.value.left = None
                    return
                else:
                    q.enq(root.value.left)
def deleteNode(rootnode, value):
    if not rootnode:
        return
    else:
        q= QueueLL()
        q.enq(rootnode)
        while not q.isEmpty():
            root= q.deQ()
            if root.value.data == value:
                temp= getDeepestNode(rootnode)
                root.value.data= temp.data
                deleteDeepestNode(rootnode, temp)
                return
            if root.value.left:
                q.enq(root.value.left)
            if root.value.right:
                q.enq(root.value.right)
        return "not found"
def deleteBT(rootNode):
    rootNode.data = None
    rootNode.left = None
    rootNode.right = None
    return "The BT has been successfully deleted" 

root= TreeNode("biriyani")
root.left= TreeNode("hiderabadi")
root.right= TreeNode("Lakhnau")
# preOderTraversal(root)
# print()
# inOrderTraversal(root)s 
# print()
# PostOrderTraversal(root)
# levelOrderTraversal(root)
# print(searchBT(root, "Lakhnau"))
print(insertBT(root, "spicy"))
print(insertBT(root, "non-spicy"))
print(insertBT(root, "colorful"))
print(insertBT(root, "whitish"))

# preOderTraversal(root)
# levelOrderTraversal(root)
deleteNode(root, "spicy")
preOderTraversal(root)

