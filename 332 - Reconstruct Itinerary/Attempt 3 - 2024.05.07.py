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
        Graph Traversal with DFS (Hierholzer's Algo)
        Time: O(n log n)
        Space: O(n)
        Edge: None
        '''
        import collections
        source_to_dest = collections.defaultdict(list)
        for source, dest in tickets:
            source_to_dest[source].append(dest)
        for key, list_of_dests in source_to_dest.items():
            list_of_dests.sort(reverse=True)
        stack = ["JFK"]
        path = []
        while stack:
            while source_to_dest[stack[-1]]:
                next_dest = source_to_dest[stack[-1]].pop()
                stack.append(next_dest)
            path.append(stack.pop())
        return path[::-1]

solution = Solution()
print(solution.findItinerary([["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]))
# ["JFK","MUC","LHR","SFO","SJC"]

print(solution.findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
# ["JFK","ATL","JFK","SFO","ATL","SFO"]
# Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK","ATL","SFO"], but it is larger in lexical
# order.
