from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/

        You are given an integer array height of length n. There are n vertical lines drawn such that the two
        endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.

        Input: height = [1,8,6,2,5,4,8,3,7]
        Output: 49
        Explanation: The above vertical lines are represented by array
        [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

        Input: height = [1,1]
        Output: 1

        Constraints:
        n == height.length
        2 <= n <= 10^5
        0 <= height[i] <= 10^4

        Plan:
        1. Looks like two pointers. Left = 0, right = len(height)-1. left_max_height = height[left], right_max_height =
        height[right], left_max_index = 0, right_max_index = len(height)-1.
        2. While left < right:
            3. If height[left] > left_max_height, then update the left_max values.
            4. If height[right]
        Honestly I'm not sure. Skipping to solution.
        """
        l, r = 0, len(height) - 1
        res = 0

        while l < r:
            res = max(res, min(height[l], height[r]) * (r - l))
            if height[l] < height[r]:
                l += 1
            elif height[r] <= height[l]:
                r -= 1
        return res

result = Solution()
print(result.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(result.maxArea([1,1]))                # 1

# Neetcode
# def maxProfit(self, prices: List[int]) -> int:
#         res = 0
#
#         l = 0
#         for r in range(1, len(prices)):
#             if prices[r] < prices[l]:
#                 l = r
#             res = max(res, prices[r] - prices[l])
#         return res

# Leetcode
# def maxProfit(self, prices: List[int]) -> int:
#         min_price = float('inf')
#         max_profit = 0
#         for i in range(len(prices)):
#             if prices[i] < min_price:
#                 min_price = prices[i]
#             elif prices[i] - min_price > max_profit:
#                 max_profit = prices[i] - min_price
#
#         return max_profit
