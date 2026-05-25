class Solution:
    def isValid(self, s: str) -> bool:
        #map all closing brackets to its opening brackets 
        bracketMap = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        #create a stack 
        stack = []

        #iterate through every single character 
        for i in range(len(s)):
            bracket = s[i]
            #if its an opening bracket 
            if bracket not in bracketMap:
                stack.append(bracket)
            #if its a closing bracket 
            else:
                #check whether the stack is empty before accessing the last index 
                #check whether the last bracket is the opening bracket of the current bracket 
                if len(stack) == 0:
                    return False 
                if stack[-1] != bracketMap[bracket]:
                    return False 
                stack.pop()
        if len(stack) == 0:
            return True 
        else: 
            return False
