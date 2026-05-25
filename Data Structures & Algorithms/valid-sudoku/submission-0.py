from math import sqrt
class Solution:

    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #check every row for duplicates 
        for row in range(len(board)):
            #store seen values in a hash set 
            seen = set()
            for col in range(len(board)):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False 
                seen.add(value)

        #check every column for duplicates 
        for col in range(len(board)):
            #store seen values in a hash set 
            seen = set()
            for row in range(len(board)):
                value = board[row][col]
                if value == ".":
                    continue
                if value in seen:
                    return False 
                seen.add(value)

        #check each sub-boxes for duplicates
        box_size = int(sqrt(len(board)))

        #look for the top left corners
        for box_row in range(0, len(board), box_size):
            for box_col in range(0, len(board), box_size):

                #Store seen values in each sub box 
                seen = set()

                #Scanning each sub box 
                for r in range(box_row, box_row+box_size):
                    for c in range(box_col, box_col+box_size):
                        value = board[r][c]
                        if value == ".":
                            continue
                        if value in seen:
                            return False 
                        seen.add(value)
        return True
                        