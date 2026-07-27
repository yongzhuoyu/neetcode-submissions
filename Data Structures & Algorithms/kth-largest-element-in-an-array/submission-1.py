class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        #Create a heap to store the k largest numbers seen 
        heap = []
        for num in nums:
            #Push each number into the heap 
            heapq.heappush(heap, num)
            #Pop from heap if it exceeds k size 
            if len(heap) > k:
                heapq.heappop(heap)
        #heap[0] is the smallest among the k largest numbers, so it is the kth largest overall
        return heap[0]