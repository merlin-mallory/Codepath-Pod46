from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        """
        You are given an array prices where prices[i] is the price of a given stock on the ith day.

        You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the
        future to sell that stock.

        Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

        Input: prices = [7,1,5,3,6,4]
        Output: 5
        Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
        Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.

        Input: prices = [7,6,4,3,1]
        Output: 0
        Explanation: In this case, no transactions are done and the max profit = 0.

        Constraints:

        1 <= prices.length <= 10^5
        0 <= prices[i] <= 10^4

        Plan:
        Sliding Window
        Time: O(n)
        Space: O(1)
        Edge: None
        """
        max_profit = 0
        lowest_buy = prices[0]
        for val in prices:
            cur_profit = val - lowest_buy
            max_profit = max(max_profit, cur_profit)
            lowest_buy = min(lowest_buy, val)
        return max_profit




result = Solution()
print(result.maxProfit([7,1,5,3,6,4]))  # 5
print(result.maxProfit([7,6,4,3,1]))    # 0
print(result.maxProfit([1,4,2]))        # 3
print(result.maxProfit([0,3,8,6,8,6,6,8,2,0,2,7]))  # 8