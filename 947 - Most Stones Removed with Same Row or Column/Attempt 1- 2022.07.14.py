class Solution:
    def removeStones(self, stones: List[List[int]]) -> int:
        """
        On a 2D plane, we place n stones at some integer coordinate points. Each coordinate point may have at most
        one stone.

        A stone can be removed if it shares either the same row or the same column as another stone that has not been
        removed.

        Given an array stones of length n where stones[i] = [xi, yi] represents the location of the ith stone,
        return the largest possible number of stones that can be removed.

        Input: stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
        Output: 5
        Explanation: One way to remove 5 stones is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,1].
        2. Remove stone [2,1] because it shares the same column as [0,1].
        3. Remove stone [1,2] because it shares the same row as [1,0].
        4. Remove stone [1,0] because it shares the same column as [0,0].
        5. Remove stone [0,1] because it shares the same row as [0,0].
        Stone [0,0] cannot be removed since it does not share a row/column with another stone still on the plane.
        Example 2:

        Input: stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
        Output: 3
        Explanation: One way to make 3 moves is as follows:
        1. Remove stone [2,2] because it shares the same row as [2,0].
        2. Remove stone [2,0] because it shares the same column as [0,0].
        3. Remove stone [0,2] because it shares the same row as [0,0]. Stones [0,0] and [1,
        1] cannot be removed since they do not share a row/column with another stone still on the plane.

        Input: stones = [[0,0]]
        Output: 0
        Explanation: [0,0] is the only stone on the plane, so you cannot remove it.

        Constraints:
        1 <= stones.length <= 1000
        0 <= xi, yi <= 10^4
        No two stones are at the same coordinate point.

        Too hard, skipping for now.
        """
        # DFS Answer
        def dfs(i, j):
            points.discard((i, j))
            for y in rows[i]:
                if (i, y) in points:
                    dfs(i, y)
            for x in cols[j]:
                if (x, j) in points:
                    dfs(x, j)

        points, island, rows, cols = {(i, j) for i, j in stones}, 0, collections.defaultdict(
            list), collections.defaultdict(list)
        for i, j in stones:
            rows[i].append(j)
            cols[j].append(i)
        for i, j in stones:
            if (i, j) in points:
                dfs(i, j)
                island += 1
        return len(stones) - island

        # Union find answer
        # uf = {}
        #
        # def find(x):
        #     if x != uf.setdefault(x, x):
        #         uf[x] = find(uf[x])
        #     return uf[x]
        #
        # for i, j in stones:
        #     uf[find(i)] = find(~j)
        # return len(stones) - len({find(x) for x in uf})
