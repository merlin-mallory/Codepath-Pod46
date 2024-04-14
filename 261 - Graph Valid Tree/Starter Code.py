from typing import List
class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        261 - Graph Valid Tree

        https://leetcode.com/problems/graph-valid-tree/

        You have a graph of n nodes labeled from 0 to n - 1. You are given an integer n and a list of edges where
        edges[i] = [ai, bi] indicates that there is an undirected edge between nodes ai and bi in the graph.

        Return true if the edges of the given graph make up a valid tree, and false otherwise.

        Constraints:
        1 <= n <= 2000
        0 <= edges.length <= 5000
        edges[i].length == 2
        0 <= ai, bi < n
        ai != bi
        There are no self-loops or repeated edges.
        '''

solution = Solution()
print(solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))            # True
print(solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))     # False
