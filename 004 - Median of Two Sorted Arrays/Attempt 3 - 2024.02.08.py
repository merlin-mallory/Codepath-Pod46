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
        Compare the lengths of nums1 and nums2. Lets set the smaller size array to A, and the larger size array to B.
        We'll binary search the smaller array to attempt to find the median value there. We'll use that mid value to
        calcuate the index that we'll need to consider in the larger array, in order to maintain an equal size len.
        If the len of the total_arr is odd, then we'll calculate the median as the maximum of the 2 left values.
        Otherwise, we'll calculate the median as the (max of the two left values + min of the two right values) / 2.
        Time: O(log(n))
        Space: O(1)
        Edge: None
        '''
        A, B = nums1, nums2
        total_len = len(nums1) + len(nums2)
        half_len = total_len // 2
        if len(nums2) < len(nums1):
            A, B = B, A
        # A is the shorter list, B is the longer list.
        l, r = 0, len(A)-1
        while True:
            m = (l + r) // 2
            n = half_len - m - 2

            A_left = A[m] if m >= 0 else float('-inf')
            A_right = A[m+1] if (m+1) < len(A) else float('inf')
            B_left = B[n] if n >= 0 else float('-inf')
            B_right = B[n+1] if (n+1) < len(B) else float('inf')

            if (A_left <= B_right) and (B_left <= A_right):
                # We found the median
                if total_len % 2 == 1:
                    return min(A_right, B_right)
                else:
                    return (max(A_left, B_left) + min(A_right, B_right)) / 2
            elif A_left > B_right:
                # We need to reduce A in size
                r = m - 1
            else:
                l = m + 1

result = Solution()
print(result.findMedianSortedArrays([1,3], [2]))        # 2.00000
print(result.findMedianSortedArrays([1,2], [3,4]))      # 2.50000
