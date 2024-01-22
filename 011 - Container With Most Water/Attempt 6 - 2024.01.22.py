from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/container-with-most-water/

        You are given an integer array 'height' of length n. There are n vertical lines drawn such that the two
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
        Two Pointers
        1. Initialize vars. l = 0, r = len(height)-1, vol = 0, l_max = height[l], r_max = height[r].
        2. Check if height[l] <= height[r]. We'll advance the pointer of the smaller height.
            3. Check if height[l] <= l_max. If so, calculate the current volume (l_max - height[l]), and add it to
            vol. In any event, l += 1.
            4. Do the same thing for the right side. Eventually the pointers will converge on the max height of the
            array.
        5. Return vol
        """
        l, r = 0, len(height)-1
        max_vol = 0

        while l < r:
            if height[l] <= height[r]:
                current_vol = height[l] * (r-l)
                max_vol = max(max_vol, current_vol)
                l += 1
            else:
                current_vol = height[r] * (r-l)
                max_vol = max(max_vol, current_vol)
                r -= 1

        return max_vol

result = Solution()
print(result.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(result.maxArea([1,1]))                # 1
