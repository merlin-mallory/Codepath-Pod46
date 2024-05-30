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
        Time: O(w * n^2), where w = len(wordList) and n = len(wordList[0]) Both building the pattern dict and BFS
        processing follow this.
        Space: O(w * n^2), for the pattern dictionary. Worst case is w * n^2 patterns. Deque and visited_set ore O(w)
        Edge: beginWord and endWord might not be in wordList
        '''
        import collections
        pattern_dict = collections.defaultdict(list)
        if endWord not in wordList: return 0
        wordList.append(beginWord)
        for word in wordList:
            for i in range(len(word)):
                pattern = word[:i] + "*" + word[i+1:]
                pattern_dict[pattern].append(word)
        deque = collections.deque([beginWord])
        visited_set = set()
        time = 1
        while deque:
            for _ in range(len(deque)):
                cur_word = deque.popleft()
                if cur_word in visited_set: continue
                if cur_word == endWord: return time
                visited_set.add(cur_word)
                for i in range(len(cur_word)):
                    pattern = cur_word[:i] + "*" + cur_word[i+1:]
                    for neighbor in pattern_dict[pattern]:
                        if neighbor not in pattern_dict:
                            deque.append(neighbor)
            time += 1
        return 0




solution = Solution()
print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log","cog"]))   # 5
# Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5 words long.

print(solution.ladderLength("hit", "cog", ["hot","dot","dog","lot","log"]))         # 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

print(solution.ladderLength("hot", "dog", ["hot","dog"]))                           # 0
# Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.
