from typing import List
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        '''
        239. Sliding Window Maximum

        https://leetcode.com/problems/sliding-window-maximum/

        You are given an array of integers nums, there is a sliding window of size k which is moving from the very
        left of the array to the very right. You can only see the k numbers in the window. Each time the sliding
        window moves right by one position.

        Return the max sliding window.

        Example 1:
        Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
        Output: [3,3,5,5,6,7]
        Explanation:
        Window position                Max
        ---------------               -----
        [1  3  -1] -3  5  3  6  7       3
         1 [3  -1  -3] 5  3  6  7       3
         1  3 [-1  -3  5] 3  6  7       5
         1  3  -1 [-3  5  3] 6  7       5
         1  3  -1  -3 [5  3  6] 7       6
         1  3  -1  -3  5 [3  6  7]      7

        Example 2:
        Input: nums = [1], k = 1
        Output: [1]

        Constraints:
        1 <= nums.length <= 10^5
        -10^4 <= nums[i] <= 10^4
        1 <= k <= nums.length

        Plan:
        Sliding Window with Monotonic Decreasing Order Deque
        Time: O(n)
        Space: O(n)
        Edge: Noe
        '''
        import collections
        deque = collections.deque()
        l, r = 0, 0
        final_arr = []
        while r < len(nums):
            while deque and (deque[0] < l): deque.popleft()
            while deque and (nums[r] > nums[deque[-1]]): deque.pop()
            deque.append(r)
            if deque and (r+1 >= k):
                final_arr.append(nums[deque[0]])
                l += 1
            r += 1
        return final_arr

result = Solution()

print(result.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3))  # [3,3,5,5,6,7]
print(result.maxSlidingWindow([1], 1))                  # [1]
print(result.maxSlidingWindow([1], 1))                  # [1]
