class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        max_area = 0
        #Store all visited land cells that are part of an island 
        visited = set()

        def dfs(row, col):
            #Return 0 for invalid cells 
            #Check if the cell is out of bounds 
            if col >= len(grid[0]):
                return 0
            if row >= len(grid):
                return 0
            if col < 0:
                return 0
            if row < 0:
                return 0
            #Check if it has been visited
            if (row, col) in visited:
                return 0
            #Check if it is a water cell:
            if grid[row][col] == 0:
                return 0
            #If it is a valid cell, add it to visited
            visited.add((row, col))
            #Traverse to neighbouring branches and return their area 
            right_area = dfs(row, col+1)
            down_area = dfs(row+1, col)
            left_area = dfs(row, col-1)
            up_area = dfs(row-1, col)

            #Return the area of the current cell + all of its neighbouring branches 
            return 1 + right_area + down_area + left_area + up_area

        #Try every cell as a possible new island to find max_area
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                #Check if it is a land cell and has not been visited 
                if grid[row][col] == 1 and (row, col) not in visited:
                    #Start dfs from this cell to calculate the area of a complete island
                    current_area = dfs(row, col)
                    #compare current_area to the current max_area and keep the larger value
                    max_area = max(current_area, max_area)
        return max_area