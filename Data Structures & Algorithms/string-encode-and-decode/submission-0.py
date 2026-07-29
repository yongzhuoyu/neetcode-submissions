class Solution:

    def encode(self, strs: List[str]) -> str:
        #Use an array to store the encoded parts
        encoded = []
        for string in strs:
            #add the length of string and # in front of each string 
            encoded.append(str(len(string)))
            encoded.append("#")
            encoded.append(string)
        #Join them together into a single string and return 
        return "".join(encoded)
            
            
    def decode(self, s: str) -> List[str]:
        result = []
        i = 0

        while i < len(s):
            #Find the next "#" by initialising j and moving j forward until we find "#"
            j = i
            while s[j] != "#":
                j += 1
            #Find the length of a substring
            str_length = int(s[i:j])
            #Find the index of the start of word and end of word 
            word_start = j + 1
            word_end = word_start + str_length - 1
            #Splice the substring and append it to result 
            result.append(s[word_start: word_end + 1])
            #Move the i pointer 
            i = word_end + 1
        return result