class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        #Create a memo that maps (i, j) to the LCS length 
        memo = {}
        #Define dfs(i, j) to be the longest common subsequence length between text1[i:] and text2[j:]
        def dfs(i, j):
            #Base case:
            #When we reach the end of the string for either text1 or text2
            if i == len(text1) or j == len(text2):
                return 0
            if (i, j) in memo:
                return memo[(i, j)]
            #If a character from both string matches, count the match and progress both indexes by 1 
            if text1[i] == text2[j]:
                result = 1 + dfs(i + 1, j + 1) 
                return result
            else:
                #Skip the current character in text 1 
                skip_text1 = dfs(i + 1, j)
                #Skip the current character in text 2 
                skip_text2 = dfs(i, j + 1)
                #Take the maximum subsequence length from both choices 
                result = max(dfs(i + 1, j), dfs(i, j + 1))
                #Cache the result to (i, j)
                memo[(i, j)] = result
                return result
        return dfs(0, 0)