class Solution:
    def climbStairs(self, n: int) -> int:
        #Create a memo that maps number of steps -> number of ways to climb those steps
        memo = {}

        #Helper that returns the number of ways to climb given steps 
        def ways(steps):
            #Base case
            #Return number of ways to climb 0 step 
            if steps == 0:
                return 1 
            #Return number of ways to climb 1 step
            if steps == 1:
                return 1

            #If the number of steps has been calculated, return the saved answer 
            if steps in memo:
                return memo[steps]

            #Calculate the number of way when final step is one step 
            one_step_ways = ways(steps - 1)
            #Calcuate the number of ways when final step is two step 
            two_step_ways = ways(steps - 2)
            total_ways = one_step_ways + two_step_ways 

            #Save result to memo for future calls to reuse 
            memo[steps] = total_ways 
            return total_ways
        
        return ways(n)