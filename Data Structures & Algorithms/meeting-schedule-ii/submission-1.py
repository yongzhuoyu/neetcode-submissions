"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:
        intervals.sort(key=lambda x: x.start)

        heap = []
        for interval in intervals:
            start = interval.start
            end = interval.end

            #Check whether the current interval starts after the earliest end time 
            if heap and start >= heap[0]:
                #Remove the earliest end time and add the current meeting end 
                heapq.heappop(heap)
                heapq.heappush(heap, end)
            else:
                #Allocate a new meeting room for overlapping intervals
                heapq.heappush(heap, end)
        return len(heap)