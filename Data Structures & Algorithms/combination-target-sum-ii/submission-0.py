class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        path = []
        result = []

        def backtrack(start, current_sum):
            #Base cases: save path to result if current_sum == target 
            if current_sum == target:
                result.append(path.copy())
                return 
            #Return if current_sum > target 
            if current_sum > target:
                return
            #Try every candidate from start 
            for i in range(start, len(candidates)):
                #Skip duplicate candidates at the same recursion level 
                if i > start and candidates[i] == candidates[i-1]:
                    continue
                #Choose this candidate 
                path.append(candidates[i])
                #Recurse from the index after the selected candidate
                backtrack(i+1, current_sum + candidates[i])
                #Remove the last chosen candidate every time a child function returns
                path.pop()
        backtrack(0,0)
        return result