class Solution:
    def rob(self, nums: List[int]) -> int:
        #If there is only one house, return the money immediately 
        if len(nums) == 1:
            return nums[0]

        #Helper used to solve the original house robber problem 
        def rob_linear(houses):
            memo = {}

            def max_money(i):
                #Base cases
                if i < 0:
                    return 0

                if i == 0:
                    return houses[0]

                if i in memo:
                    return memo[i]

                max_money_skip = max_money(i - 1)
                max_money_rob = houses[i] + max_money(i - 2)
                current_max = max(max_money_skip, max_money_rob)

                memo[i] = current_max
                return current_max

            #Always start max_money from the final_index of houses 
            return max_money(len(houses) - 1)

        #Two cases for the outer function 
        #Exclude the final house 
        exclude_final_house = rob_linear(nums[:-1])
        exclude_first_house = rob_linear(nums[1:])
        return max(exclude_final_house, exclude_first_house)
