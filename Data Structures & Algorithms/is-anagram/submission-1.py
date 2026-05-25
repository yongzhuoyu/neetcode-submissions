class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #edge case: if they have different lengths: they cant be anagrams 
        if len(s) != len(t):
            return False
        
        #create a hashmap for the first string and matching each character to its count 
        sMap = {}
        for i in range(len(s)):
            #check if the ch alr exist in sMap
            if s[i] in sMap:
                #increment the count by 1 
                sMap[s[i]] += 1
            else:
                #else set the count of ch to 1
                sMap[s[i]] = 1

        #iterate through each character in t and check if it exists in sMap 
        for i in range(len(t)):
            #check that it exists in sMap, if not return false 
            if not t[i] in sMap:
                return False 
            #if it exists, decrement the count of that ch by 1 
            sMap[t[i]] -= 1
            #if the count goes below 0, return false
            if sMap[t[i]] < 0:
                return False
        return True 