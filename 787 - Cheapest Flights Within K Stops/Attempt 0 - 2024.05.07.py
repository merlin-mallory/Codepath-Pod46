from typing import List
class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        '''
        787 - Cheapest Flights Within K Stops

        https://leetcode.com/problems/cheapest-flights-within-k-stops/

        There are n cities connected by some number of flights. You are given an array flights where
        flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.

        You are also given three integers src, dst, and k, return the cheapest price from src to dst with
        at most k stops. If there is no such route, return -1.

        Constraints:
        1 <= n <= 100
        0 <= flights.length <= (n * (n - 1) / 2)
        flights[i].length == 3
        0 <= fromi, toi < n
        fromi != toi
        1 <= pricei <= 104
        There will not be any multiple flights between two cities.
        0 <= src, dst, k < n
        src != dst

        Plan:
        Graph Traversal with BFS (Bellman-Ford Algo)
        Time: O(k*E), where k = k, and E = len of flights
        Space: O(n), where n = n
        Edge: None
        '''
        prices = [float("inf")] * n
        prices[src] = 0
        for i in range(k+1):
            temp_prices = prices[:]
            for source, dest, edge_price in flights:
                if prices[source] == float("inf"): continue
                if prices[source] + edge_price < temp_prices[dest]:
                    temp_prices[dest] = prices[source] + edge_price
            prices = temp_prices
        return prices[dst] if prices[dst] != float("inf") else -1

solution = Solution()

print(solution.findCheapestPrice(4, [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], 0, 3,1))
# 700
# Explanation: The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
# Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2,1))
# 200
# Explanation: The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

print(solution.findCheapestPrice(3, [[0,1,100],[1,2,100],[0,2,500]], 0, 2,1))
# 200
# Explanation: The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.
