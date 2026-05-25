class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        #Brute force: trying every possible substring starting at every index 
        #initialise a variable to store the length of longest substring
        longest = 0
        for i in range(len(s)):
        #create a hashmap to store the characters and the count of each ch 
        #in the window starting from i 
            countMap = {}
            for j in range(i , len(s)):
                #check if that charcter is in hashmap 
                if s[j] not in countMap:
                    countMap[s[j]] = 1
                else:
                    countMap[s[j]] += 1
                #calculate the length of the window 
                windowSize = j - i + 1
                #get the numbers of characters to be replaced in each window 
                mostFrequent = max(countMap.values())
                replace = windowSize - mostFrequent

                #check if num of ch replaced is less than k, if so, it is a valid window 
                if replace <= k:
                    #update the maxlength of substring 
                    longest = max(longest, windowSize)
                else:
                    break
        return longest