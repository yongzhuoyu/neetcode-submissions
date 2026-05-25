class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countMap = {}
        for num in nums:
            if num in countMap:
                countMap[num] += 1
            else:
                countMap[num] = 1
        
        sorted_keys = sorted(countMap.keys(), key=lambda x: countMap[x], reverse=True)

        result = []
        for i in range(k):
            result.append(sorted_keys[i])
        return result