class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        #interval = [currentStart, currentEnd]
        #new_interval = [newStart, newEnd]
        #Every interval must fall into one of 3 cases: 
        # - Completelely before new_interval: currentEnd < newStart
        # - Completeley after new_interval: currentStart > newEnd
        # - Overlapping: currentStart <= newEnd and currentEnd >= newStart 
        
        result = []
        i = 0
        # Add non overlapping intervals before newInterval
        while i < len(intervals) and intervals[i][1] < newInterval[0]:
            result.append(intervals[i])
            i+=1 

        #Check whether the currentInterval start before or during newEnd 
        #if yes, both overlapping conditions are true and merge intervals that overlap with new Interval 
        while i < len(intervals) and intervals[i][0] <= newInterval[1]:
            #Find the newStart and newEnd of the merged intervals
            newStart = min(intervals[i][0], newInterval[0])
            newEnd = max(intervals[i][1], newInterval[1])
            newInterval = [newStart, newEnd]
            i+=1
        
        #Add the merged newInterval 
        result.append(newInterval)

        #Add remaining intervals after
        while i <len(intervals) and intervals[i][0] > newInterval[1]:
            result.append(intervals[i])
            i+=1
        return result