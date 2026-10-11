class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #Create Memo that maps (i, holding) to the maximum addition profit 
        memo = {}

        #Define dfs(i, holding) to return the maximum profits from day i onward, given whether we own a stock 
        def dfs(i, holding):
            #If i is beyong the last trading day, return 0
            if i >= len(prices):
                return 0
            if (i, holding) in memo:
                return memo[(i, holding)]
            #If we own a stock, we have two choices 
            if holding:
                #Choice 1: Sell the stock today and advance by 2 days 
                sell = prices[i] + dfs(i + 2, False)
                #Choice 2: Continue holding and advance by 1 day
                hold = dfs(i + 1, True)
                #Take the maximum profits from both choices 
                profit = max(sell, hold)
            #If we dont own a stock, we have two choices 
            else:
                #Choice 1: Buy a stock and include buying cost 
                buy = -prices[i] + dfs(i + 1, True)
                #Choice 2: Skip today and advance 1 day 
                skip = dfs(i + 1, False)
                #Take the max profits from both decisions 
                profit = max(buy, skip)
            
            memo[(i, holding)] = profit
            return profit
        return dfs(0, False)