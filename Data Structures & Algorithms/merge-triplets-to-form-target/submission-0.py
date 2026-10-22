class Solution:
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        #Use three boolean flags to check whether the target coordinates are found 
        found = [False, False, False]

        #iterate through every triplet 
        for triplet in triplets:
            #Check whether any coordinates in triplet exceed its target 
            is_exceed = False 
            for i in range(3):
                if triplet[i] > target[i]:
                    is_exceed = True
                    break
            #If so, skip the entire triplet
            if is_exceed:
                continue
            #Chehck whether any coordinate in triplet exactly matches its target 
            for i in range(3):
                if triplet[i] == target[i]:
                    found[i] = True
        
        #Return True only if all 3 boolean flags are True 
        for i in range(3):
            if found[i] == False:
                return False
        return True