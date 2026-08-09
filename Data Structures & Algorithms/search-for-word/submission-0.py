class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        #Track cells used by the current path 
        visited = set()

        #Helper would recieve row and column and  word_index its trying to match
        #Check if the current cell matches word[word_index]
        def dfs(row, col, word_index):
            #Check whether the row or column is outside board. If so, return False 
            if row >= len(board) or row < 0 or col >= len(board[0]) or col < 0:
                return False 
            #Check whether the current cell is already visited 
            if (row, col) in visited:
                return False
            #Compare the board ch with word[word_index]. If they are different, return False
            if board[row][col] != word[word_index]:
                return False 
            #If its the final character, return True 
            if word_index == len(word) - 1:
                return True
            #Add the current position to visited if cell passes all failture check 
            visited.add((row, col))
            #Call dfs on its neightbours using word_index + 1 and use found to store whether any of the four calls would return True 
            found = (dfs(row, col + 1, word_index+1) or
                dfs(row + 1, col, word_index+1) or
                dfs(row, col - 1, word_index+1) or
                dfs(row - 1, col, word_index+1))

            #Remove the choice by removing the current position from visited 
            visited.remove((row, col))
            #Return the stored result 
            return found

        #Try every board cell as a possible starting position 
        for row in range(len(board)):
            for col in range(len(board[0])):
                #If any starting position returns true, return True immediately 
                if dfs(row, col, 0):
                    return True
        #Return False if every starting position fails
        return False