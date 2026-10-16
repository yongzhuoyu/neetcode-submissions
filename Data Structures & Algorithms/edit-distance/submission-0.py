class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        #Create memo mapping (i, j) to the result
        memo = {}

        #Define dfs(i, j) to be the minimum operations needed to transform word1[i:] to word2[j:]
        def dfs(i, j):
            #When i reaches the end of word1 
            if i == len(word1):
                return len(word2) - j
            #When j reaches the end of word2
            if j == len(word2):
                return len(word1) - i
            if (i, j) in memo:
                return memo[(i, j)]
            #Advance both i and j if character matches 
            if word1[i] == word2[j]:
                return dfs(i + 1, j + 1)
            #Otherwise, explore 3 operations
            #1. INSERT
            insert = 1 + dfs(i, j + 1)
            #2. DELETE 
            delete = 1+ dfs(i + 1, j)
            #3. REPLACE 
            replace = 1 + dfs(i + 1, j + 1)
            #Take the minimmum result among the 3 choices 
            result = min(insert, delete, replace)
            memo[(i, j)] = result
            return result
        return dfs(0, 0)