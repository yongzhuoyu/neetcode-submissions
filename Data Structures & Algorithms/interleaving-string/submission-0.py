class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        #Return false if the combined length of s1 and s2 != s3
        if len(s1) + len(s2) != len(s3):
            return False
        #Create memo that maps (i, j) to its result
        memo = {}

        #Define dfs(i, j) to determine whether s1[i:] and s2[j:] can interleave to form s3[i+j:]
        def dfs(i, j):
            #Base Case
            #If i and j reaches the end of s1 and s2 respectively 
            if i == len(s1) and j == len(s2):
                return True
            if (i, j) in memo:
                return memo[(i, j)]
            #Get the current position at s3
            k = i + j
            #Choice 1: take from s1 
            #Check wheter i is within bounds 
            if i < len(s1):
                #Check whether s1[i] matches with s3[k]
                if s1[i] == s3[k]:
                    take_s1 = dfs(i + 1, j)
                    #If this branch succeeds, return True 
                    if take_s1:
                        memo[(i, j)] = True
                        return True
            #Choice 2: take from s2
            #Check whether j is within bounds 
            if j < len(s2):
                if s2[j] == s3[k]:
                    take_s2 = dfs(i, j+1)
                    if take_s2:
                        memo[(i, j)] = True
                        return True 
            memo[(i, j)] = False
            return False 
        return dfs(0,0)