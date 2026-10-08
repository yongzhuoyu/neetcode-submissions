class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        #Memo maps (row, col) to their number of unique paths 
        memo = {}
        def dfs(row, col):
            #Base case
            #When destination is reached 
            if row == m - 1 and col == n - 1:
                return 1 
            #When row/col goes out of bounds 
            if row >= m or col >= n:
                return 0
            if (row, col) in memo:
                return memo[(row, col)]
            #Explore moving right 
            moving_right = dfs(row, col + 1)
            #Explore moving down 
            moving_down = dfs(row + 1, col)
            #Sum all the possible paths from both moving_right and moving_down
            result = moving_right + moving_down 
            #Cache the result in the memo before returning 
            memo[(row, col)] = result
            return result
        return dfs(0,0)