class Trie:
    #Implement Trie to store its children and is_end_of_word
    def __init__(self):
        self.children = {}
        self.is_end_of_word = False

class WordDictionary:
    #Create a root node when WordDictionary is instantiated
    def __init__(self):
        self.root = Trie()

    def addWord(self, word: str) -> None:
        #Set current pointer to root 
        current = self.root
        #Check if ch in word exist, if not create a Trie node for that character 
        for ch in word:
            if ch not in current.children:
                current.children[ch] = Trie()
            #Set the current pointer to child node 
            current = current.children[ch]
        #Mark the last node of the word 
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        #Check whether word[index:] can matched starting from this node 
        def helper(index, node):
            #Base case is when we have matched all character and reached the last node 
            if index == len(word):
                #At the last node, we will check if its the last character of a word
                return node.is_end_of_word
            ch = word[index]
            if ch != ".":
                if ch not in node.children:
                    return False
                #for a normal character, recurse down one exact child
                return helper(index+1, node.children[ch])
            #If the ch is a willdcard,try every child of the current node 
            if ch == ".":
                for child in node.children.values():
                    #check if a path exist from the child node 
                    if helper(index+1, child):
                        return True
                #After all the children fails, return False 
                return False
        return helper(0, self.root)
