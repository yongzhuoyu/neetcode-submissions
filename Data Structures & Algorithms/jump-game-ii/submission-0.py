class Solution:
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        current_end = 0
        furthest = 0

        for i in range(len(nums) - 1):
            #Update the furthest index reachable from the current position
            furthest = max(furthest, i + nums[i])

            #Check if we have reached the end of the current range 
            if i == current_end:
                jumps += 1
                current_end = furthest 
        return jumps