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

        Brute ForcePlan:
        1. Outer loop through prices, inner loop from outer loop to end of array. Calculate current_profit,
        and if it exceeds max_profit, then set max_profit to current_profit.

        DP Plan:
        1. Create a max_profit array of size len(prices), this will contain the maximum profit up to that day
        2. Create a lowest_buy_date array of size len(prices), this will contain index values
        3. Loop through prices, and fill up the other two arrays.
        4. Return the last element in the max_profit array.
        """
        if len(prices) == 1:
            return 0

        max_profit = [0] * len(prices)
        lowest_buy_date = 0
        lowest_buy_value = prices[0]

        for i in range(1, len(prices)):
            current_profit = prices[i] - prices[lowest_buy_date]
            max_profit[i] = max(max_profit[i-1], current_profit)
            if prices[i] < lowest_buy_value:
                lowest_buy_date = i
                lowest_buy_value = prices[i]

        return max(0, max_profit[-1])

        # Optimal One Pass, O(n) time O(1) space
        # min_price = float('inf')
        # max_profit = 0
        # for i in range(len(prices)):
        #     if prices[i] < min_price:
        #         min_price = prices[i]
        #     elif prices[i] - min_price > max_profit:
        #         max_profit = prices[i] - min_price
        #
        # return max_profit



        # Brute Force is time limit exceeded
        # max_profit = 0
        # for i in range(len(prices)):
        #     for j in range(i, len(prices)):
        #         current_profit = prices[j] - prices[i]
        #         max_profit = max(max_profit, current_profit)
        #
        # return max_profit
