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
        1. Create a min_heap, and put the (0,0) pair in there. Create final_arr. Create added_set.
        2. Loop while there is a heap and k:
            3. Pop the top of the min_heap, grab the indexes, append the pair to final_arr.
            4. Explore adding +1 to nums1, and if it's in range and not in added_set, then add it to the min_heap.
            5. Do the same exploration for +1 to nums2.
        6. Return the final_arr
        '''
        import heapq
        min_heap = []
        final_arr = []
        added_set = set()
        heapq.heappush(min_heap, (nums1[0]+nums2[0], 0, 0))
        added_set.add((0, 0))

        while min_heap and k:
            _, left, right = heapq.heappop(min_heap)
            final_arr.append([nums1[left], nums2[right]])

            if left + 1 <= len(nums1)-1 and (left+1, right) not in added_set:
                heapq.heappush(min_heap, (nums1[left+1]+nums2[right], left+1, right))
                added_set.add((left+1, right))

            if right + 1 <= len(nums2)-1 and (left, right+1) not in added_set:
                heapq.heappush(min_heap, (nums1[left]+nums2[right+1], left, right+1))
                added_set.add((left, right+1))

            k -= 1

        return final_arr

result = Solution()
print(result.kSmallestPairs([1,7,11], [2,4,6], 3))  # [[1,2],[1,4],[1,6]]
print(result.kSmallestPairs([1,1,2], [1,2,3], 2))   # [[1,1],[1,1]]
print(result.kSmallestPairs([1,2], [3], 3))         # [[1,3],[2,3]]
