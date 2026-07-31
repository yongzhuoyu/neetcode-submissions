class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        #Pair each position with its corresponding speed 
        cars = []
        for i in range(len(position)):
            cars.append([position[i], speed[i]])
        #Sort the pairs by position from the closest to furthest 
        cars.sort(reverse = True)
        #Create stack to store fleet arrival times 
        stack = []
        #Process each pair and calculate the time taken for each car to reach target 
        for car in cars:
            time_taken = (target - car[0]) / car[1]
            #Push the first fleet arrival time in the stack 
            if not stack:
                stack.append(time_taken)
            #Check whether current car would join the fleet in front of it 
            if time_taken <= stack[-1]:
                #Car would join the fleet so stack is unchanged 
                continue 
            #If not, the car cannot catch the fleet and create its own fleet 
            else:
                stack.append(time_taken)
        return len(stack)