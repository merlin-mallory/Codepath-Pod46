
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
        1. Looks like a min heap problem.
        2. Use two pointers to select the tuples that will be tossed into the minheap. The (0,0) pair is guarenteed
        to be one of the minheap values. Then there's two possiblities for the next smallest pair. Calculate nums1[
        i]+nums2[i+1] and nums1[i+1]+nums2[i]. Add the smaller sum to the minheap.
        '''
        # Failed attempt. Two pointers is not involved at all, I should've stuck with the gut reaction of just
        # building a minheap, making a hashmap to keep track of visited, and tossing both possiblities into the
        # minheap each iteration. Loop while len(final_arr) < k and there's a queue. Interesting note about heap
        # queue: I don't need to use heapify before doing heappush and heappop. For heappop, the only parameter is
        # the heap var. For heappush, the parameter is the heap var and then the tuple to be chucked into the heap.
        # It looks like heapq defaults to minheap.

        final_result = [[nums1[0], nums2[0]]]

        nums1_i = 0
        nums2_i = 0

        for i in range(k-1):
            if nums1_i + 1 < len(nums1):
                move_nums1 = nums1[nums1_i+1] + nums2[nums2_i]
            else:
                move_nums1 = float('inf')

            if nums2_i + 1 < len(nums2):
                move_nums2 = nums1[nums1_i] + nums2[nums2_i+1]
            else:
                move_nums2 = float('inf')

            if move_nums1 <= move_nums2 and move_nums1 != float('inf'):
                final_result.append([nums1[nums1_i+1], nums2[nums2_i]])
                nums1_i += 1
            elif move_nums1 >= move_nums2 and move_nums2 != float('inf'):
                final_result.append([nums1[nums1_i], nums2[nums2_i+1]])
                nums2_i += 1

        return final_result
