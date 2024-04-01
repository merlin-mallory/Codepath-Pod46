from typing import List
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        286 - Walls and Gates

        https://leetcode.com/problems/walls-and-gates/

        You are given an m x n grid rooms initialized with these three possible values.

            -1: A wall or an obstacle.

            0: A gate.

            INF: Infinity means an empty room. We use the value 231 - 1 = 2147483647 to represent INF as you may
            assume that the distance to a gate is less than 2147483647.

        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a gate, it should be
        filled with INF.

        Constraints:
        m == rooms.length
        n == rooms[i].length
        1 <= m, n <= 250
        rooms[i][j] is -1, 0, or 2^31 - 1.

        Do not return anything, modify rooms in-place instead.
        """
        import collections
        deque = collections.deque()
        rows = len(rooms)
        cols = len(rooms[0])
        INF = 2147483647

        for r in range(rows):
            for c in range(cols):
                if rooms[r][c] == 0:
                    deque.append((r,c,0))

        while deque:
            r, c, dist = deque.popleft()
            adj = [(1,0), (-1,0), (0,1), (0,-1)]
            for ar, ac in adj:
                nr, nc = r+ar, c+ac
                if (nr >= 0) and (nc >= 0) and (nr < rows) and (nc < cols) and rooms[nr][nc] == INF:
                    rooms[nr][nc] = dist + 1
                    deque.append((nr, nc, dist + 1))



solution = Solution()

grid1 = [[2147483647,-1,0,2147483647],
         [2147483647,2147483647,2147483647,-1],
         [2147483647,-1,2147483647,-1],
         [0,-1,2147483647,2147483647]]
solution.wallsAndGates(grid1)
print(grid1)
# [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]

grid2 = [[-1]]
solution.wallsAndGates(grid2)
print(grid2)
# [[-1]]
