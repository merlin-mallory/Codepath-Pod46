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
        1. Create a min_heap, and add the (0,0,0) tuple to it. Create the final_arr.
        2. Loop through the min_heap while there is a min_heap and k > 0.
            3. Pop the top of the min_heap, deconstruct the tuple, and append the pair to the final_arr.
            4. Explore adding +1 to the nums1 index, check if that option has already been added to the min_heap,
            and if not, then add the tuple to the min_heap (if it's within range). Then do the same thing for adding
            +1 to the nums2 index.
        5. Eventually the loop will break when we've reached k tuples in the final_arr.
        6. Return the final_arr.
        '''
        min_heap = []
        added_set = set()
        final_arr = []

        heapq.heappush(min_heap, (nums1[0]+nums2[0], 0, 0))
        added_set.add((nums1[0]+nums2[0], 0, 0))

        while min_heap and k > 0:
            _, nums1_i, nums2_i = heapq.heappop(min_heap)
            final_arr.append([nums1[nums1_i], nums2[nums2_i]])

            if nums1_i+1 <= len(nums1)-1:
                this_tup = (nums1[nums1_i+1]+nums2[nums2_i], nums1_i+1, nums2_i)
                if this_tup not in added_set:
                    heapq.heappush(min_heap, this_tup)
                    added_set.add(this_tup)

            if nums2_i+1 <= len(nums2)-1:
                this_tup = (nums1[nums1_i]+nums2[nums2_i+1], nums1_i, nums2_i+1)
                if this_tup not in added_set:
                    heapq.heappush(min_heap, this_tup)
                    added_set.add(this_tup)

            k -= 1

        return final_arr




result = Solution()
print(result.kSmallestPairs([1,7,11], [2,4,6], 3))  # [[1,2],[1,4],[1,6]]
print(result.kSmallestPairs([1,1,2], [1,2,3], 2))   # [[1,1],[1,1]]
print(result.kSmallestPairs([1,2], [3], 3))         # [[1,3],[2,3]]