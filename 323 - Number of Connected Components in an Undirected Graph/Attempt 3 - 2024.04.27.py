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
        Time: O(E+V)
        Space: O(V)
        Edge: None
        '''
        par = [i for i in range(n)]
        rank = [1] * len(par)
        def find_parent(n1):
            while n1 != par[n1]:
                par[n1] = par[par[n1]]
                n1 = par[n1]
            return n1
        def union(n1,n2):
            p1, p2 = find_parent(n1), find_parent(n2)
            if p1 == p2: return False
            if rank[n1] >= rank[n2]:
                par[n2] = n1
                rank[n1] += rank[n2]
            else:
                par[n1] = n2
                rank[n2] += rank[n1]
            return True
        connected_count = n
        for a,b in edges:
            if union(a,b): connected_count -= 1
        return connected_count



solution = Solution()
print(solution.countComponents(5,[[0,1],[1,2],[3,4]]))        # 2
print(solution.countComponents(5,[[1,0],[1,2],[2,3],[3,4]]))  # 1
