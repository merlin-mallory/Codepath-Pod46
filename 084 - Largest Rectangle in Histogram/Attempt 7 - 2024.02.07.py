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
        Stack Sliding Window
        Init max_area = 0
        l = 0, r = 0
        Loop while r < len(heights).
            start = r
            cur_val = heights[r]
            if cur_val < stack[-1][0]:
                stack_val, stack_i = stack.pop()
                cur_area = stack_val * (r - stack_i)
                Update max_area
                start = stack_i
            append([cur_val, start]) to the stack
        Loop while stack.
            stack_val, stack_i = stack.pop()
            cur_area = stack_val * (len(height) - stack_i)
            Update max_area
        Return max_area
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        max_area = 0
        l, r = 0, 0
        while r < len(heights):
            start = r
            cur_val = heights[r]
            while stack and cur_val < stack[-1][0]:
                stack_val, stack_i = stack.pop()
                cur_area = stack_val * (r - stack_i)
                max_area = max(max_area, cur_area)
                start = stack_i
            stack.append([cur_val, start])
            r += 1

        while stack:
            stack_val, stack_i = stack.pop()
            cur_area = stack_val * (len(heights) - stack_i)
            max_area = max(max_area, cur_area)

        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
print(result.largestRectangleArea([2,1,2]))         # 3
