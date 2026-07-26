class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #Store negative weights to fake a max heap
        negative = []
        for stone in stones:
            negative.append(-stone)
        #Convert negative into a heap
        heapq.heapify(negative)

        #Continue simulation when there are two stones or more 
        while len(negative) >= 2:
            #Pop the two heavist stone and convert them into positive values 
            largest = -(heapq.heappop(negative))
            second_largest = -(heapq.heappop(negative))
            remaining = largest - second_largest
            #If both values are different, take the difference and add it back into negative 
            if remaining != 0:
                heapq.heappush(negative, -remaining)
        #return weight if there is one last stone, or 0 if none remains
        if len(negative) == 1:
            return -negative[0]
        else:
            return 0