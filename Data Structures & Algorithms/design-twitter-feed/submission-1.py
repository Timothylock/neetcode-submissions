class Twitter:

    def __init__(self):
        self.following = {}
        self.posts = {} # Dict of min heaps. Min heaps because we can easily pop out the mins
        self.intID = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.posts:
            self.posts[userId] = []
        
        if len(self.posts[userId]) >= 10:
            heapq.heappushpop(self.posts[userId], (self.intID, tweetId))
        else:
            heapq.heappush(self.posts[userId], (self.intID, tweetId))
        
        self.intID += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        fuid = [userId]
        if userId in self.following:
            fuid += self.following[userId].keys()
        posts = []

        for uid in fuid:
            if uid not in self.posts:
                continue

            posts += self.posts[uid]

        heapq.heapify_max(posts)
        res = []
        for _ in range(10):
            if len(posts) == 0:
                break

            _, tweetId = heapq.heappop_max(posts)
            res.append(tweetId)

        return res



    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            self.following[followerId] = {}

        self.following[followerId][followeeId] = None
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.following:
            return 
        if followeeId not in self.following[followerId]:
            return

        del self.following[followerId][followeeId]
