class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        #Calculate the total sum of nums 
        total = sum(nums)

        #If the total is odd, than equal partioning would be impossible so return false 
        if total % 2 != 0:
            return False

        #Calculate the target as the half of total sum 
        target = total / 2 
        
        #Define dfs(i, current_sum) to determine whether the remaining numbers can bring current_sum to target 
        def dfs(i, current_sum):
            #Base case 
            if current_sum == target:
                return True
            if current_sum > target:
                return False
            if i == len(nums):
                return False
            #Take nums[i]
            take = dfs(i + 1, current_sum + nums[i])
            #If the take branch is true, return true as there is no need to check the skip branch 
            if take:
                return True
            #Skip nums[i]
            skip = dfs(i + 1, current_sum)
            return skip 
        return dfs(0, 0)
