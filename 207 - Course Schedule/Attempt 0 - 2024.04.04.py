from typing import List
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        '''
        207 - Course Schedule

        https://leetcode.com/problems/course-schedule/

        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an
        array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you
        want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.
        Return true if you can finish all courses. Otherwise, return false.

        Constraints:
        1 <= numCourses <= 2000
        0 <= prerequisites.length <= 5000
        prerequisites[i].length == 2
        0 <= ai, bi < numCourses
        All the pairs prerequisites[i] are unique.
        '''
        import collections
        prereq_dict = collections.defaultdict(list)
        for course, prereq in prerequisites:
            prereq_dict[course].append(prereq)
        visited_set = set()
        def dfs(course):
            if course in visited_set: return False
            if prereq_dict[course] == []: return True
            visited_set.add(course)
            for prereq in prereq_dict[course]:
                if not dfs(prereq): return False
            visited_set.remove(course)
            prereq_dict[course] = []
            return True

        for course in range(numCourses):
            if not dfs(course): return False
        return True

solution = Solution()

print(solution.canFinish(2, [[1, 0]]))  # True
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0. So it is
# possible.

print(solution.canFinish(2, [[1, 0], [0, 1]]))  # False
# Explanation: There are a total of 2 courses to take. To take course 1 you should have finished course 0,
# and to take course 0 you should also have finished course 1. So it is impossible.

print(solution.canFinish(5,[[0,1],[0,2],[1,3],[1,4],[3,4]]))  # True
# Explanation: There isn't a cycle in this dict, so the answer is True
