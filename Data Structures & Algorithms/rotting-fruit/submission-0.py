class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        queue = deque()
        fresh_count = 0 

        #check every grid cell for rotten/fresh fruit 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                if grid[row][col] == 2:
                    queue.append((row,col))
                if grid[row][col] == 1:
                    fresh_count += 1
        directions = [
            (0,1),
            (1,0),
            (0,-1),
            (-1,0)
        ]
        minutes = 0
        #Stop once fresh fruit has rotted and no minutes pass when there are no fresh fruits  
        while fresh_count > 0 and queue:    
            #Record the number of fruits in the current layer 
            queue_size = len(queue)
            #Process exactly queue_size number of oranges 
            for i in range(queue_size):
                #Remove one fruit from queue 
                row, col = queue.popleft()
                #Check the 4 neighbouring cells 
                for row_change, col_change in directions:
                    new_row = row + row_change 
                    new_col = col + col_change

                    is_inside_grid = (
                        0 <= new_row < len(grid)
                        and 0 <= new_col < len(grid[0])
                    )

                    #Check if neighbour is inside grid and is fresh
                    if is_inside_grid and grid[new_row][new_col] == 1:
                        #Change it to rotten, decrement fesh_count and add it to queue
                        grid[new_row][new_col] = 2
                        fresh_count -= 1 
                        queue.append((new_row, new_col))

            #Increment minutes
            minutes += 1
        #If fresh fruites are unreachable, return -1
        if fresh_count > 0:
            return -1
        return minutes