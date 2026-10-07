class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        #Create memo that maps (i, prev_index) to the max length of subsequence starting from i 
        memo = {}

        #Define dfs(i, prev_index) as the max length of a subsequence we can build from index i 
        def dfs(i, prev_index):
            #Base Case: when i reaches end of nums, return 0 as no more elements can be selected 
            if i == len(nums):
                return 0
            if (i, prev_index) in memo:
                return memo[(i, prev_index)]
            #At each index, choose whether to take or skip nums[i]
            #Skip current number
            skip = dfs(i + 1, prev_index)
            result = 0
            #Condition for taking: if there is no previous element or current number is greater than number at previous index 
            take = 0
            if prev_index == -1 or nums[i] > nums[prev_index]:
                #Take the current number 
                take = 1 + dfs(i + 1, i)
            
            #Choose the max length between skip or take 
            result = max(skip, take)
            #Cache the result in memo 
            memo[(i, prev_index)] = result
            return result
        
        return dfs(0, -1)