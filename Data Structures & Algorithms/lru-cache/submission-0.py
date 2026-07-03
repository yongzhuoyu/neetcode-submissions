#Create custom doubly linked linked node 
class Node:
    def __init__(self, key=0, value=0):
        self.key = key 
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    #Create a helper insert function as most recent 
    def insert(self, node):
        #Locate the current node before right
        previous = self.right.prev
        #Connect previous and right to the newly inserted node
        previous.next = node
        node.prev = previous
        node.next = self.right
        self.right.prev = node 
    
    #Create a helper remove function from the least recent 
    def remove(self, node):
        #Locate neighbours of deleted node 
        nxt = node.next
        previous = node.prev
        #Connect nxt and previous 
        previous.next = nxt
        nxt.prev = previous

    def __init__(self, capacity: int):
        #Store the variables as instance attributes
        self.capacity = capacity 
        #Create an empty hash map 
        self.keyMap = {}
        #Create two dummy nodes: left and right 
        self.left = Node()
        self.right = Node()

        self.left.next = self.right 
        self.right.prev = self.left

    def get(self, key: int) -> int:
        if key not in self.keyMap:
            return -1
        
        node = self.keyMap[key]
        self.remove(node)
        self.insert(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        #Add key value-pair into hash map or update value 
        if key in self.keyMap:
            #Retrieve node from keyMap and update its value 
            node = self.keyMap[key]
            node.value = value 
            
            #Updating and repositioning the same node by removing it first, then inserting it
            self.remove(node)
            self.insert(node)
        else:
            #Create Node 
            node = Node(key, value)
            self.keyMap[key] = node
            #Insert it inside linked list 
            self.insert(node)
        #Check if new pair causes cache to exceed capacity 
        if len(self.keyMap) > self.capacity:
            #Retrieve the LRU node, remove node from linked list and remove LRU key from map
            lru = self.left.next 
            self.remove(lru)
            del self.keyMap[lru.key]

