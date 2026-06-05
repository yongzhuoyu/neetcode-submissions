class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if not nums:
        #     return 0
        # #Sort the nums array 
        # nums.sort()
        # current = 1
        # longest = 1
        # for i in range(1, len(nums)):
        #     #Check whether the two elements are duplicate 
        #     if nums[i] == nums[i-1]:
        #         #if so, continue to the next iteration 
        #         continue
        #     #If the next element is 1 greater than current
        #     if nums[i] == nums[i-1] + 1:
        #         #add it to the current sequence 
        #         current += 1
        #     #if not, reset the sequence to 1 
        #     else:
        #         current = 1
        #     #check whether the current streak is longer than max sequence 
        #     longest = max(current, longest)
        # return longest

        #Starting couting a sequence if it is the start of a sequence 
        #A number is the start of a sequence if num-1 dosent exist in the set 

        #Store all numbers into a set instead
        numSet = set(nums)
        #Guard against empty input as their sequence would be 0
        longest = 0
        for num in numSet:
            #Check whether that number is the start of a sequence 
            if num - 1 not in numSet:
                #Count the current sequence as long as the next number exist 
                currNum = num
                currSeq = 1
                while currNum  + 1 in numSet:
                    currSeq += 1 
                    currNum += 1 
                #Compare current sequence with longest sequence 
                longest = max(longest, currSeq)
        return longest