from typing import List
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        '''
        323 - Number of Connected Components in an Undirected Graph

        https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/

        You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates
        that there is an edge between ai and bi in the graph.

        Return the number of connected components in the graph.

        Example 1:
        Input: n = 5, edges = [[0,1],[1,2],[3,4]]
        Output: 2

        Example 2:
        Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
        Output: 1

        Constraints:
        1 <= n <= 2000
        1 <= edges.length <= 5000
        edges[i].length == 2
        0 <= ai <= bi < n
        ai != bi
        There are no repeated edges.

        Plan:
        Union Find
        Time: O(E log V), where E = len(edges) and V = n
        Space: O(V)
        Edge: None
        '''
        component_count = n
        par = [n for n in range(n)]
        rank = [1] * len(par)
        def findParent(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        def union(n1, n2):
            p1, p2 = findParent(n1), findParent(n2)
            if p1 == p2: return False
            if rank[p1] >= rank[p2]:
                par[p2] = p1
                rank[p1] += rank[p2]
            else:
                par[p1] = p2
                rank[p2] += rank[p1]
            return True
        for n1, n2 in edges:
            if union(n1, n2): component_count -= 1
        return component_count



solution = Solution()
print(solution.countComponents(5,[[0,1],[1,2],[3,4]]))        # 2
print(solution.countComponents(5,[[1,0],[1,2],[2,3],[3,4]]))  # 1
