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
        Two Pointers.
        1. Initialize l = 0, r = len(height)-1, max_l = height[l], max_r = height[r], vol
        2. Loop while l < r
            3. If height[l] <= height[r], then we'll advance the l pointer.
                4. If height[l] >= max_l, then update max_l.
                5. Otherwise, calculate current_vol = max_l - height[l], and add it to vol
                6. l += 1
            6. Do the same for the r pointer.
        """
        l, r = 0, len(height)-1
        max_l, max_r = 0, 0
        vol = 0

        while l < r:
            if height[l] <= height[r]:
                if height[l] >= max_l:
                    max_l = max(max_l, height[l])
                else:
                    current_vol = max_l - height[l]
                    vol += current_vol
                l += 1
            else:
                if height[r] >= max_r:
                    max_r = max(max_l, height[r])
                else:
                    current_vol = max_r - height[r]
                    vol += current_vol
                r -= 1

        return vol


result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
