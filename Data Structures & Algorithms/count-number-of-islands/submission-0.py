class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        island_count = 0
        #Store visited land cell that belongs to an island that has been counted 
        visited = set()

        def dfs(row, col):
            #Stop dfs when base case is reached
            #if cell is out out of bounds(boundary checks must come first)
            if col >= len(grid[0]):
                return 
            if row >= len(grid):
                return 
            if col < 0:
                return
            if row < 0:
                return
            #if cell has been visited
            if (row,col) in visited:
                return
            #if cell is water 
            if grid[row][col] == "0":
                return

            #Add the current cell to visited  after confirming it is a valid land
            visited.add((row, col))

            #dfs in all 4 directions to find adjacent cells 
            dfs(row, col+1)
            dfs(row+1, col)
            dfs(row, col-1)
            dfs(row-1, col)

        #Iterate through each cell for a dfs starting point 
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #Check whether it is land and has not been visited 
                if grid[row][col] == "1" and (row, col) not in visited:
                    #increment island_count and run dfs 
                    island_count += 1 
                    dfs(row, col)

        return island_count