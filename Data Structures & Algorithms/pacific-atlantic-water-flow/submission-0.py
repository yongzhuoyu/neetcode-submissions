class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        rows = len(heights)
        cols = len(heights[0])

        pacific_queue = deque()
        atlantic_queue = deque()

        pacific_set = set()
        atlantic_set = set()

        for row in range(rows):
            for col in range(cols):
                        #Add Pacific border cells to the pacific queue and set
                if row == 0 or col == 0:
                    pacific_queue.append((row, col))
                    pacific_set.add((row, col))

                #Add Atlantic border cells to the atlantic queue and set
                if row == rows - 1 or col == cols - 1:
                    atlantic_queue.append((row, col))
                    atlantic_set.add((row, col))
        
        directions = [
            (0, 1),
            (1, 0),
            (0, -1),
            (-1 ,0)
        ]

        def bfs(queue, reachable):
            #Continue until every reachable cell has been processed 
            while queue:
                #Remove the current coordinate 
                row, col = queue.popleft()

                #Examine its four neighbours 
                for row_change, col_change in directions:
                    new_row = row + row_change 
                    new_col = col + col_change

                    is_inside_grid = (
                        0 <= new_row < rows and 
                        0 <= new_col < cols
                    )

                    #Skip an invalid neigbhour when:
                    #1. Outside grid 
                    #2. Already in reachable 
                    #3. Height is less than current height 
                    if not is_inside_grid:
                        continue
                    if (new_row, new_col) in reachable:
                        continue
                    if heights[new_row][new_col] < heights[row][col]:
                        continue
                    #Otherwise, add it to reachable and to the queue 
                    reachable.add((new_row, new_col))
                    queue.append((new_row, new_col))

        bfs(pacific_queue, pacific_set)
        bfs(atlantic_queue, atlantic_set)

        result = []
        #Return cells that are present and intersects in both sets
        for (row, col) in pacific_set:
            if (row, col) in atlantic_set:
                result.append([row, col])
        return result
