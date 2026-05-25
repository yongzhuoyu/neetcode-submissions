class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        #create a hashmap 
        countMap = {}

        #iterate through the nums array 
        for i in range(len(nums)):
            #check whether the number exist in hashmap, if not add the number and a count of 1
            if not nums[i] in countMap:
                countMap[nums[i]] = 1
            else:
                countMap[nums[i]] += 1
        
        #iterate through just the values in the hashmap 
        for value in countMap.values():
            if value > 1:
                return True 
        return False
         