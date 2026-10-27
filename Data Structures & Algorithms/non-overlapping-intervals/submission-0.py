class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        #Sort intervals by ending coordinate 
        intervals.sort(key=lambda x: x[1])
    
        last_end = intervals[0][1]
        removed = 0

        for interval in intervals[1:]:
            #Check if the current interval starts before last_end 
            if interval[0] < last_end:
                removed += 1 
            #Keep the current interval
            else:
                last_end = interval[1]
        return removed