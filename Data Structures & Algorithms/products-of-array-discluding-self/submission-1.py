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
        #Optimised space complexity: O(1) where only the result array is initialise
        #Initialise result filled with 1s  
        result = [1] * len(nums)

        #Store prefix products in result
        #prefix is the product of all elements before the current index 
        prefix = 1
        for i in range(len(nums)):
            result[i] = prefix
            #prefix variable is used to calculate prefix for the next index 
            prefix = prefix * nums[i]

        #multiply suffix products into result[i] to get product 
        #suffix is the product of all elments after the current index 
        suffix = 1
        for i in range(len(nums)-1, -1, -1):
            #Product of array would just multiplying prefix and suffix at each index since current result[i] already store the prefix
            result[i] = suffix * result[i]
            #after using suffix for currnet index, compute suffix for the previous index
            suffix = suffix * nums[i]
        return result
        # i =3, suffix=1, prefix = 8, new result[i] = 8
        # i =2, suffix=6*1=6, prefix = 2, new result[i] = 12
        # i =1, suffix=6*4=24, prefix = 1, newresult[i] = 24
        # i =0, suffix=24*2=48, prefix = 1, newresult[i] = 48