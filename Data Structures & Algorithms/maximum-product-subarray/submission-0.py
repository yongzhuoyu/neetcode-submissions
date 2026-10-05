class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        #Initialise current_max and current_min using the first number in the array 
        current_max = nums[0]
        current_min = nums[0]

        #Initiase overall result using the first number 
        result = nums[0]

        for num in nums[1:]:
            #Save the previous current_max and current_min
            #New states must be calcuated from the previous index states 
            previous_max = current_max 
            previous_min = current_min 

            #Calculate the 3 possible products:
            #Start a new subarray at the current number 
            #Extend the previous maximum_product subarray 
            #Extend the previous minimum_product subarray 

            #Set current_max to the largest of the 3 candidates 
            current_max = max(
                num,
                previous_max * num,
                previous_min * num
            )
            #Set current_min to the smallest of the 3 candidates 
            current_min = min(
                num,
                previous_max * num,
                previous_min * num
            )
            #Update result to the overall maximum product seen so far 
            result = max(current_max, result)
        return result