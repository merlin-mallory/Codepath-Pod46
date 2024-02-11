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
        Two segments: All rectangles stretching left, and all rectangles stretching right.
        We'll handle the stretching left segment first by using a stack to track extensions backwards.
        At each stage we'll update max_area.
        After we finish the loop, all of the items remaining on the stack will be rectangles stretching right. So
        we'll pop and process those as well.
        Return max_area.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        stack = []
        max_area = 0
        l, r = 0, 0
        while r < len(heights):
            current = r
            cur_val = heights[r]
            while stack and (cur_val < stack[-1][0]):
                stack_v, stack_i = stack.pop()
                current_area = stack_v * (r - stack_i)
                max_area = max(max_area, current_area)
                current = stack_i
            stack.append([cur_val, current])
            r += 1

        while stack:
            stack_v, stack_i = stack.pop()
            current_area = stack_v * (len(heights) - stack_i)
            max_area = max(max_area, current_area)

        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
print(result.largestRectangleArea([2,1,2]))         # 3
