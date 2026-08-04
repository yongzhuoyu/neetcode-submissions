class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        #Sort numbers first to group equal values together 
        nums.sort()
        path = []
        result = []

        def backtrack(start):
            #Save every path as every path is a valid subset 
            result.append(path.copy())

            for i in range(start, len(nums)):
                #Skip duplicate sibilings 
                if i > start and nums[i] == nums[i-1]:
                    continue 
                #Choose this number and add it into path
                path.append(nums[i])
                #Dfs down to the next subset 
                backtrack(i + 1)
                #Remove num[i] from path when child function returns
                path.pop()
        backtrack(0)
        return result
                
                