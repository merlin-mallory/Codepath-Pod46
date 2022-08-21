import heapq
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

        Plan:
        1. Create a min_heap. Create a tuple (sum, left_i, right_i) initialized to (0,0,0) and add it to the min_heap
        2. Create a final_arr. k > 0 and min_heap, pop the top of min_heap. Deconstruct the tuple to get the current
        indexes, and append those index's values to the final array.
        3. Then explore adding +1 to each index. If they are in bounds and not already added to the minheap, then
        add them to the minheap.
        4. Decrement k by 1. Eventually when k equals zero, or the heap is empty, the loop will break, and we will
        return the final array.
        '''
        import heapq
        min_heap = []
        final_arr = []
        added_set = set()
        heapq.heappush(min_heap, (nums1[0]+nums2[0], 0, 0))

        while k > 0 and min_heap:
            _, left_i, right_i = heapq.heappop(min_heap)
            final_arr.append([nums1[left_i], nums2[right_i]])

            if left_i + 1 < len(nums1):
                current_tup = (nums1[left_i + 1] + nums2[right_i], left_i+1, right_i)
                if current_tup not in added_set:
                    heapq.heappush(min_heap, current_tup)
                    added_set.add(current_tup)

            if right_i + 1 < len(nums2):
                current_tup = (nums1[left_i] + nums2[right_i + 1], left_i, right_i + 1)
                if current_tup not in added_set:
                    heapq.heappush(min_heap, current_tup)
                    added_set.add(current_tup)

            k -= 1

        return final_arr

result = Solution()
print(result.kSmallestPairs([1,7,11], [2,4,6], 3))  # [[1,2],[1,4],[1,6]]
print(result.kSmallestPairs([1,1,2], [1,2,3], 2))   # [[1,1],[1,1]]
print(result.kSmallestPairs([1,2], [3], 3))         # [[1,3],[2,3]]
