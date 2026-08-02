class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        path = []
        result = []
        #Store numbers that are used and unavailable 
        used = set()

        def backtrack():
            #Base case is when the we have all the numbers in path 
            if len(nums) == len(path):
                result.append(path.copy())
                return 
            for num in nums:
                #Move to the the next number if it has already been used 
                if num in used:
                    continue
                #Add an unseen number into path and mark is an unavailable
                path.append(num)
                used.add(num)
                #DFS to add all numbers into path until base case is reached
                backtrack()
                #Remove num from path and make the number avialble again 
                path.pop()
                used.remove(num)
        backtrack()
        return result
                
            