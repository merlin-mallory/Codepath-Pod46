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
        '''
        max_area = 0
        stack = []

        # Loop through heights. Check if heights[i] < stack[i]. If so, we can calculate a rectangle stretch
        # leftwards. Pop the stack, calc the cur_area, update the max_area, update the start. In any event, Append
        # [start, heights[i]] to the stack.
        for i in range(len(heights)):
            cur = heights[i]
            start = i
            while stack and (cur < stack[-1][1]):
                stack_i, stack_v = stack.pop()
                cur_area = stack_v * (i - stack_i)
                max_area = max(max_area, cur_area)
                start = stack_i
            stack.append([start, cur])

        # If there are remaining items in the stack, then we can calc rectangles stretching leftwards. Pop the stack,
        # calc cur_area, update the max_area.
        for i in range(len(stack)):
            stack_i, stack_v = stack[i][0], stack[i][1]
            cur_area = stack_v * (len(heights) - stack_i)
            max_area = max(cur_area, max_area)

        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
print(result.largestRectangleArea([2,1,2]))         # 3
