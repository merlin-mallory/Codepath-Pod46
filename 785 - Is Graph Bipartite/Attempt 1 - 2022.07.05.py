class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        '''
        https://leetcode.com/problems/is-graph-bipartite/description/

        There is an undirected graph with n nodes,
        where each node is numbered between 0 and n - 1. You are given a 2D array graph, where graph[u] is an array
        of nodes that node u is adjacent to. More formally, for each v in graph[u], there is an undirected edge
        between node u and node v. The graph has the following properties:

        There are no self-edges (graph[u] does not contain u). There are no parallel edges (graph[u] does not contain
        duplicate values). If v is in graph[u], then u is in graph[v] (the graph is undirected). The graph may not be
        connected, meaning there may be two nodes u and v such that there is no path between them. A graph is
        bipartite if the nodes can be partitioned into two independent sets A and B such that every edge in the graph
        connects a node in set A and a node in set B.

        Return true if and only if it is bipartite.

        Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
        Output: false Explanation: There is no way to partition the
        nodes into two independent sets such that every edge connects a node in one and a node in the other.

        Input: graph = [[1,3],[0,2],[1,3],[0,2]]
        Output: true
        Explanation: We can partition the nodes into two sets: {0, 2} and {1, 3}.

        Constraints:

        graph.length == n
        1 <= n <= 100
        0 <= graph[u].length < n
        0 <= graph[u][i] <= n - 1
        graph[u] does not contain u.
        All the values of graph[u] are unique.
        If graph[u] contains v, then graph[v] contains u.

        Plan:
        1. Set A = vertex 0, Set B = empty
        2. Add vertex 0's neighbors to set A
        3. Loop through vertex 0's neighbors
            4. If neighbor's neighbor is in set A, then continue.
            5. If neighbor's neighbor is not in set A, and set B is empty, then add the neighbor's neighbor to set B,
                and continue.
            6. If neighbor's neighbor is not in set A, and set B is not empty, then check if neighbor's neighbor is
            connected to set B. If it's connected, then add neighbor's neighbor to set B. Otherwise, return False.
        7. If we finish the loop and have not returned false, then we check each element in A to see that it's not in
            B, and every element in B that it's not in A. If there's ever a mismatch, return False. Otherwise,
            return True.

        Not confident in this plan, going to skip implementation
        '''

        color = {}
        for node in range(len(graph)):
            if node not in color:
                stack = [node]
                color[node] = 0
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if nei not in color:
                            stack.append(nei)
                            color[nei] = color[node] ^ 1
                        elif color[nei] == color[node]:
                            return False
        return True