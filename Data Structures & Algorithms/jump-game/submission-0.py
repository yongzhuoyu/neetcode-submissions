class Solution:
    def canJump(self, nums: List[int]) -> bool:
        #Initialise furthest to be the furthest index reachable using the index processed so far 
        furthest = 0
        for i in range(len(nums)):
            #If the current index is unreachable, return False 
            if furthest < i:
                return False

            #Update furthest using the furthest from the previous index and the furthest position from the current index
            furthest = max(furthest, i + nums[i])
            #If furthest reaches the last index, return 
            if furthest >= len(nums) - 1:
                return True 