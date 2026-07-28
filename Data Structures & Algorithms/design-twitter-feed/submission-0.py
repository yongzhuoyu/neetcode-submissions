class Twitter:

    def __init__(self):
        #Require a global increasing timestamp 
        self.time = 0
        #Require a hashmap to map userId -> list of [time, tweetID]
        self.tweets = {}
        #Require a hashmap to map followerId -> set of followeeIds
        self.following = {}

    def postTweet(self, userId: int, tweetId: int) -> None:
        #Check if user is in tweets, if not add them into tweets 
        if userId not in self.tweets:
            self.tweets[userId] = [[self.time, tweetId]]
        else:
            #Append to list of tweets under userId
            self.tweets[userId].append([self.time, tweetId])
        #Increment time
        self.time += 1 

    def getNewsFeed(self, userId: int) -> List[int]:
        #Build a list of users whose tweets should be considered
        users = set()
        users.add(userId)
        if userId in self.following:
            users.update(self.following[userId])
        #Initialise a heap to store tweets by all users and order them based on the most recent tweet as the root 
        heap = []
        for userId in users:
            if userId in self.tweets:
                for time, tweetId in self.tweets[userId]:
                    heapq.heappush(heap, [-time, tweetId])
        #Pop the 10 most recent tweets in heap and add them to result 
        result = []
        while heap and len(result) < 10:
            time, tweetId = heapq.heappop(heap)
            result.append(tweetId)
        return result

    def follow(self, followerId: int, followeeId: int) -> None:
        #Check if followerId exist in self.following 
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
            
    def unfollow(self, followerId: int, followeeId: int) -> None:
        #Remove followerID if it exists in self.following
        if followerId in self.following:
            self.following[followerId].discard(followeeId)

