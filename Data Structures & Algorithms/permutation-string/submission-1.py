class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        #Brute force: Try every substring of s2 with len(s1)
        #For each substring, sort it and compare with sorted s1 
        # target = sorted(s1)
        # window_length = len(s1)
        # for i in range(len(s2) - window_length + 1):
        #     #Extract the substring of window_length 
        #     substring = s2[i : i + window_length]
        #     #Compare with sorted s1
        #     if target == sorted(substring):
        #         return True 
        # return False
        
        #Build s1 count
        s1Count = {}
        for ch in s1:
            if ch not in s1Count:
                s1Count[ch] = 1
            else:
                s1Count[ch] += 1
        left = 0
        currentCount = {}
        for right in range(len(s2)):
            #Build character count of s2 
            if s2[right] not in currentCount:
                currentCount[s2[right]] = 1
            else:
                currentCount[s2[right]] += 1
            #Check the window size of currentCount does not exceed length of s1
            if right - left + 1 > len(s1):
                #If it exceeds, remove from left in the current window map
                currentCount[s2[left]] -= 1
                #If the count becomes zero delete the key 
                if currentCount[s2[left]] == 0:
                    del currentCount[s2[left]]
                left += 1
            #Dictionary equality check
            if currentCount == s1Count:
                return True
        return False
            
        