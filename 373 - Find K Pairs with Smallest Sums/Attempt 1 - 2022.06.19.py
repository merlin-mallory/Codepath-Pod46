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

        1 <= nums1.length, nums2.length <= 105
        -109 <= nums1[i], nums2[i] <= 109
        nums1 and nums2 both are sorted in ascending order.
        1 <= k <= 104

        1. Create a maxheap that will hold exactly k min pairs.
        2. Toss the (0,0) combo in the minheap, because it's guaranteed to be one of the lowest
        3. Create two pointers, one for each list. Seek the next smallest sum between the two combos. Make it a
        tuple, and add it to the maxheap. If the maxheap's counter reaches k, then pop the k tuples in the max heap and
        construct the array of tuples for the return.
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

        # Failed attempt
        # maxheap = []
        # heapq.heapify(maxheap)
        # heap_counter = 0
        #
        # nums1_left_pointer = 0
        # nums1_right_pointer = 0
        #
        # nums2_left_pointer = 0
        # nums2_right_pointer = 0
        #
        # starter_sum = nums1[0] + nums2[0]
        # starter_tuple = (-starter_sum, nums1[0], nums2[0])
        # heapq.heappush(maxheap, starter_tuple)
        # heap_counter += 1
        #
        # while heap_counter < k:
        #     if nums1_left_pointer < (len(nums1) - 2):
        #         combo1_sum = nums1[nums1_left_pointer + 1] + nums2[nums1_right_pointer]
        #     else:
        #         combo1_sum = float('inf')
        #
        #     if nums2_right_pointer < (len(nums2) - 2):
        #         combo2_sum = nums1[nums2_left_pointer] + nums2[nums2_right_pointer + 1]
        #     else:
        #         combo2_sum = float('inf')
        #
        #     if combo1_sum <= combo2_sum:
        #         nums1_left_pointer += 1
        #         current_tuple = (-combo1_sum, nums1[nums1_left_pointer], nums2[nums1_right_pointer])
        #         heapq.heappush(maxheap, current_tuple)
        #         heap_counter += 1
        #     else:
        #         nums2_right_pointer += 1
        #         current_tuple = (-combo2_sum, nums1[nums2_left_pointer], nums2[nums2_right_pointer])
        #         heapq.heappush(maxheap, current_tuple)
        #         heap_counter += 1
        #
        # final_list = []
        #
        #
        # while maxheap:
        #     tuple_sum, n1, n2 = heapq.heappop(maxheap)
        #     final_list.append([n1, n2])
        #
        # return final_list

# Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
# Put [3,1,2] into the heap. num1pointer = 0, num2pointer = 0, heapcounter=1.
# Combo1 = 7+2= 9, Combo2 = 1+4 = 5, select combo2
# Put [5,1,4] into the heap. num1pointer = 0, num2pointer = 1, heapcounter=2.
# Combo1 = 7+4 = 11, Combo2 = 1+6 =7, select combo2
# Put [7,1,6] into the heap. num1pointer = 0, num2pointer = 2, heapcounter=3.
# Loop breaks, final return [[1,2],[1,4],[1,6]]
# Output: [[1,2],[1,4],[1,6]]