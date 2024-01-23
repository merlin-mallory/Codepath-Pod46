from typing import List
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/

        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers
        such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[
        index2] where 1 <= index1 < index2 <= numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1,
        index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.

        Input: numbers = [2,7,11,15], target = 9
        Output: [1,2]
        Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].

        Input: numbers = [2,3,4], target = 6
        Output: [1,3]
        Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].

        Input: numbers = [-1,0], target = -1
        Output: [1,2]
        Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].

        Constraints:
        2 <= numbers.length <= 3 * 10^4
        -1000 <= numbers[i] <= 1000
        numbers is sorted in non-decreasing order.
        -1000 <= target <= 1000
        The tests are generated such that there is exactly one solution.

        I must use O(1) space.

        Plan:
        Two Pointers
        1. Initialize l=0, r = len(numbers)-1.
        2. Loop while l < r
            3. Check if twoSum > target. If it is, then we need a smaller result, so r--.
            4. Check if twoSum < target. If it is, then we need a larger result, so l++.
            5. Otherwise twoSum == target, so return [l+1, r+1] (because we need to offset by 1)
        We are guarenteeing that there is only one solution in numbers, and len(numbers) >= 2, so no edge cases.
        Time: O(n), Space: O(1)
        """
        l, r = 0, len(numbers)-1

        while l < r:
            twoSum = numbers[l] + numbers[r]
            if twoSum > target:
                r -= 1
            elif twoSum < target:
                l += 1
            else:
                return [l+1, r+1]
