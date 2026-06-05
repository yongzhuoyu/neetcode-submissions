class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0 
        right = len(numbers) - 1
        while left < right:
            #Calculate sum of the two numbers
            total = numbers[left] + numbers[right]
            #If total is less than target, move left pointer right 
            if total < target:
                left += 1 
            #If total is more than target, move right pointer left 
            elif total > target:
                right -= 1 
            #if total equals target, return the indexes of both numbers + 1 
            else:
                return [left+1, right+1]