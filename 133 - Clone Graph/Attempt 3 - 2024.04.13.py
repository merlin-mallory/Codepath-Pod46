from typing import Optional, List
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []

def createGraph(adjList):
    if not adjList:
        return None
    nodes = {i: Node(i) for i in range(1, len(adjList) + 1)}
    for i, neighbors in enumerate(adjList, start=1):
        nodes[i].neighbors = [nodes[neigh] for neigh in neighbors]
    return nodes[1]  # Returning the node with val=1 as the starting node

# Helper function to convert the cloned graph to an adjacency list representation for printing
def graphToAdjList(node: Optional['Node']) -> List[List[int]]:
    if not node:
        return []
    nodes = {}
    import collections
    queue = collections.deque([node])
    visited = set()
    while queue:
        cur = queue.popleft()
        if cur.val not in visited:
            visited.add(cur.val)
            nodes[cur.val] = [neighbor.val for neighbor in cur.neighbors]
            for neighbor in cur.neighbors:
                if neighbor.val not in visited:
                    queue.append(neighbor)
    # Convert the dictionary to a list of lists sorted by node value
    return [nodes[i] for i in sorted(nodes)]

from typing import Optional
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        '''
        133 - Clone Graph

        https://leetcode.com/problems/clone-graph/

        Given a reference of a node in a connected undirected graph.

        Return a deep copy (clone) of the graph.

        Each node in the graph contains a value (int) and a list (List[Node]) of its neighbors.

        class Node {
            public int val;
            public List<Node> neighbors;
        }

        Test case format:

        For simplicity, each node's value is the same as the node's index (1-indexed). For example, the first node
        with val == 1, the second node with val == 2, and so on. The graph is represented in the test case using an
        adjacency list.

        An adjacency list is a collection of unordered lists used to represent a finite graph. Each list describes
        the set of neighbors of a node in the graph.

        The given node will always be the first node with val = 1. You must return the copy of the given node as a
        reference to the cloned graph.

        Example 1:
        Input: adjList = [[2,4],[1,3],[2,4],[1,3]]
        Output: [[2,4],[1,3],[2,4],[1,3]]
        Explanation: There are 4 nodes in the graph.
        1st node (val = 1)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        2nd node (val = 2)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).
        3rd node (val = 3)'s neighbors are 2nd node (val = 2) and 4th node (val = 4).
        4th node (val = 4)'s neighbors are 1st node (val = 1) and 3rd node (val = 3).

        Example 2:
        Input: adjList = [[]]
        Output: [[]]
        Explanation: Note that the input contains one empty list. The graph consists of only one node with val = 1 and
        it does not have any neighbors.

        Example 3:
        Input: adjList = []
        Output: []
        Explanation: This an empty graph, it does not have any nodes. So we should just return (not return [])

        Constraints:
        The number of nodes in the graph is in the range [0, 100].
        1 <= Node.val <= 100
        Node.val is unique for each node.
        There are no repeated edges and no self-loops in the graph.
        The Graph is connected and all nodes can be visited starting from the given node.

        Plan:
        Graph Traversal with DFS
        Time: O(V+E)
        Space: O(V)
        Edge: Could be 0 nodes in adjList
        '''
        if not node: return

        old_to_new = {}
        def explore(node):
            if node not in old_to_new:
                old_to_new[node] = Node(node.val)
                for neighbor in node.neighbors:
                    explore(neighbor)

        explore(node)

        for old_node, new_node in old_to_new.items():
            for old_neighbor in old_node.neighbors:
                new_node.neighbors.append(old_to_new[old_neighbor])

        return old_to_new[node]

solution = Solution()

# Example 1
adjList = [[2,4],[1,3],[2,4],[1,3]]
graph = createGraph(adjList)
clonedGraph = solution.cloneGraph(graph)
print(graphToAdjList(clonedGraph))  # [[2,4],[1,3],[2,4],[1,3]]

# Example 2
adjList = [[]]
graph = createGraph(adjList)
clonedGraph = solution.cloneGraph(graph)
print(graphToAdjList(clonedGraph))  # [[]]

# Example 3
adjList = []
graph = createGraph(adjList)
clonedGraph = solution.cloneGraph(graph)
print(graphToAdjList(clonedGraph))  # []
