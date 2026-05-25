class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # #brute force method: try every possible pair and see if they add up to the sum 
        # for i in range(len(nums)):
        #     #inner loop starts at the second number
        #     for j in range(i+1, len(nums)):
        #         if (nums[i] + nums[j]) == target:
        #             return [i, j]
        #create a hash map 
        seen = {}
        #iterate through the array and store the index and the number as a key value pair 
        for i in range(len(nums)):
            #calculate the complement of each num 
            complement = target - nums[i]
            #check if the complement is the hashmap 
            if not complement in seen:
                #if not, store the number as a key and its index as a value
                seen[nums[i]] = i 
            #if the complement is in hashmap, return the index of that complement and current index
            else:
                return [seen[complement], i]
        return []