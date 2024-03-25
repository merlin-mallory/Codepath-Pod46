from typing import List
class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        '''
        079 - Word Search

        https://leetcode.com/problems/word-search/

        Given an m x n grid of characters board and a string word, return true if word exists in the grid.

        The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally
        or vertically neighboring. The same letter cell may not be used more than once.

        Example 1:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
        Output: true

        Example 2:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
        Output: true

        Example 3:
        Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
        Output: false

        Constraints:
        m == board.length
        n = board[i].length
        1 <= m, n <= 6
        1 <= word.length <= 15
        board and word consists of only lowercase and uppercase English letters.

        Follow up: Could you use search pruning to make your solution faster with a larger board?

        Time: O(m * n * 4^p), where m = # of rows, n = # of columns, and p = len of word
        Space: O(p)
        '''
        rows, cols = len(board), len(board[0])
        path = set()

        def backtrack(r, c, i):
            if i == len(word): return True
            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                word[i] != board[r][c] or
                (r, c) in path):
                return False
            path.add((r, c))
            cur_bool = (backtrack(r+1, c, i+1) or
                        backtrack(r-1, c, i+1) or
                        backtrack(r, c+1, i+1) or
                        backtrack(r, c-1, i+1))
            path.remove((r,c))
            return cur_bool

        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c,0): return True
        return False

result = Solution()
print(result.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCCED"))   # True
print(result.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "SEE"))      # True
print(result.exist([["A", "B", "C", "E"], ["S", "F", "C", "S"], ["A", "D", "E", "E"]], "ABCB"))     # False
