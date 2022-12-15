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
        1. Looks like two pointers. Left = 0, right = len(height)-1, total_water = 0. left_max_height = height[0],
        right_max_height = height[-1].
        2. Loop while left < right.
            3. if left_max_height < right_max_height:
                4. left++
                5. If height[left] < left_max_height:
                    6. total_water + (left_max_height - height[left]
                7. Else: (new max found)
                    8. left_max_height = height[left]
            9. Else:
                10. mirror, but for the right side.
        """
        left, right = 0, len(height)-1
        total_water = 0
        left_max_height, right_max_height = height[0], height[-1]

        while left < right:
            if left_max_height < right_max_height:
                left += 1
                if height[left] < left_max_height:
                    total_water += (left_max_height - height[left])
                else:
                    left_max_height = height[left]

            else:
                right -= 1
                if height[right] < right_max_height:
                    total_water += (right_max_height - height[right])
                else:
                    right_max_height = height[right]

        return total_water

result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
