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

        Plan:
        1. Create fresh_set and rotten_set. (m, n) tuples.
        2. While len(rotten_set) is increasing:
            3. If fresh_set adjacent to rotten_set:
                4. delete fresh_set(i), add rotten_set(i)
            5. counter++
            6. Return counter
        """

        queue = deque()

        # Step 1). build the initial set of rotten oranges
        fresh_oranges = 0
        ROWS, COLS = len(grid), len(grid[0])
        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == 2:
                    queue.append((r, c))
                elif grid[r][c] == 1:
                    fresh_oranges += 1

        # Mark the round / level, _i.e_ the ticker of timestamp
        queue.append((-1, -1))

        # Step 2). start the rotting process via BFS
        minutes_elapsed = -1
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        while queue:
            row, col = queue.popleft()
            if row == -1:
                # We finish one round of processing
                minutes_elapsed += 1
                if queue:  # to avoid the endless loop
                    queue.append((-1, -1))
            else:
                # this is a rotten orange
                # then it would contaminate its neighbors
                for d in directions:
                    neighbor_row, neighbor_col = row + d[0], col + d[1]
                    if ROWS > neighbor_row >= 0 and COLS > neighbor_col >= 0:
                        if grid[neighbor_row][neighbor_col] == 1:
                            # this orange would be contaminated
                            grid[neighbor_row][neighbor_col] = 2
                            fresh_oranges -= 1
                            # this orange would then contaminate other oranges
                            queue.append((neighbor_row, neighbor_col))

        # return elapsed minutes if no fresh orange left
        return minutes_elapsed if fresh_oranges == 0 else -1

        # fresh_set = set()
        # rotten_set = set()
        #
        # for m in range(len(grid)):
        #     for n in range(len(grid[0])):
        #         if grid[m][n] == 1:
        #             fresh_set.add((m,n))
        #         elif grid[m][n] == 2:
        #             rotten_set.add((m,n))
        #
        # print("start:", fresh_set, rotten_set)
        # rotten_increasing = True
        # counter = 0
        #
        # if len(fresh_set) == 0:
        #     return -1
        #
        # while rotten_increasing is True:
        #     rotten_increasing = False
        #     for freshfruit in fresh_set:
        #         freshm, freshn = freshfruit
        #         for rottenfruit in rotten_set:
        #             rottenm, rottenn = rottenfruit
        #
        #             if (freshm+1 == rottenm and freshn == rottenn) or (freshm-1 == rottenm and freshn == rottenn) \
        #                     or (freshm == rottenm and freshn+1 == rottenn) or \
        #                     (freshm == rottenm and freshn-1 == rottenn):
        #                 fresh_set.remove(freshfruit)
        #                 rotten_set.add(freshfruit)
        #                 rotten_increasing = True
        #     counter += 1
        # print(fresh_set, rotten_set)
        # if len(fresh_set) > 0:
        #     return -1
        # else:
        #     return counter

