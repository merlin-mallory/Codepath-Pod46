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
        Graph Traversal
        Time: O(m*n)
        Space: O(m*n)
        '''
        rows = len(grid)
        cols = len(grid[0])
        visited_set = set()
        island_count = 0
        def backtrack(r,c):
            if (
                r < 0 or c < 0 or r >= rows or c >= cols or
                (r,c) in visited_set or grid[r][c] == "0"
            ):
                return False
            visited_set.add((r,c))
            backtrack(r, c+1)
            backtrack(r, c-1)
            backtrack(r+1, c)
            backtrack(r-1, c)
            return True
        for r in range(rows):
            for c in range(cols):
                if backtrack(r,c):
                    island_count += 1
        return island_count


# BFS solution
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0

        islands = 0
        visit = set()
        rows, cols = len(grid), len(grid[0])

        def dfs(r, c):
            if (
                    r not in range(rows)
                    or c not in range(cols)
                    or grid[r][c] == "0"
                    or (r, c) in visit
            ):
                return

            visit.add((r, c))
            directions = [[0, 1], [0, -1], [1, 0], [-1, 0]]
            for dr, dc in directions:
                dfs(r + dr, c + dc)

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == "1" and (r, c) not in visit:
                    islands += 1
                    dfs(r, c)
        return islands


# BFS Solution from Neetcode
# class SolutionBFS:
#     def numIslands(self, grid: List[List[str]]) -> int:
#         if not grid:
#             return 0
#
#         rows, cols = len(grid), len(grid[0])
#         visited = set()
#         islands = 0
#
#         def bfs(r, c):
#             q = deque()
#             visited.add((r, c))
#             q.append((r, c))
#
#             while q:
#                 row, col = q.popleft()
#                 directions = [[1, 0], [-1, 0], [0, 1], [0, -1]]
#
#                 for dr, dc in directions:
#                     r, c = row + dr, col + dc
#                     if (r) in range(rows) and (c) in range(cols) and grid[r][c] == '1' and (r, c) not in visited:
#                         q.append((r, c))
#                         visited.add((r, c))
#
#         for r in range(rows):
#             for c in range(cols):
#
#                 if grid[r][c] == "1" and (r, c) not in visited:
#                     bfs(r, c)
#                     islands += 1
#
#         return islands


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

grid3 = [
    ["1","1","1","1","1","1"],
    ["1","0","0","0","0","1"],
    ["1","0","1","1","0","1"],
    ["1","0","0","0","0","1"],
    ["1","1","1","1","1","1"]
]
print(solution.numIslands(grid3))   # 2