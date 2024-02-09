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
        Set the smaller size list to A, and the larger size list to B.
        Calculate total_len and half_len.
        Binary search through A. Loop while True, because we are guaranteed an answer
            At each step, calc m = (l + r) // 2, and n = half_len - m - 2.
            Set Aleft = A[m], Aright = A[m+1], Bleft = B[n], Bright = B[n+1] (handle out-of-bounds later)
            Check if we found a median, which is when Aleft <= Bright and Bleft <= Aright.
                If the total_len is odd, then return the min of (Aright, Bright). Otherwise return the max of (Aleft,
                Bleft) + min of (Aright, Bright) / 2.
            Otherwise, if Aleft > Bright, that means we need to make A smaller, so set r = m - 1. Otherwise do l = m
            +1.
        Time: O(log(min(m,n))
        Space: O(1)
        Edge: Handle out-of-bounds stuff.
        '''
        A, B = nums1, nums2
        if len(B) < len(A):
            A, B = B, A
        total_len = len(A) + len(B)
        half_len = total_len // 2
        l, r = 0, len(A)-1
        while True:
            m = (l + r) // 2
            n = half_len - m - 2

            Aleft = A[m] if m >= 0 else float('-inf')
            Aright = A[m+1] if (m+1) < len(A) else float('inf')
            Bleft = B[n] if n >= 0 else float('-inf')
            Bright = B[n+1] if (n+1) < len(B) else float('inf')

            if (Aleft <= Bright) and (Bleft <= Aright):
                # We found the median
                if total_len % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = m - 1
            else:
                l = m + 1

result = Solution()
print(result.findMedianSortedArrays([1,3], [2]))        # 2.00000
print(result.findMedianSortedArrays([1,2], [3,4]))      # 2.50000
