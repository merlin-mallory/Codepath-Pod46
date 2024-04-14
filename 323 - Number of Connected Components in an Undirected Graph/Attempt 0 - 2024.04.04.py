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
        Graph Traversal with DFS
        Time: O(V + E)
        Space: O(V + E)
        Edge: None
        '''
        import collections
        adj_dict = collections.defaultdict(list)
        for a, b in edges:
            adj_dict[a].append(b)
            adj_dict[b].append(a)

        visited_set = set()
        set_count = 0

        def dfs(node):
            stack = [ node ]
            while stack:
                cur = stack.pop()
                for neighbor in adj_dict[cur]:
                    if neighbor not in visited_set:
                        visited_set.add(neighbor)
                        stack.append(neighbor)

        for node in range(n):
            if node not in visited_set:
                visited_set.add(node)
                dfs(node)
                set_count += 1

        return set_count

# DFS recursive alternative
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         '''
#         323 - Number of Connected Components in an Undirected Graph
#
#         https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
#
#         You have a graph of n nodes. You are given an integer n and an array edges where edges[i] = [ai, bi] indicates
#         that there is an edge between ai and bi in the graph.
#
#         Return the number of connected components in the graph.
#
#         Example 1:
#         Input: n = 5, edges = [[0,1],[1,2],[3,4]]
#         Output: 2
#
#         Example 2:
#         Input: n = 5, edges = [[0,1],[1,2],[2,3],[3,4]]
#         Output: 1
#
#         Constraints:
#         1 <= n <= 2000
#         1 <= edges.length <= 5000
#         edges[i].length == 2
#         0 <= ai <= bi < n
#         ai != bi
#         There are no repeated edges.
#         '''
#         import collections
#         adj_dict = collections.defaultdict(list)
#         for a, b in edges:
#             adj_dict[a].append(b)
#             adj_dict[b].append(a)
#
#         visited_set = set()
#         component_count = 0
#
#         def explore(key):
#             if key in visited_set: return False
#             visited_set.add(key)
#             for neighbor in adj_dict[key]:
#                 explore(neighbor)
#             return True
#
#         for key, list_of_neighbors in adj_dict.items():
#             if explore(key): component_count += 1
#
#         for empty_node in range(n):
#             if empty_node not in visited_set:
#                 component_count += 1
#
#         return component_count

# Union Find Solution from Neetcode
# Time: O(V + E)
# Space: O(V)
# class UnionFind:
#     def __init__(self):
#         self.f = {}
#
#     def findParent(self, x):
#         y = self.f.get(x, x)
#         if x != y:
#             y = self.f[x] = self.findParent(y)
#         return y
#
#     def union(self, x, y):
#         self.f[self.findParent(x)] = self.findParent(y)
#
# class Solution:
#     def countComponents(self, n: int, edges: List[List[int]]) -> int:
#         dsu = UnionFind()
#         for a, b in edges:
#             dsu.union(a, b)
#         return len(set(dsu.findParent(x) for x in range(n)))

solution = Solution()
print(solution.countComponents(5, [[0, 1], [1, 2], [3, 4]]))  # 2
print(solution.countComponents(5, [[1, 0], [1, 2], [2, 3], [3, 4]]))  # 1
