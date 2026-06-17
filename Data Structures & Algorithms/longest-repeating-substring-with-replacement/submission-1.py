class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute force: trying every possible substring starting at every index 
        #initialise a variable to store the length of longest substring
        # longest = 0
        # for i in range(len(s)):
        # #create a hashmap to store the characters and the count of each ch 
        # #in the window starting from i 
        #     countMap = {}
        #     for j in range(i , len(s)):
        #         #check if that charcter is in hashmap 
        #         if s[j] not in countMap:
        #             countMap[s[j]] = 1
        #         else:
        #             countMap[s[j]] += 1
        #         #calculate the length of the window 
        #         windowSize = j - i + 1
        #         #get the numbers of characters to be replaced in each window 
        #         mostFrequent = max(countMap.values())
        #         replace = windowSize - mostFrequent
        #         #check if num of ch replaced is less than k, if so, it is a valid window 
        #         if replace <= k:
        #             #update the maxlength of substring 
        #             longest = max(longest, windowSize)
        #         else:
        #             break
        # return longest

        frequencyMap = {}
        maxFreq = 0
        left = 0
        longest = 0
        for right in range(len(s)):
            #populate the frequency map
            if s[right] not in frequencyMap:
                frequencyMap[s[right]] = 1
            else:
                frequencyMap[s[right]] += 1 
            #Get the most frequency character 
            maxFreq = max(maxFreq, frequencyMap[s[right]])
            #Get the current window size
            windowSize = right - left + 1 
            #Get the number of replacements needed for the current window 
            replacementsNeeded = windowSize - maxFreq 

            #Check if the current window is valid, if not shrink from left 
            while replacementsNeeded > k:
                #Remove s[left] from maxFreq
                frequencyMap[s[left]] -= 1
                left += 1
                #Update the current windowSize 
                windowSize = right - left + 1
                replacementsNeeded = windowSize - maxFreq
            #Update the length of longest substring 
            longest = max(windowSize, longest)
        return longest
