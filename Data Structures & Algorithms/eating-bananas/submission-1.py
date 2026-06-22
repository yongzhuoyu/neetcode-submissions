class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #Brute Force: Try every possible speed from slowest to fastest 
        #Highest useful speed: max(piles) 
        #Calculate the total number of hours required to finish all the piles at that current speed
        #if hours < h, return speed 
        # for speed in range(1, max(piles) + 1):
        #         total_hours = 0
        #         for pile in piles:
        #             hours = math.ceil(pile/speed)
        #             total_hours += hours
        #         if total_hours <= h:
        #             return speed

        #Optimised Idea: Binary search on speed to find min speed that works 
        #Search space is left = 1, right = max(piles)
        #For each given speed, calculate total hours similar to brute force solution 
        #If total_hours <= h, speed works and save it as the current answer 
        #If speed works, there might be a slower speed that also works so we search left half 
        #If speed does not work, its too slow and we need a faster speed so we search right half
        left = 1
        right = max(piles)
        answer = right
        while left <= right:
            speed = (left + right) // 2
            total_hours = 0
            for pile in piles:
                hour = math.ceil(pile/speed)
                total_hours += hour
            if total_hours <= h:
                answer = speed
                right = speed - 1
            else:
                left = speed + 1
        return answer