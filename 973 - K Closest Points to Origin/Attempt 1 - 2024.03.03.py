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
        Minheap
        Create a minheap.
        Loop through points, grab cur_x and cur_y, heappush [(sqrt(cur_x)**2 + sqrt(cur_y)**2), cur_x, cur_y],
        and if len(minheap) > k, heappop.
        Create final arr, empty the heap and append [cur_x, cur_y] pairs to final_arr.
        Return final_arr.
        Time: O(n) or O(n log n)
        Space: O(n)
        Edge: None
        '''
        import heapq, math
        maxheap = []
        for coords in points:
            cur_x, cur_y = coords
            heapq.heappush(maxheap, [-(math.sqrt(cur_x** 2 + cur_y**2)), cur_x, cur_y])
            if len(maxheap) > k:
                heapq.heappop(maxheap)
        final_arr = []
        while maxheap:
            _, cur_x, cur_y = heapq.heappop(maxheap)
            final_arr.append([cur_x, cur_y])
        return final_arr
