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
        1. Init max_vol = 0, l = 0, r = len(height()-1.
        2. Loop while l < r
            3. If height[l] <= height[r]:
                4. cur_vol = height[l] * (r-l)
                5. max_vol = max(max_vol, cur_vol)
                6. l += 1
            7. Otherwise, same for r
        8. Return max_vol
        """

        max_vol = 0
        l = 0
        r = len(height)-1

        while l < r:
            if height[l] <= height[r]:
                cur_vol = height[l] * (r-l)
                max_vol = max(max_vol, cur_vol)
                l += 1
            else:
                cur_vol = height[r] * (r-l)
                max_vol = max(max_vol, cur_vol)
                r -= 1

        return max_vol

result = Solution()
print(result.maxArea([1,8,6,2,5,4,8,3,7]))  # 49
print(result.maxArea([1,1]))                # 1
