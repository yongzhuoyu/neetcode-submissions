class TrieNode:
    def __init__(self):
        #children map characters to TrieNode
        self.children = {}
        #is_end_of_word checks whether a full word ends here 
        self.is_end_of_word = False

class PrefixTree:

    def __init__(self):
        #Initialise root to be the starting point and it should not represent a ch 
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        #Start at root 
        current = self.root
        for ch in word:
            #check if there is no child path for this character yet 
            if ch not in current.children:
                current.children[ch] = TrieNode()
            #Move the current pointer to child 
            current = current.children[ch]
        #Mark the last character as the end of word aft processing all ch 
        current.is_end_of_word = True

    def search(self, word: str) -> bool:
        current = self.root
        for ch in word:
            #Check every character path exists from root 
            if ch not in current.children:
                return False 
            current = current.children[ch]
        #Check if the final node is marked as end_of_word 
        return current.is_end_of_word

    def startsWith(self, prefix: str) -> bool:
        current = self.root
        #Check whether every character path exist 
        for ch in prefix:
            if ch not in current.children:
                return False
            current = current.children[ch]
        return True
        