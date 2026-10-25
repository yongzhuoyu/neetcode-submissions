class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        result = []
        for i, interval in enumerate(intervals):
            #Case 1: Current interval ends before the start of newInterval 
            if interval[1] < newInterval[0]:
                result.append(interval)

            #Case 2: Current interval overlaps with newInterval
            #Overlap condition: when newInterval starts before the end of the current_interval and ends after the start of the current_interval
            elif newInterval[0] <= interval[1] and newInterval[1] >= interval[0]:
                #Update the newInterval 
                newInterval[0] = min(interval[0], newInterval[0])
                newInterval[1] = max(interval[1], newInterval[1])
            
            #Case 3: Current interval starts after the end of newInterval
            else:
                #Append newInterval before appending the remaining intervals 
                result.append(newInterval)
                result.extend(intervals[i:])
                return result

        #If all intervals comes before the currentInterval 
        result.append(newInterval)
        return result
