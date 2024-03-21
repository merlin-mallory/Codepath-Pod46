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
        Stack
        Create stack. Will contain [heights[i], i] pairs.
        max_area = 0
        i = 0
        Loop through heights. Calc all leftward stretching rectangles and update max_area.
            cur = heights[i]
            start = i
            while cur < stack[-1][0]:
                stack_v, stack_i = stack.pop()
                cur_area = stack_v * (r - l)
                max_area = max(max_area, cur_area)
                start = stack_i
            stack.append([cur, start])
        Loop through stack. Calc all rightward stretching rectangles and update max_area.
            cur_area = stack_v * (len(heights) - stack_i)
            max_area = max(max_area, cur_area)
        return max_area
        '''
        stack = []
        max_area = 0
        for cur_i, cur_v in enumerate(heights):
            start = cur_i
            while stack and (cur_v < stack[-1][1]):
                stack_i, stack_v = stack.pop()
                cur_area = stack_v * (cur_i - stack_i)
                max_area = max(max_area, cur_area)
                start = stack_i
            stack.append([start, cur_v])
        for stack_i, stack_v in stack:
            cur_area = stack_v * (len(heights) - stack_i)
            max_area = max(max_area, cur_area)
        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
print(result.largestRectangleArea([2,1,2]))         # 3
