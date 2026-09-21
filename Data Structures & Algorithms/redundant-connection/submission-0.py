class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)
        parent = []
        size = []

        for node in range(n + 1):
            #Every node initially represent its own component 
            parent.append(node)
            #Every component initally contains one node 
            size.append(1)
        
        def find(node):
            #A root is a node whose parent is itself
            if parent[node] != node:
                #Find the true root and connect this node directly to it 
                parent[node] = find(parent[node])       
            return parent[node]

        def union(node_a, node_b):
            #Find the root of each component 
            root_a = find(node_a)
            root_b = find(node_b)

            #The nodes are already connected if they have the same root 
            if root_a == root_b:
                return False
            
            #Make root_a represent the larger component 
            if size[root_a] < size[root_b]:
                root_a, root_b = root_b, root_a
            
            #Attach the smaller comonet beneath the larger one 
            parent[root_b] = root_a
            size[root_a] += size[root_b]

            return True

        #Process edges in the given order 
        for node_a, node_b in edges:
            #False would mean both endpoints are already connected
            if not union(node_a, node_b):
                return [node_a, node_b]
        return []