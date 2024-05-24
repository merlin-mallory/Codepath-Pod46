from typing import List
class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        '''
        1584 - Min Cost to Connect All Points

        https://leetcode.com/problems/min-cost-to-connect-all-points/

        You are given an array points representing integer coordinates of some points on a 2D-plane, where points[i] =
        [xi, yi].

        The cost of connecting two points [xi, yi] and [xj, yj] is the manhattan distance between them:
        |xi - xj| + |yi - yj|, where |val| denotes the absolute value of val.

        Return the minimum cost to make all points connected. All points are connected if there is exactly one simple
        path between any two points.

        Constraints:
        1 <= points.length <= 1000
        -106 <= xi, yi <= 106
        All pairs (xi, yi) are distinct.

        Plan:
        Graph Traversal with Prim's Algo
        Time: O(n^2 log n)
        Space: O(n)
        '''
        import collections, heapq
        source_to_dest = collections.defaultdict(list)
        for i in range(len(points)):
            x1, y1 = points[i]
            for j in range(i+1, len(points)):
                x2, y2 = points[j]
                dist = abs(x1-x2) + abs(y1-y2)
                source_to_dest[i].append((dist, j))
                source_to_dest[j].append((dist, i))
        minheap = [(0, 0)]
        visited_set = set()
        total_cost = 0
        while minheap:
            t1, p1 = heapq.heappop(minheap)
            if p1 in visited_set: continue
            visited_set.add(p1)
            total_cost += t1
            if len(visited_set) == len(points): return total_cost
            for t2, p2 in source_to_dest[p1]:
                if p2 not in visited_set:
                    heapq.heappush(minheap, (t2, p2))


solution = Solution()
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
# 20
# Explanation: We can connect the points as shown above to get the minimum cost of 20 Notice that there is a unique
# path between every pair of points.

print(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
# 18
