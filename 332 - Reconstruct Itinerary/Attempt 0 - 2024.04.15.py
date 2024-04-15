from typing import List
class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        332 - Reconstruct Itinerary

        https://leetcode.com/problems/reconstruct-itinerary/

        You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the
        arrival airports of one flight. Reconstruct the itinerary in order and return it.

        All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If
        there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
        when read as a single string.

        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
        You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

        Constraints:
        1 <= tickets.length <= 300
        tickets[i].length == 2
        fromi.length == 3
        toi.length == 3
        fromi and toi consist of uppercase English letters.
        fromi != toi

        Plan:
        Graph Traversal with DFS (Hierholzer's Algorithm)
        Time: O(n^2), where n = len of tickets
        Space: O(n), where n = len of tickets
        '''
        import collections
        adj = collections.defaultdict(list)
        final_arr = []

        for src, dst in tickets:
            adj[src].append(dst)

        for key in adj:
            adj[key].sort()

        def dfs(adj, src):
            if src in adj:
                destinations = adj[src][:]
                while destinations:
                    dest = destinations[0]
                    adj[src].pop(0)
                    dfs(adj, dest)
                    destinations = adj[src][:]
            final_arr.append(src)

        dfs(adj, "JFK")
        final_arr.reverse()

        if len(final_arr) != len(tickets) + 1:
            return []

        return final_arr


# Leetcode Solution
# class Solution(object):
#     def findItinerary(self, tickets):
#         """
#         :type tickets: List[List[str]]
#         :rtype: List[str]
#         """
#         from collections import defaultdict
#         self.flightMap = defaultdict(list)
# 
#         for ticket in tickets:
#             origin, dest = ticket[0], ticket[1]
#             self.flightMap[origin].append(dest)
# 
#         # sort the itinerary based on the lexical order
#         for origin, itinerary in self.flightMap.items():
#         # Note that we could have multiple identical flights, i.e. same origin and destination.
#             itinerary.sort(reverse=True)
# 
#         self.result = []
#         self.DFS('JFK')
# 
#         # reconstruct the route backwards
#         return self.result[::-1]
# 
#     def DFS(self, origin):
#         destList = self.flightMap[origin]
#         while destList:
#             #while we visit the edge, we trim it off from graph.
#             nextDest = destList.pop()
#             self.DFS(nextDest)
#         self.result.append(origin)

solution = Solution()
print(solution.findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
# ["JFK","MUC","LHR","SFO","SJC"]

print(solution.findItinerary([["JFK", "SFO"], ["JFK", "ATL"], ["SFO", "ATL"], ["ATL", "JFK"], ["ATL", "SFO"]]))
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"], but it is larger in lexical
# order.
