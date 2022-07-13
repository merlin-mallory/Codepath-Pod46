# class Solution:
#     def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
#         '''
#         https://leetcode.com/problems/course-schedule/
#
#         There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
#         array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you
#         want to take course ai.
#
#         For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
#         Return true if you can finish all courses. Otherwise, return false.
#
#         Input: numCourses = 2, prerequisites = [[1,0]]
#         Output: true
#         Explanation: There are a total of 2 courses to take.
#         To take course 1 you should have finished course 0. So it is possible.
#
#         Input: numCourses = 2, prerequisites = [[1,0],[0,1]]
#         Output: false Explanation: There are a total of 2
#         courses to take. To take course 1 you should have finished course 0, and to take course 0 you should also
#         have finished course 1. So it is impossible.
#
#         Constraints:
#
#         1 <= numCourses <= 2000
#         0 <= prerequisites.length <= 5000
#         prerequisites[i].length == 2
#         0 <= ai, bi < numCourses
#         All the pairs prerequisites[i] are unique.
#
#         I have no idea how to code this because I don't know if we are assuming that taking course zero is free for
#         everybody. Or if the zero index in numCourses represents course zero.
#         '''
#
#         """
#         :type numCourses: int
#         :type prerequisites: List[List[int]]
#         :rtype: bool
#         """
#         from collections import defaultdict, deque
#         # key: index of node; value: GNode
#         graph = defaultdict(GNode)
#
#         totalDeps = 0
#         for relation in prerequisites:
#             nextCourse, prevCourse = relation[0], relation[1]
#             graph[prevCourse].outNodes.append(nextCourse)
#             graph[nextCourse].inDegrees += 1
#             totalDeps += 1
#
#         # we start from courses that have no prerequisites.
#         # we could use either set, stack or queue to keep track of courses with no dependence.
#         nodepCourses = deque()
#         for index, node in graph.items():
#             if node.inDegrees == 0:
#                 nodepCourses.append(index)
#
#         removedEdges = 0
#         while nodepCourses:
#             # pop out course without dependency
#             course = nodepCourses.pop()
#
#             # remove its outgoing edges one by one
#             for nextCourse in graph[course].outNodes:
#                 graph[nextCourse].inDegrees -= 1
#                 removedEdges += 1
#                 # while removing edges, we might discover new courses with prerequisites removed,
#                 # i.e. new courses without prerequisites.
#                 if graph[nextCourse].inDegrees == 0:
#                     nodepCourses.append(nextCourse)
#
#         if removedEdges == totalDeps:
#             return True
#         else:
#             # if there are still some edges left, then there exist some cycles
#             # Due to the dead-lock (dependencies), we cannot remove the cyclic edges
#             return False
#
# class GNode(object):
#     """  data structure represent a vertex in the graph."""
#     def __init__(self):
#         self.inDegrees = 0
#         self.outNodes = []

def canFinish(self, n, prerequisites):
        G = [[] for i in range(n)]
        degree = [0] * n
        for j, i in prerequisites:
            G[i].append(j)
            degree[j] += 1
        bfs = [i for i in range(n) if degree[i] == 0]
        for i in bfs:
            for j in G[i]:
                degree[j] -= 1
                if degree[j] == 0:
                    bfs.append(j)
        return len(bfs) == n
