class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (right + left) // 2
            if nums[mid] == target:
                return mid
            #Check if the left half is sorted to identify the sorted half
            if nums[left] <= nums[mid]:
                #Check whether target lies inside the sorted half 
                if nums[left] <= target < nums[mid]:
                    #Move right pointer and search the left half 
                    right = mid - 1
                else:
                    #Move left pointer and search the right half
                    left = mid + 1
            #Else, right half is sorted
            else:
                #Check whether target lies inside the sorted half 
                if nums[mid] < target <= nums[right]:
                    #Move left pointer and search the right half 
                    left = mid + 1
                else:
                    #Move right pointer and search the left half
                    right = mid - 1
        return -1