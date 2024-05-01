from typing import List
class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        """
        778 - Swim in Rising Water

        https://leetcode.com/problems/swim-in-rising-water/

        You are given an n x n integer matrix grid where each value grid[i][j] represents the elevation at that point
        (i, j).

        The rain starts to fall. At time t, the depth of the water everywhere is t. You can swim from a square to
        another 4-directionally adjacent square if and only if the elevation of both squares individually are at most t.
        You can swim infinite distances in zero time. Of course, you must stay within the boundaries of the grid during
        your swim.

        Return the least time until you can reach the bottom right square (n - 1, n - 1) if you start at the top left
        square (0, 0).

        Constraints:
        n == grid.length
        n == grid[i].length
        1 <= n <= 50
        0 <= grid[i][j] < n2
        Each value grid[i][j] is unique.

        Plan:
        Graph Traversal with BFS (Dijkstra's Algo)
        Time: O(m*n)
        Space: O(m*n)
        """
        import heapq
        adj = [[1,0],[-1,0],[0,1],[0,-1]]
        minheap = [(grid[0][0], 0, 0)]   # (max_val, r, c)
        visited_set = {(0,0)}  # (r,c)
        n = len(grid)
        while minheap:
            cur_max, old_r, old_c = heapq.heappop(minheap)
            if (old_r == n-1) and (old_c == n-1): return cur_max
            for r_mod, c_mod in adj:
                r = old_r + r_mod
                c = old_c + c_mod
                if (r < 0) or (c < 0) or (r == n) or (c == n) or ((r,c) in visited_set): continue
                visited_set.add((r,c))
                heapq.heappush(minheap, (max(cur_max, grid[r][c]), r, c))


solution = Solution()

print(solution.swimInWater([[0,2],[1,3]]))
# 3
# Explanation:
# At time 0, you are in grid location (0, 0).
# You cannot go anywhere else because 4-directionally adjacent neighbors have a higher elevation than t = 0.
# You cannot reach point (1, 1) until time 3.
# When the depth of water is 3, we can swim anywhere inside the grid.

print(solution.swimInWater([[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]))
# 16
# Explanation: The final route is shown.
#  We need to wait until time 16 so that (0, 0) and (4, 4) are connected.

print(solution.swimInWater([[3,2],[0,1]]))
# 3
