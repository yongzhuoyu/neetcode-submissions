class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        #Create memo that maps (i, current_sum) to the number of valid assignment
        memo = {}

        #Define dfs(i, current_sum) as the number of ways to assign signs to nums[i:] such that the final sum equals to target 
        def dfs(i, current_sum):
            #Check base case only when all the numbers has been processed 
            if i == len(nums):
                #Check if current_sum equals to target 
                if current_sum == target:
                    return 1
                return 0
            if (i, current_sum) in memo:
                return memo[(i, current_sum)]
            #Choice 1: Add the current number 
            add = dfs(i + 1, current_sum + nums[i])

            #Choice 2: Subtract the current number 
            subtract = dfs(i + 1, current_sum - nums[i])
            result = add + subtract 
            memo[(i, current_sum)] = result
            return result
        return dfs(0, 0)