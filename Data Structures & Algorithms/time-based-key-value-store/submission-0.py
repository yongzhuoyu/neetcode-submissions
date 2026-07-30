class TimeMap:

    def __init__(self):
        #Create a hashmap to store a list of [timestamp, value] pairs representing the keys history
        self.timeMap = {}

    def set(self, key: str, value: str, timestamp: int) -> None:
        #Check if the key exists in timeMap 
        if key not in self.timeMap:
            self.timeMap[key] = [[timestamp, value]]
        else:
            #add [timestamp, value] as a pair 
            self.timeMap[key].append([timestamp, value])

    def get(self, key: str, timestamp: int) -> str:
        #Check whether the key exist 
        if key not in self.timeMap:
            return ""
        #Get the history of [timestamp, value] based on key 
        history = self.timeMap[key]
        #Binary search on the largest timestamp <= requested_timestamp 
        left = 0
        right = len(history) - 1
        result = ""
        while left <= right:
            #Get the middle index 
            mid = (right + left) // 2
            #Get the current timestamp and value 
            current_timestamp = history[mid][0]
            current_value = history[mid][1]
            #Check if the current timestamp <= requested_timestamp
            if current_timestamp <= timestamp:
                #Save the answer and search right for a larger timestamp
                result = current_value 
                left = mid + 1
            #if not, search left for a valid timestamp 
            else:
                right = mid - 1 
        return result
