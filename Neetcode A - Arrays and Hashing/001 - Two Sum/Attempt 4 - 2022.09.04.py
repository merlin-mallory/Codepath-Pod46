class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        '''
        Given an array of integers nums and an integer target, return indices of the two numbers such that they add
        up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

        Input: nums = [2,7,11,15], target = 9
        Output: [0,1]
        Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

        Input: nums = [3,2,4], target = 6
        Output: [1,2]

        Input: nums = [3,3], target = 6
        Output: [0,1]

        Constraints:

        2 <= nums.length <= 10^4
        -10^9 <= nums[i] <= 10^9
        -10^9 <= target <= 10^9
        Only one valid answer exists.

        Plan:
        1. Sort nums.
        2. Left = 0, right = len(nums)-1
        3. Loop while left < right
            4. current_sum = nums[left] + nums[right]
            5. if current_sum < target:
                6. left++
            7. if current_sum > target:
                8. right--
            9. if current_sum == target:
                10. return[left, right[
        '''
        added_set = set()

        for i in range(len(nums)):
            desired_comp = target - nums[i]
            if desired_comp in added_set:
                return [nums.index(desired_comp), i]
            else:
                added_set.add(nums[i])
