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
        Maxheap
        Create maxheap.
        Create final_arr.
        Loop through points
            Heappush [-distance, x, y] to the maxheap
            if len(maxheap) > k, heappop and discard
        Loop through maxheap.
            Append [x,y] to final_arr
        Return final_arr
        Time: O(n log k)
        Space: O(k)
        Edge: None
        '''
        import heapq, math
        max_heap = []
        final_arr = []
        for i in range(len(points)):
            dist = math.sqrt((points[i][0] ** 2 + points[i][1] ** 2))
            heapq.heappush(max_heap, [-dist, points[i][0], points[i][1]])
            if len(max_heap) > k:
                heapq.heappop(max_heap)
        for _, x, y in max_heap:
            final_arr.append([x, y])
        return final_arr
