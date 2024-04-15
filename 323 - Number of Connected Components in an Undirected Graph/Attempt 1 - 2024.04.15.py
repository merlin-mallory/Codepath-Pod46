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

        Time:
        Graph Traversal DFS
        Time: O(V+E)
        Space: O(V+E)
        Edge: None
        '''
        import collections
        dict = collections.defaultdict(list)
        for a, b in edges:
            dict[a].append(b)
            dict[b].append(a)
        component_count = 0
        visited_set = set()
        def explore(key):
            if key in visited_set:
                return False
            visited_set.add(key)
            for neighbor in dict[key]:
                explore(neighbor)
            return True

        for i in range(n):
            if explore(i): component_count += 1

        return component_count



solution = Solution()
print(solution.countComponents(5,[[0,1],[1,2],[3,4]]))        # 2
print(solution.countComponents(5,[[1,0],[1,2],[2,3],[3,4]]))  # 1
