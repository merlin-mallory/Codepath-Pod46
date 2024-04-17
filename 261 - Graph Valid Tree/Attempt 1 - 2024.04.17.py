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
        Plan:
        Union Find
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        import collections
        if len(edges) != n-1: return False
        adj = collections.defaultdict(list)
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        par = [i for i in range(n)]
        rank = [1] * len(par)

        def find_parent(cur):
            while cur != par[cur]:
                par[cur] = par[par[cur]]
                cur = par[cur]
            return cur

        def union(a,b):
            pa, pb = find_parent(a), find_parent(b)
            if pa == pb: return False
            if rank[pa] >= rank[pb]:
                par[pb] = pa
                rank[pa] += rank[pb]
            else:
                par[pa] = pb
                rank[pb] += rank[pa]
            return True

        for a, b in edges:
            if not union(a,b): return False

        return True



solution = Solution()
print(solution.validTree(5, [[0,1],[0,2],[0,3],[1,4]]))            # True
print(solution.validTree(5, [[0,1],[1,2],[2,3],[1,3],[1,4]]))     # False
