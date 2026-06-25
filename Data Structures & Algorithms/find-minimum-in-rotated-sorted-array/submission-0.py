class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0 
        right = len(nums) - 1 
        #while loop on stops when left == right
        while left < right:
            mid = (left + right) // 2
            #Check if nums[mid] > right
            if nums[mid] > nums[right]:
                #Search right half of array
                left = mid + 1
            #Else, the min is at mid itself or on the left half of array 
            else:
                right = mid
        return nums[left]