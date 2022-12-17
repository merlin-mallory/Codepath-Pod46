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
        1. Looks like two pointers. l = 0, r = len(prices)-1, max_profit = 0.
        2. While l < r:
            3. If moving l is more profitable than moving r, then move l.
                4. buy_low_price = min(buy_low_price, prices[l])
            5. Otherwise, move r.
                6. sell_high_price = mx(sell_high_price, prices[r])
        7.  Calculate and return the final result.
        """
        l, r, max_profit = 0, len(prices)-1, 0
        buy_low_price, sell_high_price = prices[l], prices[r]

        while l < r:
            profit_of_moving_l = prices[l] - prices[l+1]
            profit_of_moving_r = prices[r-1] - prices[r]
            if profit_of_moving_l >= profit_of_moving_r:
                l += 1
                buy_low_price = min(buy_low_price, prices[l])
            else:
                r -= 1
                sell_high_price = max(sell_high_price, prices[r])

        return (sell_high_price - buy_low_price)


result = Solution()
print(result.maxProfit([7,1,5,3,6,4]))  # 5
print(result.maxProfit([7,6,4,3,1]))    # 0
print(result.maxProfit([1,4,2]))        # 3
print(result.maxProfit([0,3,8,6,8,6,6,8,2,0,2,7]))  # 8