class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        result = []
        path = []

        #Every call should track the index the call can use and the sum of nums inside the path 
        def backtrack(start, current_sum):
            #Base casess 
            #When the sum == target, add path to result 
            if current_sum == target:
                result.append(path.copy())
                return
            #When sum>target, reject that branch
            if current_sum > target:
                return 
            #Choose each candidate using index i and recursively call each candidate
            for i in range(start, len(nums)):
                candidate = nums[i]
                path.append(candidate)
                #Explore this choice and reuse the same candidate 
                backtrack(i, current_sum + candidate)
                #Remove that choice from path before moving on to the next candidate 
                path.pop()
        
        backtrack(0,0)
        return result