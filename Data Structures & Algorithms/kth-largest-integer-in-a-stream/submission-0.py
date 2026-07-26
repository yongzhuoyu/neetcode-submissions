class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        #Store how many values we care about 
        self.k = k
        #store the values that we are tracking
        self.heap = []

        #Add nums into heap and filter heap to the k largest values 
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        #Push the value into heap and heappush maintains heap property 
        heapq.heappush(self.heap, val)
        #Remove the smallest number to maintain heap size of k 
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        #Return heap[0] since it is the kth largest overall num 
        return self.heap[0]
