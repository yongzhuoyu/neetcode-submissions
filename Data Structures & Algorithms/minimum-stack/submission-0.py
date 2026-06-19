class MinStack:
    #Use an additional stack(minStack) to store the minimum at each point 
    #Main stack stores all the values
    #Each position in minStack has to correspond to the same position in main stack 
    def __init__(self):
        self.mainStack = []
        self.minStack = []

    def push(self, val: int) -> None:
        self.mainStack.append(val)
        
        #Always add the first element first because minStack[-1] will crash if it is empty
        if len(self.minStack) == 0:
            self.minStack.append(val)
        else:
            self.minStack.append(min(val, self.minStack[-1]))

    def pop(self) -> None:
        self.mainStack.pop()
        self.minStack.pop()

    def top(self) -> int:
        return self.mainStack[-1]

    def getMin(self) -> int:
        return self.minStack[-1]
