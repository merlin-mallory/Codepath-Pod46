from typing import List
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        '''
        200 - Number of Islands

        https://leetcode.com/problems/number-of-islands/

        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number
        of islands.

        An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You
        may assume all four edges of the grid are all surrounded by water.

        Constraints:
        m == grid.length
        n == grid[i].length
        1 <= m, n <= 300
        grid[i][j] is '0' or '1'.

        Plan:
        Graph Traversal with DFS
        Time: O(m*n)
        Space: O(m*n)
        Edge: None
        '''
        rows, cols = len(grid), len(grid[0])
        visited_set = set()
        island_count = 0
        def explore(r,c):
            if (r < 0) or (c < 0) or (r == rows) or (c == cols) or ((r,c) in visited_set) or (grid[r][c] == '0'):
                return False
            visited_set.add((r,c))
            explore(r+1,c)
            explore(r-1,c)
            explore(r,c+1)
            explore(r,c-1)
            return True
        for r in range(rows):
            for c in range(cols):
                if (r,c) not in visited_set:
                    if explore(r,c): island_count += 1
        return island_count


solution = Solution()

grid1 = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
print(solution.numIslands(grid1))   # 1

grid2 = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(solution.numIslands(grid2))   # 3
