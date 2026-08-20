class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        #Handle empty input by returning an empty array 
        if len(digits) == 0:
            return []

        #Create a hashmp that maps each digit to its set of characters 
        digits_to_letters = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }
        result = []
        path = []

        #Backtracking logic here is to create every possible combinations starting from the current digit, and path stores the selected letters from digit that has been processed 
        def backtrack(digit_index):
            #Check wwhether all the digits has been procssed
            if digit_index == len(digits):
                #join the letters into a string and add it to result 
                letters_str = "".join(path.copy())
                result.append(letters_str) 
                return 
            #Get the current digit using digit_index 
            current_digit = digits[digit_index]
            #Use hashmap to retrieve the letters for that digit 
            letters = digits_to_letters[current_digit]
            #Try every avaiable letter for that digit 
            for letter in letters:
                #Add the letter to the path 
                path.append(letter)
                #Recurse down to the next digit 
                backtrack(digit_index + 1)
                #Remove chosen letter after child call returns 
                path.pop()
        backtrack(0)
        return result