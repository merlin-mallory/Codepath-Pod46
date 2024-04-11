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

        Plan:
        Binary Search
        Time: O(log(m+n))
        Space: O(1)
        Edge: None
        '''
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2
        A, B = nums1, nums2
        if len(nums2) < len(nums1):
            A, B = B, A
        l, r = 0, len(A)-1
        while True:
            m = (l + r) // 2
            n = half_len - m - 2
            Aleft = A[m] if (m >= 0) else float('-inf')
            Aright = A[m+1] if (m+1) < len(A) else float('inf')
            Bleft = B[n] if (n >= 0) else float('-inf')
            Bright = B[n+1] if (n+1) < len(B) else float('inf')
            if (Aleft <= Bright) and (Bleft <= Aright):
                # We found the median
                if total_len % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif (Aleft > Bright):
                # A is too big, so we need to shrink it
                r = m - 1
            else:
                l = m + 1


result = Solution()
print(result.findMedianSortedArrays([1,3], [2]))        # 2.00000
print(result.findMedianSortedArrays([1,2], [3,4]))      # 2.50000
