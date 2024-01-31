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
        1. Init max_area = 0, stack = [], pairs = [] (will contain [value, index] pairs)
        2. Construct pairs.
        3. l = 0, r = 0
        4. While r < len(heights)
            6. Calculate current_area = pairs[r][0] * (r - l + 1).
            7. Update max_area
            8. If pairs[r][0] < stack[-1][0], then append pairs[r][0] to the stack.
        '''
        max_area = 0
        stack = []  # pair: (index, height)

        for i, cur_height in enumerate(heights):
            start = i
            while stack and stack[-1][1] > cur_height:
                index, height = stack.pop()
                max_area = max(max_area, height * (i - index))
                start = index
            stack.append((start, cur_height))

        # Everything left in the stack can be extended to the right limit.
        for i, cur_height in stack:
            max_area = max(max_area, cur_height * (len(heights) - i))
        return max_area


result = Solution()
print(result.largestRectangleArea([2,1,5,6,2,3]))   # 10
print(result.largestRectangleArea([2,4]))           # 4
