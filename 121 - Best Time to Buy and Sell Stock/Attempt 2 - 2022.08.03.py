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
        1. Dynamic Programming
        2. Set minimum_buy_value = prices[0]. Set maximum_profit = 0
        3. Loop through prices from (1, len(prices)). Calculate current_profit = prices[i] - minimum_buy_value.
        Update maximum_profit. Update minimum_buy_value.
        4. After we finish the loop, the maximum_profit will hold the optimal solution for the input, so return
        maximum_profit.
        """
        minimum_buy_value, maximum_profit = prices[0], 0

        for i in range(1, len(prices)):
            current_profit = prices[i] - minimum_buy_value
            maximum_profit = max(maximum_profit, current_profit)
            minimum_buy_value = min(minimum_buy_value, prices[i])

        return maximum_profit
        