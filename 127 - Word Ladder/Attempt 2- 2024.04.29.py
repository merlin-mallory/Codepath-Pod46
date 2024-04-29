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
        Time: O(w*n*2^n), where w = len of wordList, n = len of max word in wordList
        Space: O(w*n)
        Edge: None
        '''
        import collections
        if endWord not in wordList: return 0

        # Construct pattern_dict
        pattern_dict = collections.defaultdict(list)
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_dict[pattern].append(word)

        # Construct deque, time
        deque = collections.deque([beginWord])
        time = 1
        visited_set = set(beginWord)

        # Loop through deque until endWord is reached, or deque is empty
        while deque:
            for _ in range(len(deque)):
                cur_word = deque.popleft()
                if cur_word == endWord: return time
                for i in range(len(cur_word)):
                    pattern = cur_word[:i] + "*" + cur_word[i+1:]
                    for neighbor in pattern_dict[pattern]:
                        if neighbor not in visited_set:
                            visited_set.add(neighbor)
                            deque.append(neighbor)
            time += 1
        return 0

solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))   # 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))         # 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","cog"]))         # 5

print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))   # 5
