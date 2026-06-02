class Solution:
    def romanToInt(self, s: str) -> int:
        #Create a hash map to map the symbol to its value 
        valuesMap = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        #Core condition: for each index i, check if i has a next character and 
        #value[i] < value[i+1], subtract value from total 
        #if not, add value to total 
        total = 0
        for i in range(len(s)):
            curr_value = valuesMap[s[i]]
            #Check if i is the last index, if so add value to total 
            if i < len(s) - 1:
                next_value = valuesMap[s[i+1]]
                #Check if curr_value is smaller than next_value
                #if so, subtract it from total
                if curr_value < next_value:
                    total-=curr_value
                else:
                    total+=curr_value
            else:
                total+= curr_value
        return total