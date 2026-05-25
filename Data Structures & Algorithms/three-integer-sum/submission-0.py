class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # #Brute force solution: Create all possible triplets 
        
        # #create a result list to store all possible triplets 
        # result = []

        # #triple for loop to iterate through nums
        # for i in range(len(nums)):
        #     #second for loop would iterate from i + 1 to prevent duplicate nums 
        #     for j in range(i+1 , len(nums)):
        #         #inner for loop would iterate from j+1 to prevent duplicate nums 
        #         for k in range(j+1, len(nums)):
        #             #sort the current combination of numbers 
        #             currentCom = sorted([nums[i], nums[j], nums[k]])
        #             #if this current combination adds up to 0 and does not exist in the result array 
        #             #append it to result 
        #             if sum(currentCom) == 0 and currentCom not in result:
        #                 result.append(currentCom)
        # return result

        #create an empty array to store result 
        result = []

        #sort the array first
        nums.sort()

        #iterate through the array and fix index i 
        #calculate the target from index i that will give a sum of 0 
        for i in range(len(nums)):
            #skip duplicate i by comparing it with the number before 
            if i > 0 and nums[i] == nums[i-1]:
                continue
            target = -nums[i]
            #use two pointers(left and right) to find the other two numbers that adds up to the target 
            left = i + 1
            right = len(nums) - 1
            #if sum of left and right < target, increment left 
            #if sum of left and right > target, decrement right
            #if sum of left and right == target, append it to the array 
            while left < right:
                currentSum = nums[left] + nums[right]
                if currentSum == target:
                    result.append([nums[i], nums[left], nums[right]])
                    #for left pointer, check whether the num on the right is duplicate, if so skip it 
                    while left < right and nums[left] == nums[left + 1]:
                        left += 1
                    #for right pointer, check whether the number on the left is a duplicate, if so skip it 
                    while left < right and nums[right] == nums[right - 1]:
                        right -= 1
                    #move both pointers inwards 
                    left += 1 
                    right -= 1 

                if currentSum < target:
                    left += 1
                if currentSum > target:
                    right -= 1

        return result
            
    
        
