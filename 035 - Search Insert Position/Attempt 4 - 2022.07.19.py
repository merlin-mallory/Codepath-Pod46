class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        '''
        https://leetcode.com/problems/search-insert-position/description/

        Given a sorted array of distinct integers and a target value, return the index if the target is found.
        If not, return the index where it would be if it were inserted in order.

        You must write an algorithm with O(log n) runtime complexity.

        Input: nums = [1,3,5,6], target = 5
        Output: 2

        Input: nums = [1,3,5,6], target = 2
        Output: 1

        Input: nums = [1,3,5,6], target = 7
        Output: 4

        Constraints:

        1 <= nums.length <= 10^4
        -10^4 <= nums[i] <= 10^4
        nums contains distinct values sorted in ascending order.
        -10^4 <= target <= 10^4

        1. Binary search algorithm
        2. left = 0, right = len(nums)-1
        3. mid = (left + right) // 2
        4. While right >= left:
            5. If nums[mid] < target, then left = mid. Else if nums[mid] > target, then right = mid.
            Else if nums[mid] == target, then return mid.
        6. Return right (or left?)
        '''

        left = 0
        right = len(nums)-1

        while right >= left:
            mid = (left+right) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid+1
            elif nums[mid] > target:
                right = mid-1

        return left

        # target: 7
        # left: 0, right: 3, mid: 1, mid_value: 3, 3<7, so left = 1+1=2
        # left: 2, right: 3, mid: 2, mid_value: 5, 5<7, so left = 2+1=3
        # left: 3, right: 3, mid: 3, mid_value: 6, 6<7, so left = 3+1 = 4
        # Loop breaks because left > right, left = 3, left =4. If a 7 existed, it would be in index 4. So we want to
        # return left.
