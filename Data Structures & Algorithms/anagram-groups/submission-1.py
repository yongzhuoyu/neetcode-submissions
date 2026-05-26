class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #brute force solution: sort each string in the list and group them together in a hash map 
        #if it does not, add the sorted string as a key and create a list to store the anagram as a value 
        #if it does, js append the anagram to the list 
        #return the the list of anagrams by accessing the values of hashmaps 
        # anagramMap = {}

        # #iterate through the list to get each string and sort it 
        # for word in strs:
        #     sortedStr = "".join(sorted(word))
        #     #check if it exists in a hashmap 
        #     if sortedStr not in anagramMap:
        #         anagramMap[sortedStr] = [word]
        #     else:
        #         anagramMap[sortedStr].append(word)

        # result = []
        # for anagramList in anagramMap.values():
        #     result.append(anagramList)
        # return result

        #using a hash map to map the counts of character to the list of anagrams 
        #track the count using an array of size 26 and updating the index represent different alphabets 
        #create an empty hashmap to store the the key value pair of count and list of anagrams 
        anagramMap = {}
        #iterate through every word in the string 
        for word in strs:
            #create an empty list of size 26 for each word 
            count = [0] * 26
            #iterate through each word and count the frequency of each character 
            for ch in word:
                index = ord(ch) - ord('a')
                count[index] += 1            #check if the count exist in the hashmap 
            if tuple(count) not in anagramMap:
                #if not convert the list -> tuple and add it to the hash map as a key with the word as an anagram 
                anagramMap[tuple(count)] = [word]
            #if it does exist, append the word to the list of anagrams 
            else:
                anagramMap[tuple(count)].append(word)
        #return only the values in the hashmap 
        return list(anagramMap.values())