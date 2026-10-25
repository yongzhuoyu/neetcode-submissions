class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        # Sort intervals by starting coordinate.
        intervals.append(newInterval)
        intervals.sort()

        # Initialise result with the first interval.
        result = [intervals[0]]

        for interval in intervals[1:]:
            # Check whether the current interval overlaps
            # with the last merged interval.
            if interval[0] <= result[-1][1]:
                # Extend the ending coordinate if necessary.
                result[-1][1] = max(result[-1][1], interval[1])
            else:
                # Start a new non-overlapping interval.
                result.append(interval)

        return result
