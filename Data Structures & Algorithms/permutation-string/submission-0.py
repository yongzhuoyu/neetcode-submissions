class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Brute force: Try every substring of s2 with len(s1)
        #For each substring, sort it and compare with sorted s1 

        target = sorted(s1)
        window_length = len(s1)
        for i in range(len(s2) - window_length + 1):
            #Extract the substring of window_length 
            substring = s2[i : i + window_length]
            #Compare with sorted s1
            if target == sorted(substring):
                return True 
        return False