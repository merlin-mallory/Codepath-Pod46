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
        Init max_area = 0, l = 0, r = 0.
        Loop while r < len(heights).
            Set start = r
            Check if stack[-1][0] < heights[r]. If that's the case, then we have identified a decreasing height
            scenario, so we need to stretch left. Pop the stack, calculate the area, update max_area, and update start.
            Append([val, start]) to the stack.

        At this point everything remaining on the stack will be rectangles that stretch right beyond the right bound.
        So calculate those values.
        Loop while stack.
            Pop stack, calculate cur_area, update max_area.

        Return max_area
        '''
        stack = []
        max_area = 0
        l, r = 0, 0
        while r < len(heights):
            start = r
            while stack and heights[r] < stack[-1][0]:
                cur_val, cur_ind = stack.pop()
                cur_area = cur_val * (r - cur_ind)
                max_area = max(max_area, cur_area)
                start = cur_ind
            stack.append([heights[r], start])
            r += 1

        while stack:
            cur_val, cur_ind = stack.pop()
            cur_area = cur_val * (len(heights) - cur_ind)
            max_area = max(max_area, cur_area)

        return max_area

result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
print(result.largestRectangleArea([2,1,2]))         # 3
