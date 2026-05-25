from math import sqrt
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # #check every row for duplicates 
        # for row in range(len(board)):
        #     #store seen values in a hash set 
        #     seen = set()
        #     for col in range(len(board)):
        #         value = board[row][col]
        #         if value == ".":
        #             continue
        #         if value in seen:
        #             return False 
        #         seen.add(value)

        # #check every column for duplicates 
        # for col in range(len(board)):
        #     #store seen values in a hash set 
        #     seen = set()
        #     for row in range(len(board)):
        #         value = board[row][col]
        #         if value == ".":
        #             continue
        #         if value in seen:
        #             return False 
        #         seen.add(value)

        # #check each sub-boxes for duplicates
        # box_size = int(sqrt(len(board)))

        # #look for the top left corners
        # for box_row in range(0, len(board), box_size):
        #     for box_col in range(0, len(board), box_size):

        #         #Store seen values in each sub box 
        #         seen = set()

        #         #Scanning each sub box 
        #         for r in range(box_row, box_row+box_size):
        #             for c in range(box_col, box_col+box_size):
        #                 value = board[r][c]
        #                 if value == ".":
        #                     continue
        #                 if value in seen:
        #                     return False 
        #                 seen.add(value)
        # return True
        
        #Initialise the 3 structures: row, column and boxes
        row = []
        col = []
        boxes = []

        #Populate them 9 sets in each structure to store unique values 
        for i in range(9):
            row.append(set())
            col.append(set())
            boxes.append(set())

        #Iterate through every cell, starting from the top left 
        for r in range(9):
            for c in range(9):
                value = board[r][c]

                #Check if the current value is "."
                if value == ".":
                    continue

                #Calculate box index based on position of cell 
                box_index = ((r // 3) * 3) + (c // 3)

                #Check if value is in row  
                if value in row[r]:
                    return False

                #Check if value is in column
                if value in col[c]:
                    return False 
                
                #Check if value is in box using box index
                if value in boxes[box_index]:
                    return False

                #Add all unseen values into the hash set
                row[r].add(value)
                col[c].add(value)
                boxes[box_index].add(value)
        return True

                        