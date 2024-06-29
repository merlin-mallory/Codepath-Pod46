from typing import List
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        210 - Course Schedule II

        https://leetcode.com/problems/course-schedule-ii/

        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
        array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want
        to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return the ordering of courses you should take to finish all courses. If there are many valid answers, return
        any of them. If it is impossible to finish all courses, return an empty array.

        Example 3:
        Input: numCourses = 1, prerequisites = []
        Output: [0]

        Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= numCourses * (numCourses - 1)
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        ai != bi
        All the pairs [ai, bi] are distinct.

        Plan:
        Graph Traversal with DFS
        Time: ?
        Space: ?
        Edge: Return [] if it is impossible to finish all courses
        '''
        import collections
        course_to_prereq = collections.defaultdict(list)
        for course, prereq in prerequisites:
            course_to_prereq[course].append(prereq)
        visited_set = set()
        cycle_set = set()
        final_arr = []

        def explore(course):
            if course in visited_set: return True
            if course in cycle_set: return False
            cycle_set.add(course)
            for prereq in course_to_prereq[course]:
                if not explore(prereq): return False
            cycle_set.remove(course)
            visited_set.add(course)
            final_arr.append(course)
            return True

        for i in range(numCourses):
            if not explore(i): return []

        return final_arr



solution = Solution()

print(solution.findOrder(2, [[1, 0]]))
# [0,1]
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0.
# So the correct course order is [0,1].

print(solution.findOrder(4, [[1, 0], [2, 0], [3, 1], [3, 2]]))
# [0,2,1,3]
# Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both courses 1 and
# 2. Both courses 1 and 2 should be taken after you finished course 0. So one correct course order is [0,1,2,3].
# Another correct ordering is [0,2,1,3].

print(solution.findOrder(1, []))
# [0]

print(solution.findOrder(2, [[0,1],[1,0]]))
# []
