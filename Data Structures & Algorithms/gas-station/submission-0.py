class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        #Represents the starting point of a station
        start = 0
        #Represent the net gas accumulated from start through i 
        tank = 0
        #Represent the net gas accumulated from 0 through i 
        total = 0

        for i in range(len(gas)):
            #Calculate the net gain or loss at each station 
            net = gas[i] - cost[i]
            #Add net to tank and total 
            tank += net
            total += net 

            #If tank becomes negative
            if tank < 0:
                #Eliminate all starting stations from start through i 
                start = i + 1 
                tank = 0
            
        if total < 0:
            return - 1 
        return start 
        