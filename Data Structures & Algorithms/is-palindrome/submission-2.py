class Solution:
    def isPalindrome(self, s: str) -> bool:
        # #santise the input string by removing all empty spaces and non-alphnumeric character 
        # #since the string is case-insensitive, convert each character to a lower case 
        # cleaned = []
        # for ch in s:
        #     if ch.isalnum():
        #         cleaned.append(ch.lower())

        # left = 0 
        # right = len(cleaned) - 1
        # #continue checking until both the left and right index meets in the middle 
        # while left < right:
        #     #check whether the characters are the same, if not return false 
        #     if cleaned[left] != cleaned[right]:
        #         return False 
        #     #increment the left index and decrement the right index 
        #     left+=1
        #     right-=1
        # return True
        #Initialise two pointers
        left=0
        right=len(s)-1

        while left<right:
            #Move the left pointer to the next valid character 
            while left < right and not s[left].isalnum():
                left += 1
            #Move the right pointer to the next valid character 
            while left < right and not s[right].isalnum():
                right -= 1
            #Compare between two valid characters after making them lower case 
            if s[left].lower() != s[right].lower():
                return False
            left+=1
            right-=1
        return True