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
        self.user_to_tweets = collections.defaultdict(list)
        self.user_to_followers = collections.defaultdict(set)
        self.counter = 0
    def postTweet(self, userId: int, tweetId: int) -> None:
        '''
        Composes a new tweet with ID tweetId by the user userId. Each call to this function will be made with a unique
        tweetId.
        '''
        self.user_to_tweets[userId].append([self.counter, tweetId])
        self.counter -= 1

    def getNewsFeed(self, userId: int) -> List[int]:
        '''
        Retrieves the 10 most recent tweet IDs in the user's news feed. Each item in the news feed must be posted by
        users who the user followed or by the user themself. Tweets must be ordered from most recent to least recent.
        '''
        import heapq
        maxheap = []
        self.user_to_followers[userId].add(userId)
        for followee in self.user_to_followers[userId]:
            if followee in self.user_to_tweets:
                i = len(self.user_to_tweets[followee])-1
                count, tweet_id = self.user_to_tweets[followee][i]
                heapq.heappush(maxheap, (count, followee, i, tweet_id))
        final_arr = []
        while maxheap and (len(final_arr) < 10):
            count, followeeId, i, tweet_id = heapq.heappop(maxheap)
            final_arr.append(tweet_id)
            if i > 0:
                new_i = i - 1
                new_count, new_tweet_id = self.user_to_tweets[followeeId][new_i]
                heapq.heappush(maxheap, (new_count, followeeId, new_i, new_tweet_id))
        return final_arr

    def follow(self, followerId: int, followeeId: int) -> None:
        '''
        The user with ID followerId started following the user with ID followeeId.
        '''
        self.user_to_followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        '''
        The user with ID followerId started unfollowing the user with ID followeeId.
        '''
        if followeeId not in self.user_to_followers[followerId]: return
        self.user_to_followers[followerId].remove(followeeId)

# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)