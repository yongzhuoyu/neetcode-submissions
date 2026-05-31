"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        #Overlap condition: current_start < previous_end
        #Sort intervals by start time 
        intervals.sort(key=lambda x:x.start)
        for i in range(1, len(intervals)):
            #Compare each interval with the previous one 
            prev_interval = intervals[i-1]
            curr_interval = intervals[i]
        
            #If current start is before previous end, return False
            if curr_interval.start < prev_interval.end:
                return False
        #If no overlaps, return True
        return True
