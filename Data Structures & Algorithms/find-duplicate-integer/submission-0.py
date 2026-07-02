class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow = 0 
        fast = 0
        #Find a meeting point inside the cycle 
        while True:
            #Fast moves two steps at a time while slow moves one step at a time
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break
        #Find the cycle entrance 
        #Initiase one pointer to the start of the list
        finder = 0 
        while finder != slow:
            #Both pointers move one step at a time until they meet again at the cycle entrance 
            finder = nums[finder]
            slow = nums[slow]
        return finder