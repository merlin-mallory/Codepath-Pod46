from typing import List
class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        https://leetcode.com/problems/find-k-pairs-with-smallest-sums/description/
        You are given two integer arrays nums1 and nums2 sorted in ascending order and an integer k.

        Define a pair (u, v) which consists of one element from the first array and one element from the second array.

        Return the k pairs (u1, v1), (u2, v2), ..., (uk, vk) with the smallest sums.

        Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        Output: [[1,2],[1,4],[1,6]]
        Explanation: The first 3 pairs
        are returned from the sequence: [1,2],[1,4],[1,6],[7,2],[7,4],[11,2],[7,6],[11,4],[11,6]

        Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
        Output: [[1,1],[1,1]]
        Explanation: The first 2 pairs are returned from the sequence:
        [1,1],[1,1],[1,2],[2,1],[1,2],[2,2],[1,3],[1,3],[2,3]

        Input: nums1 = [1,2], nums2 = [3], k = 3
        Output: [[1,3],[2,3]]
        Explanation: All possible pairs are returned from the sequence: [1,3],[2,3]

        Constraints:

        1 <= nums1.length, nums2.length <= 10^5
        -10^9 <= nums1[i], nums2[i] <= 10^9
        nums1 and nums2 both are sorted in ascending order.
        1 <= k <= 10^4
        '''
        import heapq
        final_arr = []
        minheap = []
        heapq.heappush(minheap, (0, 0, 0))
        visited = set()
        visited.add((0, 0, 0))

        while len(final_arr) < k and minheap:
            _, left_i, right_i = heapq.heappop(minheap)
            final_arr.append([nums1[left_i], nums2[right_i]])

            if left_i+1 <= len(nums1)-1:
                option1_tup = (nums1[left_i+1] + nums2[right_i], left_i+1, right_i)
                if option1_tup not in visited:
                    heapq.heappush(minheap, option1_tup)
                    visited.add(option1_tup)

            if right_i+1 <= len(nums2)-1:
                option2_tup = (nums1[left_i] + nums2[right_i + 1], left_i, right_i+1)
                if option2_tup not in visited:
                    heapq.heappush(minheap, option2_tup)
                    visited.add(option2_tup)

        return final_arr

result = Solution()
print(result.kSmallestPairs([1,7,11], [2,4,6], 3))  # [[1,2],[1,4],[1,6]]
print(result.kSmallestPairs([1,1,2], [1,2,3], 2))   # [[1,1],[1,1]]
print(result.kSmallestPairs([1,2], [3], 3))         # [[1,3],[2,3]]
