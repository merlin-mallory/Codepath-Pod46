from typing import List

class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False
class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        '''
        212 - Word Search II

        https://leetcode.com/problems/word-search-ii/

        Given an m x n board of characters and a list of strings words, return all words on the board.

        Each word must be constructed from letters of sequentially adjacent cells, where adjacent cells are
        horizontally or vertically neighboring. The same letter cell may not be used more than once in a word.

        Example 1:
        Input: board = [["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
        words = ["oath","pea","eat","rain"]
        Output: ["eat","oath"]

        Example 2:
        Input: board = [["a","b"],["c","d"]], words = ["abcb"]
        Output: []

        Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 12
        board[i][j] is a lowercase English letter.
        1 <= words.length <= 3 * 104
        1 <= words[i].length <= 10
        words[i] consists of lowercase English letters.
        All the strings of words are unique.

        Plan:
        Backtracking with Trie
        Time: O(4^n), where n = max len of word in words
        '''
        final_set = set()
        root = TrieNode()
        for word in words:
            cur = root
            for c in word:
                if c not in cur.children:
                    cur.children[c] = TrieNode()
                cur = cur.children[c]
            cur.is_end = True

        def search(r,c,word,node):
            if (r < 0) or (c < 0) or (r >= rows) or (c >= cols) or ((r,c) in visited_set) or (board[r][c] not in
                                                                                      node.children):
                return
            visited_set.add((r,c))
            word += board[r][c]
            node = node.children[board[r][c]]
            if node.is_end: final_set.add(word)
            search(r+1,c,word,node)
            search(r-1,c,word,node)
            search(r,c+1,word,node)
            search(r,c-1,word,node)
            visited_set.remove((r,c))

        rows, cols = len(board), len(board[0])
        visited_set = set()
        for r in range(rows):
            for c in range(cols):
                search(r,c,"", root)

        return list(final_set)

solution = Solution()
print(solution.findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]],
                         ["oath","pea","eat","rain"]))
# ["eat","oath"]

print(solution.findWords([["a","b"],["c","d"]], ["abcb"]))
# []

print(solution.findWords(
[
    ["o","a","b","n"],
    ["o","t","a","e"],
    ["a","h","k","r"],
    ["a","f","l","v"]
], ["oa","oaa"]))
# ["oa", "oaa"]
