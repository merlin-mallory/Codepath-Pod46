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
        1. Looks like sliding window. Set max_water = 0. Left = 0, right = len(height)-1.
        2. While left < right,
            3. Calculate current_area = (right - left) * min(height[left], height[right])
            4. Update max_water.
            5. Iterate the smaller pointer inwards.
        """

        max_water = 0
        left, right = 0, len(height)-1

        while left < right:
            current_area = (right - left) * min(height[left], height[right])
            max_water = max(max_water, current_area)
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1

        return max_water

result = Solution()
print(result.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(result.maxArea([1,1]))                # 1
