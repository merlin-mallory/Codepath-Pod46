from typing import List
def print_board(board: List[List[str]]) -> None:
    for row in board:
        print('["' + '","'.join(row) + '"]')
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        130 - Surrounded Regions

        https://leetcode.com/problems/surrounded-regions/

        Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

        A region is captured by flipping all 'O's into 'X's in that surrounded region.

        Example 1:
        Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
        Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
        Explanation: Notice that an 'O' should not be flipped if:
        - It is on the border, or
        - It is adjacent to an 'O' that should not be flipped.
        The bottom 'O' is on the border, so it is not flipped.
        The other three 'O' form a surrounded region, so they are flipped.

        Example 2:
        Input: board = [["X"]]
        Output: [["X"]]

        Constraints:
        m == board.length
        n == board[i].length
        1 <= m, n <= 200
        board[i][j] is 'X' or 'O'.

        Do not return anything, modify board in-place instead.
        """
        if not board: return
        rows, cols = len(board), len(board[0])

        def explore(r, c):
            if board[r][c] != "O":
                return
            stack = [(r, c)]
            while stack:
                r, c = stack.pop()
                if 0 <= r < rows and 0 <= c < cols and board[r][c] == "O":
                    board[r][c] = "S"  # Mark as safe
                    stack.extend([(r + 1, c), (r - 1, c), (r, c + 1), (r, c - 1)])

        # Start BFS from the borders
        for r in range(rows):
            explore(r, 0)
            explore(r, cols - 1)
        for c in range(cols):
            explore(0, c)
            explore(rows - 1, c)

        # Flip the regions
        for r in range(rows):
            for c in range(cols):
                if board[r][c] == "O":
                    board[r][c] = "X"
                elif board[r][c] == "S":
                    board[r][c] = "O"

# DFS Solution:
# class Solution:
#     def solve(self, board: List[List[str]]) -> None:
#         if not board: return
#         rows = len(board)
#         cols = len(board[0])
#         visited_set = set()
#         def explore(r,c):
#             if (r < 0) or (c < 0) or (r == rows) or (c == cols) or ((r,c) in visited_set) or board[r][c] == "X":
#                 return False
#             visited_set.add((r,c))
#             board[r][c] = "S"
#             explore(r+1,c)
#             explore(r-1,c)
#             explore(r,c+1)
#             explore(r,c-1)
#             return True
#
#         for r in range(rows):
#             explore(r,0)     # Explore left edge
#             explore(r, cols-1)  # Explore right edge
#         for c in range(cols):
#             explore(0, c)    # Explore top edge
#             explore(rows-1, c)  # Explore bottom edge
#
#         for r in range(rows):
#             for c in range(cols):
#                 if board[r][c] == "O": board[r][c] = "X"
#                 elif board[r][c] == "S": board[r][c] = "O"

solution = Solution()

grid1 = [
    ["X","X","X","X"],
    ["X","O","O","X"],
    ["X","X","O","X"],
    ["X","O","X","X"]]
solution.solve(grid1)
print_board(grid1)
# [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]

print("")

grid2 = [
    ["X"]
]
solution.solve(grid2)
print_board(grid2)
# [["X"]]
