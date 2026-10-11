class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        #Create memo that maps (i, remaining) to the number of combinations
        memo = {}

        #Define dfs(i, remaining) to be the number of distinct combinations that sum to remaining using coins[i:]
        def dfs(i, remaining):
            #Base Case
            #When there is a valid combination
            if remaining == 0:
                return 1
            #When the total amount has been exceeded 
            if remaining < 0:
                return 0
            #When no dominations remain
            if i == len(coins):
                return 0 
            if (i, remaining) in memo:
                return memo[(i, remaining)]
            #Two Choices:
            #Choice 1: Take coins[i]
            take = dfs(i, remaining - coins[i])

            #Choice 2: Skip coins[i]
            skip = dfs(i + 1, remaining)

            #Add the number of combinations from both choices 
            result = take + skip
            memo[(i, remaining)] = result
            return result
        return dfs(0, amount)