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
        Graph traversal with DFS
        Time: O(m*n)
        Space: O(m*n)
        Edge: None
        '''
        rows, cols = len(grid), len(grid[0])
        visited_set = set()
        max_area = [0]

        def explore(r,c):
            if (r < 0) or (c < 0) or (r == rows) or (c == cols) or ((r,c) in visited_set):
                return 0

            visited_set.add((r,c))

            if grid[r][c] == 0:
                return 0

            return 1 + explore(r+1, c) + explore(r-1, c) + explore(r, c+1) + explore(r, c-1)

        for r in range(rows):
            for c in range(cols):
                cur_area = explore(r,c)
                max_area[0] = max(max_area[0], cur_area)

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

grid3 = [
    [1,1,0,0,0],
    [1,1,0,0,0],
    [0,0,0,1,1],
    [0,0,0,1,1]
]
print(solution.maxAreaOfIsland(grid3))   # 4
