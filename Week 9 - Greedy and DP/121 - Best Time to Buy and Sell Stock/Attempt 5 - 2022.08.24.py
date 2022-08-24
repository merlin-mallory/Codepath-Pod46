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
        1. Initialize lowest_buy_amount to prices[i]. Initialize maximum_profit to 0.
        2. Loop through prices(1, len(prices)). Set current_sell_amount = prices[i]. Calculate current_profit =
        current_sell_amount - lowest_buy_amount. Find the max of maximum_profit and current_profit. Find the min of
        lowest_buy_amount and current_sell_amount.
        3. Return maximum_profit
        """

        lowest_buy_amount = prices[0]
        maximum_profit = 0

        for i in range(1, len(prices)):
            current_sell_amount = prices[i]
            current_profit = current_sell_amount - lowest_buy_amount
            maximum_profit = max(maximum_profit, current_profit)
            lowest_buy_amount = min(lowest_buy_amount, current_sell_amount)

        return maximum_profit
        