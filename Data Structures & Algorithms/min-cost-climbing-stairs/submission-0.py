class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        #Memo that maps each stair index to the minimum cost of reaching it
        memo = {}

        #Helper returns minimum total cost to reach stair i 
        def min_cost(stair):
            #Base case: cost for stair 0 and stair 1 
            if stair == 0:
                return cost[0]
            if stair == 1:
                return cost[1]

            #Return cache result if stair i has already been calculated 
            if stair in memo:
                return memo[stair]

            #Recursively calculate the minimum costs of reaching the previous two stairs 
            last_stair_cost = min_cost(stair - 1)
            previous_stair_cost = min_cost(stair - 2)

            stair_cost = cost[stair] + min(last_stair_cost, previous_stair_cost)

            memo[stair] = stair_cost 
            #Return the cheaper route of the two final stairs 
            return stair_cost 
        
        #Use the helper to calculate the cost of the final two stairs before the top 
        last_stair_cost = min_cost(len(cost) - 1)
        second_last_stair_cost = min_cost(len(cost) - 2)

        #Return the lower cost of the two steps 
        return min(last_stair_cost, second_last_stair_cost)
