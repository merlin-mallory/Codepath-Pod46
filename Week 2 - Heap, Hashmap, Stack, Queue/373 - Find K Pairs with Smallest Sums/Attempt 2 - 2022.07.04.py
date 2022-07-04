import heapq


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
        1. nums1_pointer = 0, nums2_pointer = 0, max_heap = [], heapq.heapify(max_heap), added_set = (), res = []
        2. Calculate the [0][0] sum, add the tuple (sum, nums1[nums1_pointer], nums2[nums2_pointer]) to the maxheap.
        3. While the len(res) < k:
            4. Pop the top of the maxheap, deconstruct the tuple, and append it to the final return list.
            5. Explore iterating nums1_pointer by 1. Calculate the new sum, and if the tuple is not in added_set,
            then add it the max_heap.
            6. Explore iterating nums2_pointer by 1. Calculate the new sum, and if the tuple is not in added_set,
            then add it the max_heap.
        7. Return the final response
        8. Time: O(k log (m+n)), where k is parameter, m is len(nums1), and n is len(nums2).
        9. Space: O(m+n)
        '''
        import heapq

        ret = []

        if len(nums1) * len(nums2) > 0:
            queue = [(nums1[0] + nums2[0], (0, 0))]
            visited = {}

            while len(ret) < k and queue:
                _, (i, j) = heapq.heappop(queue)
                ret.append((nums1[i], nums2[j]))

                if j + 1 < len(nums2) and (i, j + 1) not in visited:
                    heapq.heappush(queue, (nums1[i] + nums2[j + 1], (i, j + 1)))
                    visited[(i, j + 1)] = 1

                if i + 1 < len(nums1) and (i + 1, j) not in visited:
                    heapq.heappush(queue, (nums1[i + 1] + nums2[j], (i + 1, j)))
                    visited[(i + 1, j)] = 1
        return ret

        # Failed
        # nums1_pointer, nums2_pointer, max_heap, res, added_set = 0, 0, [], [], {}
        # heapq.heapify(max_heap)
        #
        # starting_sum = nums1[nums1_pointer] + nums2[nums2_pointer]
        # new_tuple = (-starting_sum, nums1[nums1_pointer], nums2[nums2_pointer])
        # heapq.heappush(max_heap, new_tuple)
        #
        # num1_max_index = len(nums1) - 1
        # num2_max_index = len(nums2) - 1
        #
        # while len(res) < k and max_heap:
        #     _, left, right = heapq.heappop(max_heap)
        #     res.append([left, right])
        #
        #     if nums1_pointer+1 <= num1_max_index:
        #         option1_sum = nums1[nums1_pointer+1] + nums2[nums2_pointer]
        #         option1_tuple = (option1_sum, nums1[nums1_pointer+1], nums2[nums2_pointer])
        #     else:
        #         option1_sum = float('inf')
        #
        #     if nums2_pointer+1 <= num2_max_index:
        #         option2_sum = nums1[nums1_pointer] + nums2[nums2_pointer+1]
        #         option2_tuple = (option2_sum, nums1[nums1_pointer], nums2[nums2_pointer])
        #     else:
        #         option2_sum = float('inf')
        #
        #     if option1_sum != float('inf'):
        #         if option1_tuple not in added_set:
        #             heapq.heappush(max_heap, option1_tuple)
        #             nums1_pointer += 1
        #
        #     if option1_sum != float('inf'):
        #         if option2_tuple not in added_set:
        #             heapq.heappush(max_heap, option2_tuple)
        #             nums2_pointer += 1
        #
        # return res
