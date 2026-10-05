class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        #Memo that maps remaining amount -> minimum number of coinds to make it 
        memo = {}

        #define dfs(remaining) as the minimum number of coins required to make exactly the remaining amount 
        def dfs(remaining):
            #Base case when remaining is 0
            if remaining == 0:
                return 0
            #Check if remaining has been calculated, if so return cached result
            if remaining in memo:
                return memo[remaining]

            #Initialise best result as infinity 
            best = float("inf")

            #Try every possible denomination 
            for coin in coins:
                #Only choose the coin if it dosent exceed remaining 
                if coin <= remaining:
                    #Recursively find the minimum number of coins to for amount left 
                    candidate = 1 + dfs(remaining - coin)
                    #Compare this candidate with the best result stored
                    best = min(best, candidate)
            #Store the best result in memo for this remaining amount 
            memo[remaining] = best
            return best

        answer = dfs(amount)
        if answer == float("inf"):
            return -1
        return answer