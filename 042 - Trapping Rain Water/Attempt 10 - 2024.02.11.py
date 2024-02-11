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
        Sliding Window
        Track l_max, r_max, l, r.
        Iterate pointers towards the peak
        Accumulate vol
        Return vol
        Time: O(n)
        Space: O(1)
        Edge: None
        """
        l, r = 0, len(height)-1
        max_l = height[l]
        max_r = height[r]
        vol = 0
        while l <= r:
            if height[l] <= height[r]:
                # Iterate left pointer
                if height[l] > max_l:
                    max_l = height[l]
                else:
                    vol += max_l - height[l]
                l += 1
            else:
                # Iterate right pointer
                if height[r] > max_r:
                    max_r = height[r]
                else:
                    vol += max_r - height[r]
                r -= 1
        return vol


result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
print(result.trap([4,2,3]))                     # 1
print(result.trap([5,4,1,2]))                   # 1
