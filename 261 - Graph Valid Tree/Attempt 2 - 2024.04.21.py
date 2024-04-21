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

        Valid Tree needs to be:
        1. Connected
        2. No cycles

        Plan:
        Union Find
        Time: O(V+E)
        Space: O(V)
        Edge: None
        '''
        if len(edges) != n-1: return False
        par = [i for i in range(n+1)]
        rank = [1] * len(par)
        def find_parent(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1

        def union(n1, n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2: return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True

        for n1, n2 in edges:
            if not union(n1, n2): return False

        return True


solution = Solution()
print(solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))            # True
print(solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))     # False
