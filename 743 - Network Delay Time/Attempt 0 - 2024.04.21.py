from typing import List
class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        '''
        743 - Network Delay Time

        https://leetcode.com/problems/network-delay-time/

        You are given a network of n nodes, labeled from 1 to n. You are also given times, a list of travel times as
        directed edges times[i] = (ui, vi, wi), where ui is the source node, vi is the target node, and wi is the time
        it takes for a signal to travel from source to target.

        We will send a signal from a given node k. Return the minimum time it takes for all the n nodes to receive the
        signal. If it is impossible for all the n nodes to receive the signal, return -1.

        Constraints:
        1 <= k <= n <= 100
        1 <= times.length <= 6000
        times[i].length == 3
        1 <= ui, vi <= n
        ui != vi
        0 <= wi <= 100
        All the pairs (ui, vi) are unique. (i.e., no multiple edges.)

        Plan:
        Graph Traversal with BFS (Dijkstra's Algo)
        Time: O(E log V)
        Space: Technically O(V+E), but number of edges dominates because of constraints, so O(E)
        Edge: None
        '''
        import collections, heapq
        source_to_dest = collections.defaultdict(list)
        for source, dest, time in times:
            source_to_dest[source].append((time, dest))
        minheap = [(0, k)] # (time, node)
        visited_set = set()
        total_time = 0
        while minheap:
            t1, n1 = heapq.heappop(minheap)
            if n1 in visited_set: continue
            visited_set.add(n1)
            total_time = t1

            for t2, n2 in source_to_dest[n1]:
                if n2 not in visited_set:
                    heapq.heappush(minheap, (t1 + t2, n2))
        return total_time if (len(visited_set) == n) else -1

# ChatGPT Solution
# class Solution:
#     def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
#         '''
#         Plan:
#         Graph Traversal with BFS (Dijkstra's Algo)
#         Time: O(E log E)
#         Space: Technically O(V+E), but number of edges dominates because of constraints, so O(E)
#         Edge: None
#         '''
#         import collections, heapq
#         source_to_dest = collections.defaultdict(list)
#         for source, dest, time in times:
#             source_to_dest[source].append((time, dest))
#         minheap = [(0, k)] # (time, node)
#         visited_dict = {}
#         while minheap:
#             time, node = heapq.heappop(minheap)
#             if node not in visited_dict:
#                 visited_dict[node] = time
#                 for time2, dest2 in source_to_dest[node]:
#                     if dest2 not in visited_dict:
#                         heapq.heappush(minheap, (time + time2, dest2))
#         if len(visited_dict) == n:
#             return max(visited_dict.values())
#         else:
#             return -1

solution = Solution()
print(solution.networkDelayTime( [[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
print(solution.networkDelayTime([[1,2,1]], 2, 1))                   # 1
print(solution.networkDelayTime([[1,2,1]], 2, 2))                   # -1
