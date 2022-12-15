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

        Plan:
        1. Looks like binary search. Left = 0, right = len(nums)-1.
        2. While left <= right, calculate mid index, and then look at that value. If the mid value is < the target
        value, then we know that the target must be to the right, so search from mid+1 to right. If the mid value is
        > the target value, then the opposite is the case, so search from left to mid-1. If the mid value is equal to
        the target value, then we've found the desired index, so return i.
        3. The tricky part is returning the index where the value would go if it's not in the list. I think it's
        always going to be at the right pointer, but we'll see.
        '''
        # Failed, it was left lol.

        left, right = 0, len(nums)-1

        while left <= right:
            mid_i = (left+right) // 2
            mid_v = nums[mid_i]

            if mid_v < target:
                left = mid_i + 1
            elif mid_v > target:
                right = mid_i - 1
            else:  # mid_v =- target
                return mid_i

        return left
