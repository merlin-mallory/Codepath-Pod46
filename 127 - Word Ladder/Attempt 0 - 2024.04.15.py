from typing import List
class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        127 - Word Ladder

        https://leetcode.com/problems/word-ladder/

        A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of
        words beginWord -> s1 -> s2 -> ... -> sk such that:

        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList.
        Note that beginWord does not need to be in wordList. sk == endWord Given two words, beginWord and endWord,
        and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord
        to endWord, or 0 if no such sequence exists.

        Constraints:
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.

        Plan:
        Graph Traversal with BFS
        Time: O(m * n^2), where m = len of beginWord, and n = len of wordList
        Space: O(m * n^2), where m = len of beginWord, and n = len of wordList, but realistically O(m*n) because each
        word appears in exactly m patterns.
        Edge: Need to handle the possibility that endWord might not be in the wordList.
        '''
        import collections
        if endWord not in wordList: return 0
        neighbor_dict = collections.defaultdict(list)
        wordList.append(beginWord)
        # This loop time: O(m * n), space: O(m * n)
        for word in wordList:
            for j in range(len(word)):
                pattern = word[:j] + "*" + word[j+1:]
                neighbor_dict[pattern].append(word)
        visited_set = set(beginWord)
        deque = collections.deque([beginWord])
        count = 1
        # This BFS time: O(m^2 * n), Space: O(m).
        # The Outer loop time is O(n) because of the visited_set, the inner loop time is O(m*n)
        while deque:
            for i in range(len(deque)):
                word = deque.popleft()
                if word == endWord: return count
                for j in range(len(word)):
                    pattern = word[:j] + "*" + word[j+1:]
                    for neighbor in neighbor_dict[pattern]:
                        if neighbor not in visited_set:
                            visited_set.add(neighbor)
                            deque.append(neighbor)
            count += 1
        return 0

solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))   # 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))         # 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
