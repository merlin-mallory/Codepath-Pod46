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
        1. Looks like two pointers. left = 0, right = len(numbers)-1.
        2. Initialize current_sum to numbers[left] + numbers[right]. If current_sum equals the target, then return [
        left, right]. If current_sum > target, then we need to explore making the sum smaller, so decrement right by
        one. If current_sum < target, then we need to explore making the sum bigger, so increment left by one.
        3. We are guarenteed to have a single answer in the array, so we can terminate the loop with current_sum =
        target, and then return [left, right]
        """
        left, right = 0, len(numbers)-1

        current_sum = numbers[left] + numbers[right]

        while current_sum != target:
            if current_sum > target:
                right -= 1
                current_sum = numbers[left] + numbers[right]
            elif current_sum < target:
                left += 1
                current_sum = numbers[left] + numbers[right]

        return [left+1, right+1]

result = Solution()
print(result.twoSum([2,7,11,15], 9))    # [1,2]
print(result.twoSum([2,3,4], 6))        # [1,3]
print(result.twoSum([-1,0], -1))        # [1,2]
