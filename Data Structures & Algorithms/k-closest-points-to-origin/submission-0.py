class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        #Create a heap to store negative distance and its coordinates 
        heap = []
        for point in points:
            #Calculate the negative distance from origin for each point 
            negative_distance = -(point[0]*point[0] + point[1]*point[1])
            #Push it into the heap 
            heapq.heappush(heap, [negative_distance, point])
            #Pop the furthest coordinate from heap to maintain heap of k size 
            if len(heap) > k:
                heapq.heappop(heap)

        result = []
        #Heap contains the k closest points, append only the coordinates 
        for i in range(k):
            result.append(heap[i][1])
        return result