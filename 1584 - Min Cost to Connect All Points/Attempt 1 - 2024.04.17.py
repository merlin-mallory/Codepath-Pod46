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
        Graph Traversal with Minheap and Prim's Algorithm
        Time: O(n log n)
        Space: O(n)
        Edge: None
        '''



solution = Solution()
print(solution.minCostConnectPoints([[0,0],[2,2],[3,10],[5,2],[7,0]]))
# 20
# Explanation: We can connect the points as shown above to get the minimum cost of 20 Notice that there is a unique
# path between every pair of points.

print(solution.minCostConnectPoints([[3,12],[-2,5],[-4,1]]))
# 18
