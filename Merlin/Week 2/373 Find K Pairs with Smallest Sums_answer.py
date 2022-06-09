class Solution:
    def kSmallestPairs(self, nums1: List[int], nums2: List[int], k: int) -> List[List[int]]:
        '''
        337 Find K Pairs with Smallest Sums: https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
        Given two sorted arrays and an integer k, we will find the smallest k pairs of sums (one from each array).

        Restrictions:
        1. len(nums1) >= 1
        2. len(nums2) <= 10^5
        3. k >= 1
        4. k <= 10^9
        5. nums1 and nums2 are both sorted in ascending order.

        Input: nums1 = [1,7,11], nums2 = [2,4,6], k = 3
        Output: [[1,2],[1,4],[1,6]]

        Input: nums1 = [1,1,2], nums2 = [1,2,3], k = 2
        Output: [[1,1],[1,1]]

        Input: nums1 = [1,2], nums2 = [3], k = 3
        Output: [[1,3],[2,3]]

        Plan:
        1. Create a minheap.
        2. Loop through the arrays and toss all possible combinations into the minheap.
        3. Pop k values from the minheap and add them to the final list
        4. Return the final list
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