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

        1. Create numbers_set that contains all numbers[i].
        2. Loop through numbers, and check if the complement is in the set. If it is, then record the
        first_pass_index. Then loop through numbers again and grab the index of the complement.
        3. Return [first_pass_index, second_pass_index]
        4. Time: O(n), Space: O(n)
        """
        l, r = 0, len(numbers) - 1

        while l < r:
            curSum = numbers[l] + numbers[r]

            if curSum > target:
                r -= 1
            elif curSum < target:
                l += 1
            else:
                return [l + 1, r + 1]

        # My O(n) space solution
        numbers_set = set(numbers)
        first_pass_index = -1
        desired_complement = -1

        for index, ele in enumerate(numbers):
            if target-ele in numbers_set:
                first_pass_index = index
                desired_complement = target-ele
                break

        for i in range(first_pass_index+1, len(numbers)):
            if numbers[i] == desired_complement:
                return [first_pass_index+1, i+1]
