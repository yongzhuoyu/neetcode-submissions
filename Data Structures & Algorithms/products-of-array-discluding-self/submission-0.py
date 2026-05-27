class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #Brute force: At each index, compute the product of every element except nums[i]

        # #Initialise product array
        # result = [] 
        # for i in range(len(nums)):
        #     product = 1
        #     for j in range(len(nums)):
        #         if j != i:
        #             product *= nums[j]
        #     result.append(product)
        # return result

        # prefix = [1, 1, 2, 8]
        # suffix = [48, 24, 6, 1]

        #Prefix and Suffix technique where we compute the product before and after each index and store it an array 
        #Initialise result, prefix and suffix array filled with 1s  
        prefix = [1] * len(nums)
        suffix = [1] * len(nums)
        result = [1] * len(nums)

        #Store prefix products for each index in a prefix array 
        #prefix product for first element is 1 so we can skip the iteration for that 
        for i in range(1, len(nums)):
            prefix[i] = nums[i-1] * prefix[i-1]
        #Store suffix products for each index in a suffix array 
        #spefix product for last element is 1 so we can skip the iteration for that 
        for i in range(len(nums)-2, -1, -1):
            suffix[i] = suffix[i+1] * nums[i+1]
        #Product of array would just multiplying prefix and suffix at each index 
        for i in range(len(nums)):
            result[i] = prefix[i] * suffix[i]
        return result