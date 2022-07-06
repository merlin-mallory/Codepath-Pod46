class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        '''
        https://leetcode.com/problems/word-ladder/ A transformation sequence from word beginWord to word endWord
        using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList.
        Note that beginWord does not need to be in wordList. sk == endWord Given two words, beginWord and endWord,
        and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord
        to endWord, or 0 if no such sequence exists.

        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log","cog"]
        Output: 5
        Explanation: One shortest transformation sequence is "hit" -> "hot" -> "dot" -> "dog" -> cog", which is 5
        words long.

        Input: beginWord = "hit", endWord = "cog", wordList = ["hot","dot","dog","lot","log"]
        Output: 0
        Explanation: The endWord "cog" is not in wordList, therefore there is no valid transformation sequence.

        Constraints:
        1 <= beginWord.length <= 10
        endWord.length == beginWord.length
        1 <= wordList.length <= 5000
        wordList[i].length == beginWord.length
        beginWord, endWord, and wordList[i] consist of lowercase English letters.
        beginWord != endWord
        All the words in wordList are unique.

        Plan:
        1. It looks like the word length and list length is small enough that we can do BFS to generate all possible
        substrings, and if a result is found, return it immediately. However we will need to explore the entire tree
        in order to be sure that a solution does not exist.
        2. We will create an array of all lower case letters, and loop through each character of the current string
        to see if there exists a matching word in the dictionary. If a match is found, then we will enqueue the
        substring. We'll keep going until we explore the entire dictionary, which will be the length of the
        dictionary's keys. If we reach the end of that loop, then we've verified that the transformation sequence
        does not exist in the dictionary.
        3. We know that the shortest sequence will not contain any duplicates, so we'll need to check for duplicates
        before adding new elements to substrings.

        I'm not confident in this plan, so skipping to solution.
        '''

        from collections import defaultdict

        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList or not endWord or not beginWord or not wordList:
            return 0

        # Since all words are of same length.
        L = len(beginWord)

        # Dictionary to hold combination of words that can be formed,
        # from any given word. By changing one letter at a time.
        all_combo_dict = defaultdict(list)
        for word in wordList:
            for i in range(L):
                # Key is the generic word
                # Value is a list of words which have the same intermediate generic word.
                all_combo_dict[word[:i] + "*" + word[i + 1:]].append(word)

        # Queue for BFS
        queue = collections.deque([(beginWord, 1)])
        # Visited to make sure we don't repeat processing same word.
        visited = {beginWord: True}
        while queue:
            current_word, level = queue.popleft()
            for i in range(L):
                # Intermediate words for current word
                intermediate_word = current_word[:i] + "*" + current_word[i + 1:]

                # Next states are all the words which share the same intermediate state.
                for word in all_combo_dict[intermediate_word]:
                    # If at any point if we find what we are looking for
                    # i.e. the end word - we can return with the answer.
                    if word == endWord:
                        return level + 1
                    # Otherwise, add it to the BFS Queue. Also mark it visited
                    if word not in visited:
                        visited[word] = True
                        queue.append((word, level + 1))
                all_combo_dict[intermediate_word] = []

        return 0
