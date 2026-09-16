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
                lastBracket = stack[-1]
                #check whether the last bracket is the opening bracket of the current bracket 
                if lastBracket == bracketMap[bracket]:
                    stack.pop()
        if len(stack) == 0:
            return True 
        else: 
            return False
