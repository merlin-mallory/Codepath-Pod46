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
        Time: O(n)
        Space: O(1)
        Edge: None
        """
        l, r = 0, len(height)-1
        water_vol = 0
        left_max = height[l]
        right_max = height[r]
        while l < r:
            if height[l] <= height[r]:
                if height[l] < left_max:
                    water_vol += left_max - height[l]
                else:
                    left_max = height[l]
                l += 1
            else:
                if height[r] < right_max:
                    water_vol += right_max - height[r]
                else:
                    right_max = height[r]
                r -= 1
        return water_vol



result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
print(result.trap([4,2,3]))                     # 1
print(result.trap([5,4,1,2]))                   # 1
