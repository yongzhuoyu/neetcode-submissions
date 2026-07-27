class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        #Count how many times each task appears and map task -> frequency 
        countMap = {}
        for task in tasks:
            if task not in countMap:
                countMap[task] = 1
            else:
                countMap[task] += 1
        #Build a max heap from frequencies since we want the most frequently available tasks
        heap = []
        for value in countMap.values():
            heapq.heappush(heap, -value)
        #Store tasks that have been used but have remaining count 
        cooldown = deque()
        time = 0

        while heap or cooldown:
            time += 1 
            #check the front of cooldown and if it is ready 
            while cooldown and cooldown[0][1] <= time:
                #pop it from cooldown and push it back to the heap 
                count, available_time = cooldown.popleft()
                heapq.heappush(heap, count)
            #run one available task if possible 
            if heap:
                count = heapq.heappop(heap)
                # Counts are negative, so adding 1 means one copy has been used
                count += 1 
                #If it is not 0, that task still has reminaing copies 
                if count != 0:
                    available_time = time + n + 1 
                    cooldown.append([count, available_time])
        return time