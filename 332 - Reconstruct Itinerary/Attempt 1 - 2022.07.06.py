class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        '''
        https://leetcode.com/problems/reconstruct-itinerary/

        You are given a list of airline tickets where tickets[i] = [fromi, toi] represent the departure and the
        arrival airports of one flight. Reconstruct the itinerary in order and return it.

        All of the tickets belong to a man who departs from "JFK", thus, the itinerary must begin with "JFK". If
        there are multiple valid itineraries, you should return the itinerary that has the smallest lexical order
        when read as a single string.

        For example, the itinerary ["JFK", "LGA"] has a smaller lexical order than ["JFK", "LGB"].
        You may assume all tickets form at least one valid itinerary. You must use all the tickets once and only once.

        Input: tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
        Output: ["JFK","MUC","LHR","SFO","SJC"]

        Input: tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
        Output: ["JFK",
        "ATL","JFK","SFO","ATL","SFO"]
        Explanation: Another possible reconstruction is ["JFK","SFO","ATL","JFK",
        "ATL","SFO"] but it is larger in lexical order.

        Constraints:
        1 <= tickets.length <= 300
        tickets[i].length == 2
        fromi.length == 3
        toi.length == 3
        fromi and toi consist of uppercase English letters.
        fromi != toi

        Plan:
        1. Create a mapping dictionary, outgoing_dict. Keys = Airport codes, values = list of tickets leaving that node.
        2. Loop through tickets and construct the dictionary.
        3. Use DFS to generate all legal substrings.
        4. Start at the JFK node. Pop the stack. Check if each neighbor's tickets were already used. If it hasn't
        been already used, then add a tuple containing (current_path, level) to the stack. If a node doesn't have any
        outgoing neighbors that have not been used, then backtrack. If len(current_substring) = len(tickets) after
        adding, then we've found a valid solution, so append it to a final_array.
        5. Loop until level = len(tickets). Then sort the final results in ascending order to get the desired output.

        Not confident in solution, skipping to answer
        '''

        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict
        self.flightMap = defaultdict(list)

        for ticket in tickets:
            origin, dest = ticket[0], ticket[1]
            self.flightMap[origin].append(dest)

        self.visitBitmap = {}

        # sort the itinerary based on the lexical order
        for origin, itinerary in self.flightMap.items():
            # Note that we could have multiple identical flights, i.e. same origin and destination.
            itinerary.sort()
            self.visitBitmap[origin] = [False] * len(itinerary)

        self.flights = len(tickets)
        self.result = []
        route = ['JFK']
        self.backtracking('JFK', route)

        return self.result

    def backtracking(self, origin, route):
        if len(route) == self.flights + 1:
            self.result = route
            return True

        for i, nextDest in enumerate(self.flightMap[origin]):
            if not self.visitBitmap[origin][i]:
                # mark the visit before the next recursion
                self.visitBitmap[origin][i] = True
                ret = self.backtracking(nextDest, route + [nextDest])
                self.visitBitmap[origin][i] = False
                if ret:
                    return True

        return False
