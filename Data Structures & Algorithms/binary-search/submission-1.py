class Solution:
    def search(self, nums: List[int], target: int) -> int:
        #create the left, right and middle index 
        left = 0
        right = len(nums) - 1
        middle = 0
        
        while left <= right:
            #calculate the middle index 
            middle = (right + left) // 2

            #if the median num is equal to the target, return the index of median num
            if nums[middle] == target:
                return middle

            #check if the median num is larger than the target 
            if nums[middle] > target:
                #move the right pointer to middle to check the first half of the array 
                right = middle - 1
            #check if the median num is smaller than the target 
            if nums[middle] < target:
                left = middle + 1 
                #move the left pointer to the middle to check second half of the array 
        return -1 
