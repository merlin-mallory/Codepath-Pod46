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
        1. Initialize l = 0, r = len(height)-1, max_vol = 0.
        2. Loop while l < r
            3. Calculate the current volume. (r - l + 1) * min(height[l], height[r])
            4. Update max_vol.
            5. If height[l] >= height[r], then l++. Otherwise r--.
        6. Return max_vol at the end
        Time: O(n), Space: O(1)
        """
        l, r = 0, len(height)-1
        max_vol = 0

        while l < r:
            if height[l] <= height[r]:
                current_vol = height[l] * (r-l)
                max_vol = max(current_vol, max_vol)
                l += 1
            else:
                current_vol = height[r] * (r-l)
                max_vol = max(current_vol, max_vol)
                r -= 1

        return max_vol

result = Solution()
print(result.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(result.maxArea([1,1]))                # 1
