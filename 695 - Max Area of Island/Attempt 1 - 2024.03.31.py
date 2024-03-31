from typing import List
class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        '''
        695 - Max Area of Island

        https://leetcode.com/problems/max-area-of-island/

        You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected
        4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

        The area of an island is the number of cells with a value 1 in the island.

        Return the maximum area of an island in grid. If there is no island, return 0.

        Example 1:
        Input: grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],[0,0,0,0,0,0,0,1,1,1,0,0,0],[0,1,1,0,1,0,0,0,0,0,0,0,0],
        [0,1,0,0,1,1,0,0,1,0,1,0,0],[0,1,0,0,1,1,0,0,1,1,1,0,0],[0,0,0,0,0,0,0,0,0,0,1,0,0],
        [0,0,0,0,0,0,0,1,1,1,0,0,0],[0,0,0,0,0,0,0,1,1,0,0,0,0]]
        Output: 6
        Explanation: The answer is not 11, because the island must be connected 4-directionally.

        Example 2:
        Input: grid = [[0,0,0,0,0,0,0,0]]
        Output: 0

        Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 50
        grid[i][j] is either 0 or 1.

        Plan:
        Backtracking
        Time: O(m*n)
        Space: O(m*n)
        Edge: None
        '''
        rows = len(grid)
        cols = len(grid[0])
        visited_set = set()
        max_area = [0]
        def backtrack(r,c):
            if (r < 0) or (c < 0) or (r == rows) or (c == cols) or ((r,c) in visited_set) or grid[r][c] == 0:
                return 0
            visited_set.add((r,c))
            cur_area = 1 + backtrack(r+1,c) + backtrack(r-1,c) + backtrack(r,c+1) + backtrack(r,c-1)
            max_area[0] = max(max_area[0], cur_area)
            # visited_set.remove((r,c))
            return cur_area
        for r in range(rows):
            for c in range(cols):
                backtrack(r,c)
        return max_area[0]


solution = Solution()

grid1 = [
    [0,0,1,0,0,0,0,1,0,0,0,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,1,1,0,1,0,0,0,0,0,0,0,0],
    [0,1,0,0,1,1,0,0,1,0,1,0,0],
    [0,1,0,0,1,1,0,0,1,1,1,0,0],
    [0,0,0,0,0,0,0,0,0,0,1,0,0],
    [0,0,0,0,0,0,0,1,1,1,0,0,0],
    [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(solution.maxAreaOfIsland(grid1))   # 6

grid2 = [
    [0,0,0,0,0,0,0,0]
]
print(solution.maxAreaOfIsland(grid2))   # 0
