class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        #Create a hash map to store each characters last occurence 
        last = {}
        for i in range(len(s)):
            last[s[i]] = i

        start = 0
        end = 0
        result = []

        #Iterate through the string to identify the partitions 
        for i in range(len(s)):
            #Update end to the last occurence of all character in this partition 
            end = max(end, last[s[i]])
            #Start a new partition and update result when we reach the end of the current partition 
            if i == end:
                result.append(end - start + 1)
                start = i + 1
        return result