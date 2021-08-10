class TrieNode:
    def __init__(self):
        self.children= {}
        self.endOfString= False

class Trie:
    def __init__(self):
        self.root= TrieNode()

    def insertString(self, word):
        current= self.root
        for ch in word:
            node= current.children.get(ch)
            if node is None:
                node= TrieNode()
                current.children.update({ch:node})
            current = node
        current.endOfString = True
        print("added the word to the trie")

    def search(self, word):
        current= self.root
        for ch in word:
            node= current.children.get(ch)
            if node is None:
                return False
            current= node
        if current.endOfString:
            return True
        else: return False

def deleteString(root, word, index):
    ch= word[index]
    currentNode= root.children.get(ch)
    canThisBeDeleted= False

    #case 1: more than one children ie some other string is dependent on this
    if len(currentNode.children) > 1:
        deleteString(currentNode, word, index)
        return False

    if index == len(word) - 1:
    # case 2: the whole string matches with another children
        if len(currentNode.children) >= 1:
            currentNode.endOfString = False
            return False
    # case 3: delete the leaf or last character
        else:
            currentNode.children.pop(ch)
            return True
            
    # ???
    if currentNode.endOfString:
        deleteString(currentNode, word, index + 1)
        return False

    # case 4: does not impact any other string
    canThisBeDeleted = deleteString(currentNode, word, index + 1)
    if canThisBeDeleted:
        root.children.pop(ch)
        return True
    else: return False


newTrie = Trie()
newTrie.insertString("App")
newTrie.insertString("Appl")
deleteString(newTrie.root, "App", 0)
print(newTrie.search("Appl"))
print(newTrie.search("App"))
