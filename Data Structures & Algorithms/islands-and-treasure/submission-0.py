class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:
        #Create queue to store coordinates waiting ot be processed 
        queue = deque()

        #Scan every cell in the grid and add treasure cell to queue 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 0:
                    queue.append((row, col))
        
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]

        #Continue while coordinates remain in queue 
        while queue:
            #Remove coordinates at the front 
            row, col = queue.popleft()
            #Current cell distance 
            current_distance = grid[row][col]
            #Check that neighbour is inside grid and its value is INF
            for direction in directions:
                new_row = row + direction[0]
                new_col = col + direction[1]

                if (0 <= new_row < len(grid) and 0 <= new_col < len(grid[0]) and grid[new_row][new_col] == 2147483647):
                    #Set new distance of neighbor 
                    grid[new_row][new_col] = current_distance + 1 
                    #Add coordinates to the queue 
                    queue.append((new_row, new_col)) 