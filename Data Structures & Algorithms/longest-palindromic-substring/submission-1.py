class Solution:
    def longestPalindrome(self, s: str) -> str:
        #Starting index of the longest palindrome found
        longest_start = 0

        #Longest length of the palindrome found 
        longest_length = 1

        #Try every index as a possible centre 
        for i in range(len(s)):
            #Initialise two pointers at i for odd length palindrome 
            left = i
            right = i

            #Continue expanding when pointers are not out of index and characters match 
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                #Calculate the length of substring palindrome 
                current_length = right - left + 1

                #If its more than longest_length, update the two state variables
                if current_length > longest_length:
                    longest_length = current_length
                    longest_start = left 

                #Expand outwards
                left -= 1 
                right += 1 

            #Initialise left to the current centre and right to centre plus one for even-length palindromes
            left = i
            right = i + 1

            #Continue expanding when pointers are not out of index and characters match 
            while (left >= 0 and right < len(s) and s[left] == s[right]):
                #Calculate the length of substring palindrome 
                current_length = right - left + 1

                #If its more than longest_length, update the two state variables
                if current_length > longest_length:
                    longest_length = current_length
                    longest_start = left 

                #Expand outwards
                left -= 1 
                right += 1 
        #Return the longest palindrome substring 
        return s[longest_start:longest_start + longest_length]
            