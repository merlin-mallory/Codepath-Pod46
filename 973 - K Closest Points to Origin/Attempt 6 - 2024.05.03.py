class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        '''
        973 - K Closest Points to Origin

        https://leetcode.com/problems/k-closest-points-to-origin/

        Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane and an integer k,
        return the k closest points to the origin (0, 0).

        The distance between two points on the X-Y plane is the Euclidean distance (i.e., √(x1 - x2)2 + (y1 - y2)2).

        You may return the answer in any order. The answer is guaranteed to be unique (except for the order that it
        is in).

        Example 1:
        Input: points = [[1,3],[-2,2]], k = 1
        Output: [[-2,2]]
        Explanation:
        The distance between (1, 3) and the origin is sqrt(10).
        The distance between (-2, 2) and the origin is sqrt(8).
        Since sqrt(8) < sqrt(10), (-2, 2) is closer to the origin.
        We only want the closest k = 1 points from the origin, so the answer is just [[-2,2]].

        Example 2:
        Input: points = [[3,3],[5,-1],[-2,4]], k = 2
        Output: [[3,3],[-2,4]]
        Explanation: The answer [[-2,4],[3,3]] would also be accepted.

        Constraints:

        1 <= k <= points.length <= 10^4
        -10^4 <= xi, yi <= 10^4

        Plan:
        Maxheap of size k
        Time: O(n log k)
        Space: O(k)
        Edge: None
        '''
        import heapq
        maxheap = []
        for n1, n2 in points:
            dist = (n1**2) + (n2**2)
            heapq.heappush(maxheap, (-dist, n1, n2))
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        final_arr = []
        for _, n1, n2 in maxheap:
            final_arr.append([n1, n2])
        return final_arr

