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
        1. Create a min_heap with  (0,0,0) in it.
        2. Create an added_set.
        3. Loop through nums1 and nums2, exploring two possibilities. Either iterating nums1+1 or nums2+1. If a
        possibility is not in the added_set, then add it to the min_heap. Iterate the larger tuple result.
        4. Pop k tuples from the min_heap, and append them to the final array.
        '''
        # Failed attempt.
        min_heap = [(nums1[0]+nums2[0], nums1[0], nums2[0])]
        added_set = set()
        added_set.add((0,0,0))

        loop_counter = 1
        p1 = 0
        p2 = 0

        while loop_counter <= k:
            if p1+1 < len(nums1)-1:
                option1_tup = ((nums1[p1+1] + nums2[p2]), nums1[p1+1], nums2[p2])
            else:
                option1_tup = ((nums1[p1] + nums2[p2]), nums1[p1], nums2[p2])

            if p2+1 < len(nums2)-1:
                option2_tup = ((nums1[p1] + nums2[p2+1]), nums1[p1], nums2[p2+1])
            else:
                option2_tup = ((nums1[p1] + nums2[p2]), nums1[p1], nums2[p2])

            if option1_tup and (option1_tup not in added_set):
                added_set.add(option1_tup)
                heapq.heappush(min_heap, option1_tup)

            if option2_tup and (option2_tup not in added_set):
                added_set.add(option2_tup)
                heapq.heappush(min_heap, option2_tup)

            if option1_tup and option2_tup:
                if option1_tup[0] >= option2_tup[0]:
                    p1 += 1
                else:
                    p2 += 1
            elif option1_tup:
                p1 += 1
            elif option2_tup:
                p2 += 1
            loop_counter += 1

        final_arr = []
        for i in range(k):
            _, left, right = heapq.heappop(min_heap)
            final_arr.append([left, right])
        return final_arr

