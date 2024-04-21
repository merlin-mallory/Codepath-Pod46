from typing import List
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        '''
        684 - Redundant Connection

        https://leetcode.com/problems/redundant-connection/

        In this problem, a tree is an undirected graph that is connected and has no cycles.

        You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added.
        The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The
        graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge
        between nodes ai and bi in the graph.

        Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple
        answers, return the answer that occurs last in the input.

        Example 1:
        Input: edges = [[1,2],[1,3],[2,3]]
        Output: [2,3]

        Example 2:
        Input: edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
        Output: [1,4]

        Constraints:
        n == edges.length
        3 <= n <= 1000
        edges[i].length == 2
        1 <= ai < bi <= edges.length
        ai != bi
        There are no repeated edges.
        The given graph is connected.

        Plan:
        Union Find
        Time: O(V+E)
        Space: O(V)
        Edge: None
        '''
        par = [i for i in range(len(edges) + 1)]
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
            if not union(n1,n2): return [n1, n2]


solution = Solution()
print(solution.findRedundantConnection([[1,2],[1,3],[2,3]]))                 # [2, 3]
print(solution.findRedundantConnection([[1,2],[2,3],[3,4],[1,4],[1,5]]))     # [1, 4]
