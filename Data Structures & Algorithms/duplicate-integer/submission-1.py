class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #Brute Force Solution 
        #Compare every pair of numbers and 
        #check whether their indices have the same value 
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         if nums[i] == nums[j]:
        #             return True 
        # return False 

        #Hash Set Solution 
        #Create a new hash 
        seen = set()
    
        #Iterate through nums and check if num was seen 
        for num in nums:
            if num in seen:
                return True 
            #add number to seen if its the first time we see this num 
            seen.add(num)
        return False
