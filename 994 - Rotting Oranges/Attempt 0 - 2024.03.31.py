from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """
        https://leetcode.com/problems/rotting-oranges/

        You are given an m x n grid where each cell can have one of three values:

        0 representing an empty cell,
        1 representing a fresh orange, or
        2 representing a rotten orange.
        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is
        impossible, return -1.

        Input: grid = [[2,1,1],[1,1,0],[0,1,1]]
        Output: 4

        Input: grid = [[2,1,1],[0,1,1],[1,0,1]] Output: -1 Explanation: The orange in the bottom left corner (row 2,
        column 0) is never rotten, because rotting only happens 4-directionally.

        Input: grid = [[0,2]]
        Output: 0
        Explanation: Since there are already no fresh oranges at minute 0, the answer is just 0.

        Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 10
        grid[i][j] is 0, 1, or 2
        Time: O(m*n)
        Space: O(m*n)
        Edge: None
        """
        import collections
        deque = collections.deque()
        time = 0
        rows = len(grid)
        cols = len(grid[0])
        fresh_orange_count = 0

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 1:
                    fresh_orange_count += 1
                elif grid[r][c] == 2:
                    deque.append((r, c))

        while deque and (fresh_orange_count > 0):
            time += 1
            for i in range(len(deque)):
                r, c = deque.popleft()
                grid[r][c] = 2
                adj = [[1, 0], [-1, 0], [0, 1], [0, -1]]
                for rmod, cmod in adj:
                    row, col = r + rmod, c + cmod
                    if (rows > row >= 0) and (cols > col >= 0) and (grid[row][col] == 1):
                        grid[row][col] = 2
                        fresh_orange_count -= 1
                        deque.append((row, col))

        return time if (fresh_orange_count == 0) else -1


solution = Solution()

grid1 = [[2, 1, 1],
         [1, 1, 0],
         [0, 1, 1]]
print(solution.orangesRotting(grid1))  # 4

grid2 = [[2, 1, 1],
         [0, 1, 1],
         [1, 0, 1]]
print(solution.orangesRotting(grid2))  # -1

grid3 = [[0, 2]]
print(solution.orangesRotting(grid3))  # 0
