class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        #Store all the complete subsets 
        result = []
        #Store the current subsets that are being built 
        path = []

        #Create a helper to decide what to do at each nums[index] 
        def backtrack(index):
            #Base case: adding a copy of path to the result 
            if index == len(nums):
                result.append(path.copy())
                return
            #Branch 1: Exclude the current number by moving to the next index 
            backtrack(index + 1)

            #Branch 2: Include the current number by adding it to path, and moving to the next index 
            path.append(nums[index])
            backtrack(index+1)
            #Backtracking by undoing the included choice
            path.pop()
        #Start from the index 0 of nums
        backtrack(0)
        return result