class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # [[1,8], [3,6], [8,12]]
        #If intervals is empty, return empty array 
        if len(intervals) == 0:
            return []

        #Sort the intervals
        intervals.sort()

        #initialise merged array with the first interval
        merged = [intervals[0]]

        #start iterating from the second interval as we need the previous interval 
        for interval in intervals[1:]:
            #initialise previous and current interval 
            current_start, current_end = interval
            previous_start, previous_end = merged[-1]

            #Check whether the intervals are overlapping
            if current_start <= previous_end:
                #Compare whether current or previous has the bigger end 
                #Update the previous end to the bigger value of the two 
                merged[-1][1] = max(current_end, previous_end)
            else:
                merged.append(interval)
        return merged