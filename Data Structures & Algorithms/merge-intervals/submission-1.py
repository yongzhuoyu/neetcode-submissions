class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        intervals.sort()

        result = [intervals[0]]

        for interval in intervals[1:]:
            #Check if the current interval overlaps with the last interval in result 
            if interval[0] <= result[-1][1]:
                #Merge the intervals by updating the ending coordinate in result[-1]
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                result.append(interval)
        return result