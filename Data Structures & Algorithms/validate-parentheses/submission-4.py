class Solution:
    def isValid(self, s: str) -> bool:
        #Create a hashmap to map the closing to opening brackets 
        bracketMap = {
            ")": "(",
            "}": "{",
            "]": "["
        }
        #Create a stack to push opening brackets 
        stack = []
        #Iterate through str 
        for bracket in s:
            #check if its an opening bracket, if so push it 
            if not bracket in bracketMap:
                stack.append(bracket)
            else:
                #check whether stack is empty 
                if len(stack) == 0:
                    return False
                #pop the last added bracket 
                last = stack.pop()
                #check whether it matches with the closing bracket 
                if bracketMap[bracket] != last:
                    return False
        #check whether all opening brackets r closed 
        if len(stack) != 0:
            return False
        return True

        # #map all closing brackets to its opening brackets 
        # bracketMap = {
        #     ')': '(',
        #     '}': '{',
        #     ']': '['
        # }
        # #create a stack 
        # stack = []

        # #iterate through every single character 
        # for i in range(len(s)):
        #     bracket = s[i]
        #     #if its an opening bracket 
        #     if bracket not in bracketMap:
        #         stack.append(bracket)
        #     #if its a closing bracket 
        #     else:
        #         #check whether the stack is empty before accessing the last index 
        #         #check whether the last bracket is the opening bracket of the current bracket 
        #         if len(stack) == 0:
        #             return False 
        #         if stack[-1] != bracketMap[bracket]:
        #             return False 
        #         stack.pop()
        # if len(stack) == 0:
        #     return True 
        # else: 
        #     return False

        
