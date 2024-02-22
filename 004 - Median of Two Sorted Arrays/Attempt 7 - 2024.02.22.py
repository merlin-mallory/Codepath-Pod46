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
        # Plan: Sliding Window with Binary Search
        # Calc total_len and half_len
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2

        # Set the shorter len array to A, and the longer len array to B.
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A

        # Binary search through A. Infinite loop, because we're guaranteed an answer
        l, r = 0, len(A)-1
        while True:
            # Calc m = (l + r) // 2 (used for A indexing)
            m = (l+r) // 2
            # Calc n = half_len - m - 2 (used for B indexing)
            n = half_len - m - 2
            # Calc Aleft, Aright, Bleft, Bright. Handle out-of-bounds.
            Aleft = A[m] if (m >= 0) else float('-inf')
            Aright = A[m+1] if ((m+1) < len(A)) else float('inf')
            Bleft = B[n] if (n >= 0) else float('-inf')
            Bright = B[n+1] if ((n+1) < len(B)) else float('inf')

            # Check if (Aleft <= Bright) and (Bleft <= Aright). This is when we've found a median.
            if (Aleft <= Bright) and (Bleft <= Aright):
                # We found the median.
                # Check if the total_len is odd. If so, then return the min of (Aright, Bright). Otherwise,
                # return max((Aleft, Bleft) + min(Aright, Bright))/2.
                if total_len % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright))/2
            # Check if (Aleft > Bright). This means that A is too big, so r = m - 1. Otherwise do l = m + 1.
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1

        # Time: O(log(min(m, n)))
        # Space: O(1)
        # Edge: nums1 and nums2 could be empty


result = Solution()
print(result.findMedianSortedArrays([1,3], [2]))        # 2.00000
print(result.findMedianSortedArrays([1,2], [3,4]))      # 2.50000
