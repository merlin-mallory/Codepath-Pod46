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
        Init vol = 0, l = 0, r = len(height)-1, max_l = 0, max_r = 0.
        Loop while l < r.
            Check if height[l] <= height[r]. If so, then we'll advance the left pointer, because we know there will
            be a right bound that will contain the water. So the first thing we do is check if height[i] > max_l,
            and if so, just update max_l. We don't need to add any water in this case. Otherwise, if height[i] <=
            max_l, then we should add that index's water to vol. In either case, advance l += 1
            Do the same thing for the r pointer.
        Return vol.
        """
        vol = 0
        l, r = 0, len(height)-1
        max_l = height[l]
        max_r = height[r]

        while l < r:
            if height[l] <= height[r]:
                # Advance left pointer
                if height[l] < max_l:
                    vol += max_l - height[l]
                else:
                    max_l = height[l]
                l += 1
            else:
                # Advance right pointer
                if height[r] < max_r:
                    vol += max_r - height[r]
                else:
                    max_r = height[r]
                r -= 1
        return vol


result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
print(result.trap([4,2,3]))                     # 1
print(result.trap([5,4,1,2]))                   # 1
