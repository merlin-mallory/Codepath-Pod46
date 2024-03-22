class Twitter:
    '''
    355 - Design Twitter

    https://leetcode.com/problems/design-twitter/

    Design a simplified version of Twitter where users can post tweets, follow/unfollow another user, and is able to
    see the 10 most recent tweets in the user's news feed.

    Implement the Twitter class. See individual docstrings for details.

    Example 1:
    Input
    ["Twitter", "postTweet", "getNewsFeed", "follow", "postTweet", "getNewsFeed", "unfollow", "getNewsFeed"]
    [[], [1, 5], [1], [1, 2], [2, 6], [1], [1, 2], [1]]
    Output
    [null, null, [5], null, null, [6, 5], null, [5]]

    Explanation
    Twitter twitter = new Twitter();
    twitter.postTweet(1, 5); // User 1 posts a new tweet (id = 5).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5]. return [5]
    twitter.follow(1, 2);    // User 1 follows user 2.
    twitter.postTweet(2, 6); // User 2 posts a new tweet (id = 6).
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 2 tweet ids -> [6, 5]. Tweet id 6 should
    precede tweet id 5 because it is posted after tweet id 5.
    twitter.unfollow(1, 2);  // User 1 unfollows user 2.
    twitter.getNewsFeed(1);  // User 1's news feed should return a list with 1 tweet id -> [5], since user 1 is no
    longer following user 2.

    Constraints:
    1 <= userId, followerId, followeeId <= 500
    0 <= tweetId <= 10^4
    All the tweets have unique IDs.
    At most 3 * 10^4 calls will be made to postTweet, getNewsFeed, follow, and unfollow.
    '''

    def __init__(self):
        '''
        Initializes your twitter object.
        '''
        import collections
        self.count = 0
        self.user_to_tweets_list = collections.defaultdict(list)  # userId -> list of [count, tweetIds]
        self.user_to_followee_set = collections.defaultdict(set)  # userId -> set of followeeId

    def postTweet(self, userId: int, tweetId: int) -> None:
        '''
        Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique
        tweetId.
        '''
        self.user_to_tweets_list[userId].append([self.count, tweetId])
        self.count -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
        '''
        import heapq
        final_arr = []
        max_heap = []

        self.user_to_followee_set[userId].add(userId)
        for followeeId in self.user_to_followee_set[userId]:
            if followeeId in self.user_to_tweets_list:
                index = len(self.user_to_tweets_list[followeeId]) - 1
                count, tweet_id = self.user_to_tweets_list[followeeId][index]
                heapq.heappush(max_heap, [count, tweet_id, followeeId, index - 1])

        while max_heap and len(final_arr) < 10:
            count, tweet_id, followeeId, index = heapq.heappop(max_heap)
            final_arr.append(tweet_id)
            if index >= 0:
                count, tweet_id = self.user_to_tweets_list[followeeId][index]
                heapq.heappush(max_heap, [count, tweet_id, followeeId, index - 1])
        return final_arr

    def follow(self, followerId: int, followeeId: int) -> None:
        '''
        The user with ID followerId started following the user with ID followeeId.
        '''
        self.user_to_followee_set[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        '''
        The user with ID followerId started unfollowing the user with ID followeeId.
        '''
        if followeeId in self.user_to_followee_set[followerId]:
            self.user_to_followee_set[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)