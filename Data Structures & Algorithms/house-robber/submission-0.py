class Solution:
    def rob(self, nums: List[int]) -> int:
        #Memo that maps house index -> maximum money obtained from 0 to that index 
        memo = {}

        #Helper defines the maximum money from 0 to that index 
        def max_money(i):
            #Base case
            #If i is below 0, return 0 
            if i < 0:
                return 0
            #If is 0, return only the first house 
            if i == 0:
                return nums[i]

            #Check whether the result of that index has been cached 
            if i in memo:
                return memo[i]

            #Two decision branches
            #Skip house i: return the max amount from houses 0 to i - 1 
            max_money_skip = max_money(i - 1)
            #Rob house i: collect nums[i], skip adjacent house i - 1 and combine it with best result from 0 to i - 2 
            max_money_rob = nums[i] + max_money(i - 2)
            current_max = max(max_money_skip, max_money_rob)

            #Cache result in memo and return 
            memo[i] = current_max
            return current_max
        
        #Start the helper from the last index of the house 
        return max_money(len(nums) - 1)