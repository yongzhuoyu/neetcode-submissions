class Solution:
    def solve(self, board: List[List[str]]) -> None:
        rows = len(board)
        cols = len(board[0])
        queue = deque()

        #Find all intial safe cells at the edge of the board
        for row in range(rows):
            for col in range(cols):
                is_border = (
                    row == 0 or col == 0 or row == rows - 1 
                    or col == cols - 1
                ) 
                if is_border and board[row][col] == "O":
                    board[row][col] = "T"
                    #Add its coordinates to the queue 
                    queue.append((row, col))

        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
        #Find all cells connected to the safe region using BFS
        def bfs(queue): 
            while queue:
                row, col = queue.popleft()
                
                #Check its four neighbours
                for row_change, col_change in directions:
                    new_row = row + row_change
                    new_col = col + col_change 

                    #Check neighbour is out of bounds 
                    is_inside_board = (
                        0 <= new_row < rows and
                        0 <= new_col < cols
                    )

                    if not is_inside_board:
                        continue
                    if board[new_row][new_col] != "O":
                        continue
                    
                    #Change the neighbour to "T" and update queue
                    board[new_row][new_col] = "T"
                    queue.append((new_row, new_col))

        bfs(queue)
        #Update the board 
        for row in range(rows):
            for col in range(cols):
                #Surround "O" cells by changing them to "X"
                if board[row][col] == "O":
                    board[row][col] = "X"
                #Change "T" cells back to O
                if board[row][col] == "T":
                    board[row][col] = "O"
                