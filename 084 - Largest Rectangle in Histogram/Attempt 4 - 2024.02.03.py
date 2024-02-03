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

        Plan:
        Two Pointers
        1. l = 0, r = len(heights)-1, max_area = 0, max_l = heights[l], max_r = heights[r]
        2. Loop while l < r.
            3. If heights[l] < heights[r], then calculate cur_area, update max_area, update max_l, and l++.
            4. Otherwise, calculate cur_area, update max_area, update max_r, and r--
        5. Return max_area
        Time: O(n)
        Space: O(1)
        Edge: None
        '''
        stack = []  # Monotonic Decreasing Order, [val, ind]
        max_area = 0

        i = 0
        while i < len(heights):
            start = i
            cur_height = heights[i]
            while stack and cur_height < stack[-1][0]:
                cur_val, cur_ind = stack.pop()
                cur_area = cur_val * (i - cur_ind)
                max_area = max(max_area, cur_area)
                start = cur_ind
            stack.append([cur_height, start])
            i += 1

        while stack:
            cur_val, cur_ind = stack.pop()
            cur_area = cur_val * (len(heights) - cur_ind)
            max_area = max(max_area, cur_area)

        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
