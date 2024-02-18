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
        l, r = 0, len(height)-1
        l_max = height[0], r_max = height[-1]
        Loop while l <= r.
            If height[l] <= height[r], then either update l_max or calc cur_area = l_max - height[l], update vol, l++.
            If height[l] > height[r], then either update r_max or calc cur_area = r_max - height[r[, update vol, r++.
        Return vol.
        Time: O(n)
        Space: O(1)
        Edge: None
        """
        vol = 0
        l, r = 0, len(height)-1
        l_max, r_max = height[0], height[-1]
        while l <= r:
            if height[l] <= height[r]:
                if height[l] >= l_max:
                    l_max = height[l]
                else:
                    cur_area = l_max - height[l]
                    vol += cur_area
                l += 1
            else:
                if height[r] >= r_max:
                    r_max = height[r]
                else:
                    cur_area = r_max - height[r]
                    vol += cur_area
                r -= 1
        return vol



result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
print(result.trap([4,2,3]))                     # 1
print(result.trap([5,4,1,2]))                   # 1
