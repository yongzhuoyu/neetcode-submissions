class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        #Create memo that maps each index to whether s[i:] can be segmented
        memo = {}

        #Define dfs(i) as whether the suffix starting at i can be segmented into dictionary words 
        def dfs(i):
            #Base Case
            #return True when i reaches the end of the string 
            if i == len(s):
                return True

            if i in memo:
                return memo[i]

            #Try every possible prefix starting at i 
            for end in range(i + 1, len(s) + 1):
                prefix = s[i:end]
                #Check whether prefix exists in the dictionary 
                if prefix in wordDict:
                    #Recurse from the index after the prefix to check whether its suffix can be segmented 
                    if dfs(end):
                        #If recursive calls return True, cache True for this state and return True
                        memo[i] = True
                        return True 
            #If no prefix leads to a successful segmentation
            memo[i] = False
            return False
        return dfs(0)