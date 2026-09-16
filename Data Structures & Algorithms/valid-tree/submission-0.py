class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        #Check if the number of edges is n - 1
        if len(edges) != n - 1:
            return False

        #Build an adjacency list to store the list of neighbours for each node 
        adj_list = []
        for i in range(n):
            adj_list.append([])

        #For every undirected edge [a ,b], add b to a's neighbour and add a to b's neighbour
        for edge in edges:
            adj_list[edge[0]].append(edge[1])
            adj_list[edge[1]].append(edge[0])

        #Add node 0 to visited before enqueuing it. 
        visited = {0}
        queue = deque([0])

        while queue:
            current = queue.popleft()
            #Iterate through its neighbours 
            for neighbour in adj_list[current]:
                #If neighbor has been visited, skip it 
                if neighbour in visited:
                    continue 
                #If not, mark it as visited and add it to queue
                visited.add(neighbour)
                queue.append(neighbour)
        #Return whether the number of visited nodes equals to n 
        return len(visited) == n
