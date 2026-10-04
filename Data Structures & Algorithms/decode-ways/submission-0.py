class Solution:
    def numDecodings(self, s: str) -> int:
        #Memo maps index i -> number of ways to decode a s[i:]
        memo = {}

        #Define dfs(i) to be the number of ways to decode the suffix starting at index i 
        def dfs(i):
            #Base Case:
            #When i reaches the end of the string, return 1 as that is one successful decoding 
            if i == len(s):
                return 1 
            #If the current character is 0, return 0 as we cant decode 0 by itself 
            if int(s[i]) == 0:
                return 0 
            #Check if memo if that if the result for the current index has been calculated 
            if i in memo:
                return memo[i]
            #Recurse to the next index and store the result 
            total = dfs(i + 1)

            #Check whether there is a second digit available 
            if (i + 1) < len(s):
                #Check whether that number is between 10 and 26
                if 10 <= int(s[i: i+2]) <= 26:
                    #Recurse two indexes ahead and add the result to total 
                    total += dfs(i + 2)
            #Store result in memo 
            memo[i] = total
            return total 

        return dfs(0)