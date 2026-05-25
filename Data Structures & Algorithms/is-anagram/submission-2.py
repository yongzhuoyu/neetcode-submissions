class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #Sorted approach: if two strings are anagrams
        #They should be identical after sorting their ch 
        # return sorted(s) == sorted(t)

        #HashMap method 
        #IMPORTANT: Check if the lengths of both s and t are the same 
        if len(s) != len(t):
            return False 

        #Initialise an empty hash map 
        count = {}

        #Count the characters in s 
        for ch in s:
            if ch not in count:
                count[ch] = 1
            else:
                count[ch] += 1

        #Decrement the count of characters in count 
        for ch in t:
            if ch not in count:
                return False 
            else:
                count[ch] -= 1
        
        #Check whether all the values are 0
        for value in count.values():
            if value != 0:
                return False 
        return True 


