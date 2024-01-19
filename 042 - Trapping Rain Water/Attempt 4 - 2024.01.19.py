from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        """
        https://leetcode.com/problems/trapping-rain-water/

        Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
        water it can trap after raining.

        Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
        Output: 6

        Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1].
        In this case, 6 units of rain water (blue section) are being trapped.

        Input: height = [4,2,0,3,2,5]
        Output: 9

        Constraints:
        n == height.length
        1 <= n <= 2 * 10^4
        0 <= height[i] <= 10^5

        Plan:
        Two Pointers
        1. Initialize pointers. l = 0, r = len(height)-1.
        2. Initialize l_max and r_max to height[l] and height[r]
        3. Check if height[l] > height[r]. If so, l+1.
        """
        l, r = 0, len(height)-1
        l_max, r_max = height[l], height[r]
        vol = 0

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if l_max > height[l]:
                    vol += l_max - height[l]
                else:
                    l_max = height[l]
            else:
                r -= 1
                if r_max > height[r]:
                    vol += r_max - height[r]
                else:
                    r_max = height[r]

        return vol


result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
