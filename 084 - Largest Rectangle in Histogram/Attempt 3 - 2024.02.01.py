from typing import List
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        '''
        084 - Largest Rectangle in Histogram

        https://leetcode.com/problems/largest-rectangle-in-histogram/

        Given an array of integers heights representing the histogram's bar height
        where the width of each bar is 1,
        return the area of the largest rectangle in the histogram.

        Example 1:
        Input: heights = [2,1,5,6,2,3]
        Output: 10
        Explanation: The above is a histogram where width of each bar is 1.
        The largest rectangle is shown in the red area, which has an area = 10 units.

        Example 2:
        Input: heights = [2,4]
        Output: 4

        Constraints:
        1 <= heights.length <= 10^5
        0 <= heights[i] <= 10^4
        '''
        # Monotonic Decreasing Order Stack
        stack = []  # [Index, Height]
        max_area = 0

        i = 0
        while i < len(heights):
            start = i
            cur_height = heights[i]
            while stack and cur_height < stack[-1][1]:
                cur_ind, cur_val = stack.pop()
                cur_area = cur_val * (i - cur_ind)
                max_area = max(max_area, cur_area)
                start = cur_ind
            stack.append([start, cur_height])
            i += 1

        while stack:
            cur_ind, cur_val = stack.pop()
            cur_area = cur_val * (len(heights) - cur_ind)
            max_area = max(max_area, cur_area)

        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
