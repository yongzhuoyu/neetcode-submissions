class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # #Brute force method: try every possible substring and check if the substring has any duplicates 
        # LongestStr = 0

        # for i in range(len(s)):
        #     #store all seen character
        #     seen = {}
        #     #nested loop would iterate from i+1 so we dont repeat the same ch 
        #     for j in range(i+1, len(s)):
        #         #check whether ch is in hashmap 
        #         if s[j] in seen:
        #             break
        #         seen[s[j]] = 1
        #         LongestStr = max(LongestStr, len(seen))
        # return LongestStr

        #sliding window: hash map stores the index of each ch so when we find a repeat, 
        #jump the left pointer directly to the right position instead of moving it one step at a time
        
        #create a left pointer, an empty hash map to store the result and the current maxLength 
        left = 0 
        seen = {}
        maxLength = 0

        #iterate through the entire string
        for right in range(len(s)):
            currentCh = s[right]
            #check if the currentch is inside seen, 
            #if so update the left counter to the index of the prevous occurence of the ch + 1
            if currentCh in seen:
                #use max() to prevent the left pointer to move backwards 
                left = max(left, seen[currentCh] + 1)
            #if the ch is not in seen, add it to it with currentCh and its index as a key value pair 
            seen[currentCh] = right 
            #compare the current window length with the stored max length
            maxLength = max(maxLength, right - left + 1)
        return maxLength





