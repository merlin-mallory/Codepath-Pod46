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
        1. Looks like two pointers. l = 0, r = len(height)-1, total_water = 1.
        2. left_max = height[l], right_max = height[r]
        2. while l < r:
            3. if height[l] <= height[r]:
                4. l += 1
                5. if left_max > height[l]
                    6. total_water += left_max - height[l]
                7. else:
                    8. left_max = height[l]
            9. else:
                10. r -= 1
                11. if right_max > height[r]:
                    12. total_water = right_max - height[r]
                13. else:
                    14. right_max = height[r]
        15. return total_water
        """
        l, r, total_water = 0, len(height)-1, 0
        left_max, right_max = height[l], height[r]

        while l < r:
            if height[l] <= height[r]:
                l += 1
                if left_max > height[l]:
                    total_water += left_max - height[l]
                else:
                    left_max = height[l]
            else:
                r -= 1
                if right_max > height[r]:
                    total_water += right_max - height[r]
                else:
                    right_max = height[r]

        return total_water


result = Solution()
print(result.trap([0,1,0,2,1,0,1,3,2,1,2,1]))   # 6
print(result.trap([4,2,0,3,2,5]))               # 9
