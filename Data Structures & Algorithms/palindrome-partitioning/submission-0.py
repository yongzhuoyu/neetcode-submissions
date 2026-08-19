class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []
        path = []
        #Return whether the substring reads the same forward and backward 
        def is_palindrome(substring):
            left = 0 
            right = len(substring) - 1
            while left < right:
                if substring[left] != substring[right]:
                    return False
                left += 1
                right -= 1
            return True

        def backtrack(start):
            #If all characters has been partioned, save the completed parition 
            if start == len(s):
                result.append(path.copy())
                return
            #Try every possible ending index for a substring beginning at start 
            for end in range(start, len(s)):
                substring = s[start : end+1]
                #Check if that substring is a palindrome 
                #If not, reject it and continue to the next partition 
                if is_palindrome(substring):
                    #Add it to path and recurse from the first unused character 
                    path.append(substring)
                    backtrack(end + 1)
                    path.pop()
                else:
                    continue
        backtrack(0)
        return result