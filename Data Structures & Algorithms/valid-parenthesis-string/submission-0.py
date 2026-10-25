class Solution:
    def checkValidString(self, s: str) -> bool:
        low = 0
        high = 0
        for ch in s:
            #Check if character is * 
            if ch == '*':
                low -= 1
                high += 1 
            #Check if character is (
            if ch == '(':
                low += 1
                high += 1
            #Check if character is )
            if ch == ')':
                low -= 1
                high -= 1 
            #If high is negative, return False 
            if high < 0:
                return False 
            low = max(0, low)
        return low == 0
            