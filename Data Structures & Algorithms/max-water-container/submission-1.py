class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #brute force solution: try all pairs of bars and calculate the max amount of water each pair can store
        #initialise max to store the max amount of water 
        # maxArea = 0
        # #use a nested for loop to get alls pairs of bars 
        # for i in range(len(heights)):
        #     for j in range(i + 1, len(heights)):
        #         #get the width by comparing between the two index 
        #         width = j - i
        #         #compare the shorter bar 
        #         shorterHeight = min(heights[i], heights[j])
        #         #calculate the area = width x height of the shortest bar
        #         area = width * shorterHeight
        #         #update the max if the current container stores more water 
        #         if area > maxArea:
        #             maxArea = area
        # #return max 
        # return maxArea 

        #use a two pointer approach that starts with first and last height 
        #because we are starting with the widest possible width 
        maxArea = 0
        left = 0 
        right = len(heights) - 1
        while left < right:
            #calculate area of current container 
            area = (right-left) * min(heights[left], heights[right])
            #compare it to the current max area 
            maxArea = max(area, maxArea)
             #if its lower than the max area, compare the heights of both bars 
            #if the left bar is shorter, increment increment by 1 
            if heights[left] < heights[right]:
                left+=1
            else:
            #if the right bar is shorter, decrement right by 1 
                right-=1
        return maxArea