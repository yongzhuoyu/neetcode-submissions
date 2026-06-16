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
        buy = 0
        sell = 1
        maxProfit = 0

        #the loop continues running until it reaches the end of array 
        while sell < len(prices):
            #Check if the sell price is higher than buy price 
            if prices[sell] > prices[buy]:
                #calculate profit of the current pair
                profit = prices[sell] - prices[buy]
                #compare it to the current maxProfit and update maxProfit if current is larger
                maxProfit = max(profit, maxProfit)
            #if sell price is lower or equal to buy price, update buy day to sell day 
            else:
                buy = sell
            #move sell day foward
            sell += 1
        return maxProfit

        


        