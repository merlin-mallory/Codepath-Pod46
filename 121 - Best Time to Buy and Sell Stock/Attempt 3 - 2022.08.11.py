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
        """
        max_profit = 0
        min_buy_amount = prices[0]

        for i in range(1, len(prices)):
            current_price = prices[i]
            current_profit = current_price - min_buy_amount
            if current_profit > max_profit:
                max_profit = current_profit
            if current_price < min_buy_amount:
                min_buy_amount = current_price

        return max_profit
