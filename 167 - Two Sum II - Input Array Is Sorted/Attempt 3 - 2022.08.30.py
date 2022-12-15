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
        1. Looks like two pointers. Left = 0, right = len(numbers)-1.
        2. Loop while left < right:
            3. current_val = numbers[left] + numbers[right]
            4. If current_val < target, then we need to increase the sum, so left++
            5. If current_val > target, then we need to decrease the sum, so right--
            6. If current_val == target, then we need to return [left+1, right+1] (because the array is 1-indexed).
        7. It is guarenteed that we'll find at least one current_val equal to the target, so we don't need to do any
        extra return statements.
        8. Time: O(n), Space: O(1)
        """
        left, right = 0, len(numbers)-1

        while left < right:
            current_val = numbers[left] + numbers[right]
            if current_val < target:
                left += 1
            elif current_val > target:
                right -= 1
            else:   # current_val == target
                return [left+1, right+1]
            