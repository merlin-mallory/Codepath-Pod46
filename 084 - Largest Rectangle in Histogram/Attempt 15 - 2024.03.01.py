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
        Create max_area = 0
        Create stack (will contain [i, heights[i]] pairs)
        Loop through heights, and harvest all rectangles stretching left.
            start = i
            Calc cur.
            Loop while cur < stack[-1].
                stack_i, stack_v = stack.pop()
                cur_area = stack_v * (r - l)
                max_area = max(cur_area, max_area)
                start = stack_i
            Append [start, heights[i]] to the stack.

        Loop through stack, and harvest all rectangles stretching right.
        Loop through stack.
            cur_area = stack[i][1] * (len(heights) - 1 - stack[i][0])
            max_area = max(max_area, cur_area
        Return max_area.
        Time: O(n)
        Space: O(n)
        Edge: None
        '''
        max_area = 0
        stack = []      # Will contain [i, heights[i]] pairs
        i = 0
        while i < len(heights):
            start = i
            cur = heights[i]
            while stack and cur < stack[-1][1]:
                stack_i, stack_v = stack.pop()
                cur_area = stack_v * (i - stack_i)
                max_area = max(max_area, cur_area)
                start = stack_i
            stack.append([start, heights[i]])
            i += 1

        for i in range(len(stack)):
            cur_area = stack[i][1] * (len(heights) - stack[i][0])
            max_area = max(cur_area, max_area)

        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
print(result.largestRectangleArea([2,1,2]))         # 3
