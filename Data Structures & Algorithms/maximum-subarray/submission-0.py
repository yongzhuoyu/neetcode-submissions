class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #current_sum is the maximum sum of any contiguous array ending at index i 
        current_sum = nums[0]
        #max_sum is the maximum subarray sum seen so far 
        max_sum = nums[0]

        for i in range(1, len(nums)):
            #Decide whether to:
            #1. Extend the previous subarray ending at the previous index 
            #2. Start a new subarray with the current element 
            current_sum = max(current_sum + nums[i], nums[i])
            #Update max_sum if current_sum is bigger 
            max_sum = max(current_sum, max_sum)
        return max_sum
        