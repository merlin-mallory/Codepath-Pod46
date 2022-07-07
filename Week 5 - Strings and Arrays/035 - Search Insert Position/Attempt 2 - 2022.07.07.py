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

        1. I will write a binary search algorithm.
        2. left_pointer = 0, right_pointer = len(nums)-1
        3. while right_pointer > left_pointer:
            4. mid = (left_pointer + right pointer) // 2
            5. if nums[mid] == target, then return mid
            6. elif nums[mid] > target, then right_pointer = mid, continue
            7. else (nums[mid] < target), then left_pointer = mid
            8. left_pointer++, right pointer--
        8. The loop will break whenever the target is not found in the list. The location where it would be inserted,
        if it existed, would be the right pointer, so return that index.
        '''

        left_pointer, right_pointer = 0, len(nums)-1
        while right_pointer >= left_pointer:
            mid = (left_pointer+right_pointer) // 2
            if nums[mid] == target:
                return mid
            elif nums[mid] > target:
                right_pointer = mid-1
            else: # nums[mid] < target
                left_pointer = mid+1

        return left_pointer

