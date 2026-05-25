class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # #Brute force method: try every possible pair of buying and selling days 
        # #initialise variable for max profit 
        # maxProfit = 0

        # for i in range(len(prices)):
        #     #iterate from i + 1 to avoid repeating days 
        #     for j in range(i+1, len(prices)):
        #         #calculate profit for each pair of days 
        #         profit = prices[j] - prices[i]

        #         #check whether the current profit is more than maxProfit 
        #         if profit > maxProfit:
        #             maxProfit = profit
        
        # return maxProfit

        #Sliding window where we find the cheapest buying day and the highest selling day 
        buying = 0
        selling = 1
        maxProfit = 0

        #the loop continues running until it reaches the end of array 
        while selling < len(prices):
            #calculate profit of the current pair of buying and selling 
            profit = prices[selling] - prices[buying]

            #check whether the profit is negative, if it is, change the current buying day to the current day 
            if profit < 0:
                buying = selling
            #if the profit is positive, compare it to the current maxProfit and update maxProfit if current is larger 
            else:
                if profit > maxProfit:
                    maxProfit = profit 
            #increment selling by 1 
            selling += 1
        return maxProfit
        