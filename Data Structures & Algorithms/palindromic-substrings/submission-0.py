class Solution:
    def countSubstrings(self, s: str) -> int:
        #Counter for total number of substrings 
        num_substrings = 0

        #Try every index as a possible center of a palindrome 
        for i in range(len(s)):
            #Check odd length palindromes 
            left = i 
            right = i 

            #Check both pointers are in bounds and characters at each index matchs 
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                #Count that substring as one 
                num_substrings += 1 
                #Expand outwards 
                left -= 1 
                right += 1
            
            #Check even length palindromes 
            left = i 
            right = i + 1

            #Check both pointers are in bounds and characters at each index matchs 
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                #Count that substring as one 
                num_substrings += 1 
                #Expand outwards 
                left -= 1 
                right += 1
        
        #Return the total palindrome count
        return num_substrings
            