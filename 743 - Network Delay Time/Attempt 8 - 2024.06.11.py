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
        Time: O(E log V), where E = len of times, and V = n
        Space: O(E+V)
        Edge: None, but return -1 if signal cannot clear the graph
        '''
        import collections, heapq
        source_to_dest = collections.defaultdict(list)
        for source, dest, dist in times:
            source_to_dest[source].append((dist, dest))
        minheap = [(0, k)]  # [dist, node]
        visited_set = set()
        while minheap:
            t1, n1 = heapq.heappop(minheap)
            if n1 in visited_set: continue
            visited_set.add(n1)
            if len(visited_set) == n: return t1
            for t2, n2 in source_to_dest[n1]:
                if n2 not in visited_set:
                    heapq.heappush(minheap, (t1+t2, n2))
        return -1

solution = Solution()
print(solution.networkDelayTime( [[2,1,1],[2,3,1],[3,4,1]], 4, 2))  # 2
print(solution.networkDelayTime([[1,2,1]], 2, 1))                   # 1
print(solution.networkDelayTime([[1,2,1]], 2, 2))                   # -1
