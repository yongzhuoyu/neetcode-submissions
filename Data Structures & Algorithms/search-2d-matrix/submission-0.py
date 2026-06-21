class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        #Treat the matrix as a flattened sorted array and assign a virtual index to each number 
        #Use binary search over the indexes
        #Convert each virtual index back to matrix coordinates

        rows = len(matrix)
        cols = len(matrix[0])
        left = 0 
        right = rows * cols - 1 

        while left <= right:
            mid = (right + left) // 2 
            row = mid // cols
            col = mid % cols

            value = matrix[row][col]
            if value == target:
                return True 
            elif value < target:
                left = mid + 1 
            else:
                right = mid - 1
        return False