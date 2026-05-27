class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #Sorting based approach 
        #Create a hash map to count the frequency of each num 
        # countMap = {}
        # for num in nums:
        #     if num in countMap:
        #         countMap[num] += 1
        #     else:
        #         countMap[num] = 1

        # #Create a list of [frequency, num] pair so we can sort the array by frequency
        # pairs = []
        # for num, frequency in countMap.items():
        #     pairs.append([frequency, num])
        
        # #Sort pairs array based on frequency 
        # pairs.sort()

        # #Take the last k pairs as they are the most frequent elements 
        # #initialise result array 
        # result = []

        # #Iterate through the element from the back
        # for i in range(len(pairs)-1, len(pairs) - k - 1, -1):
        #     result.append(pairs[i][1])
        # return result

        #Bucket sort approach
        #Create a hash map to count the frequency of each num 
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1

        #Initialise a frequency bucket of len(nums)+1 since we have to account for numbers that appear 0 times
        frequencyBuckets = []
        for i in range(len(nums) + 1):
            frequencyBuckets.append([])

        #Add num into the frequency bucket 
        for num in countMap:
            count = countMap[num]
            frequencyBuckets[count].append(num)

        #Initiase array to store result elements
        result = []

        #Find the most frequent element by iterating from the last bucket 
        for i in range(len(frequencyBuckets) - 1, -1, -1):
            for num in frequencyBuckets[i]:
                result.append(num)

                if len(result) == k:
                    return result
        
