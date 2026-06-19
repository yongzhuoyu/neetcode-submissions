class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        #Brute force

        #For each day i, scan every future day j 
        #Numer of days warmer than i day = j - i 
        #If none found, answer stays at 0 

        result = [0] * len(temperatures)
        for i in range(len(temperatures)):
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    result[i] = j - i
                    break
        return result
