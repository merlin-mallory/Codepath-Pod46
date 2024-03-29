from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        '''
        Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted
        arrays.

        The overall run time complexity should be O(log (m+n)).

        Example 1:
        Input: nums1 = [1,3], nums2 = [2]
        Output: 2.00000
        Explanation: merged array = [1,2,3] and median is 2.

        Example 2:
        Input: nums1 = [1,2], nums2 = [3,4]
        Output: 2.50000
        Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

        Constraints:
        nums1.length == m
        nums2.length == n
        0 <= m <= 1000
        0 <= n <= 1000
        1 <= m + n <= 2000
        -10^6 <= nums1[i], nums2[i] <= 10^6
        '''
        A, B = nums1, nums2
        total_len = len(A) + len(B)
        half_len = total_len // 2

        if len(B) < len(A):
            A, B = B, A

        # A is the smaller size array, B is the larger size array.
        # Binary search the smaller array to find the median.

        l, r = 0, len(A)-1
        while True:
            m = (l+r)//2
            n = half_len - m - 2

            leftA = A[m] if m >= 0 else float('-inf')
            rightA = A[m+1] if m+1 < len(A) else float('inf')
            leftB = B[n] if n >= 0 else float('-inf')
            rightB = B[n+1] if n+1 < len(B) else float('inf')

            if (leftA <= rightB) and (leftB <= rightB):
                if total_len % 2 == 1:
                    return min(rightA, rightB)
                else:
                    return (max(leftA, leftB) + min(leftA, leftB)) / 2
            elif (leftA > rightB):
                r = m - 1
            else:
                l = m + 1

result = Solution()
print(result.findMedianSortedArrays([1,3], [2]))        # 2.00000
print(result.findMedianSortedArrays([1,2], [3,4]))      # 2.50000
