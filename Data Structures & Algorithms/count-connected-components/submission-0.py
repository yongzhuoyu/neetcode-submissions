class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        #To store the list of neighbors for each node 
        adj_list = []

        for node in range(n):
            adj_list.append([])

        #Store every undirected edge for both nodes 
        for node_a, node_b in edges:
            adj_list[node_a].append(node_b)
            adj_list[node_b].append(node_a)

        visited = set()
        num_connected = 0
        #Iterate through every node
        for node in range(n):
            #If the current node has been visited, skip it 
            if node in visited:
                continue

            num_connected += 1
            #Create a new queue for each component and add the current node to the queue 
            queue = deque()
            queue.append(node)
            visited.add(node)
            while queue:
                current = queue.popleft()
                for neighbour in adj_list[current]:
                    if neighbour in visited:
                        continue 
                    visited.add(neighbour)
                    queue.append(neighbour)
        return num_connected