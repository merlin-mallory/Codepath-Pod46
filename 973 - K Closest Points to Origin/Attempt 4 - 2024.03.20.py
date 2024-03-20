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
        Heap
        Maxheap of size k to collect the k closest points to the origin.
        Create maxheap.
        Loop through points, and append [-math.sqrt(x**2 + y**2), x, y] to maxheap.
        Heapify maxheap
        Calc diff = len(maxheap) - k
        Loop diff times.
            Heappop
        Create final_arr
        Loop through maxheap and append [x,y] pairs to final_arr.
        Return final_arr
        Time: O(n log n)
        Space: O(n)
        Edge: None
        '''
        import heapq, math
        maxheap = []
        for x, y in points:
            maxheap.append([-math.sqrt(x**2 + y**2), x, y])
        heapq.heapify(maxheap)
        diff = len(maxheap) - k
        for _ in range(diff):
            heapq.heappop(maxheap)
        final_arr = []
        for _, x, y in maxheap:
            final_arr.append([x, y])
        return final_arr
