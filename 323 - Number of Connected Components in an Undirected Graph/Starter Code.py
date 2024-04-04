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

        Time: O(V + E)
        Space: O(V + E)
        Edge: None
        '''
        import collections
        adj_dict = collections.defaultdict(list)
        for a,b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)
        visited_set = set()
        set_count = 0
        def dfs(key):
            if key in visited_set: return
            visited_set.add(key)
            for neighbor in adj_dict[key]:
                dfs(neighbor)

        for node in range(n):
            if node not in visited_set:
                dfs(node)
                set_count += 1

        return set_count


solution = Solution()
print(solution.countComponents(5,[[0,1],[1,2],[3,4]]))        # 2
print(solution.countComponents(5,[[1,0],[1,2],[2,3],[3,4]]))  # 1
