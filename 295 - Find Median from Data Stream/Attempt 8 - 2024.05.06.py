class MedianFinder:
    '''
    295 - Find Median from Data Stream

    https://leetcode.com/problems/find-median-from-data-stream/

    The median is the middle value in an ordered integer list. If the size of the list is even, there is no middle
    value, and the median is the mean of the two middle values.

    For example, for arr = [2,3,4], the median is 3.
    For example, for arr = [2,3], the median is (2 + 3) / 2 = 2.5.
    Implement the MedianFinder class:

    MedianFinder() initializes the MedianFinder object.
    void addNum(int num) adds the integer num from the data stream to the data structure.
    double findMedian() returns the median of all elements so far. Answers within 10^-5 of the actual answer will be
    accepted.

    Example 1:
    Input
    ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    [[], [1], [2], [], [3], []]
    Output
    [null, null, null, 1.5, null, 2.0]
    Explanation:
    MedianFinder medianFinder = new MedianFinder();
    medianFinder.addNum(1);    // arr = [1]
    medianFinder.addNum(2);    // arr = [1, 2]
    medianFinder.findMedian(); // return 1.5 (i.e., (1 + 2) / 2)
    medianFinder.addNum(3);    // arr[1, 2, 3]
    medianFinder.findMedian(); // return 2.0

    Constraints:
    -10^5 <= num <= 10^5
    There will be at least one element in the data structure before calling findMedian.
    At most 5 * 104 calls will be made to addNum and findMedian.

    Follow up:
    If all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?
    If 99% of all integer numbers from the stream are in the range [0, 100], how would you optimize your solution?

    Plan:
    Minheap and Maxheap
    Time: O(n log n) for addNum, O(1) for findMedian
    Space: O(n) for addNum, O(1) for findMedian
    Edge: None
    '''

    def __init__(self):
        ''''''
        self.left_maxheap = []
        self.right_minheap = []

    def addNum(self, num: int) -> None:
        ''''''
        import heapq
        if not self.left_maxheap or (num < -self.left_maxheap[0]):
            heapq.heappush(self.left_maxheap, -num)
        else:
            heapq.heappush(self.right_minheap, num)

        if len(self.left_maxheap) > (len(self.right_minheap) + 1):
            heapq.heappush(self.right_minheap, -heapq.heappop(self.left_maxheap))
        elif len(self.right_minheap) > (len(self.left_maxheap) + 1):
            heapq.heappush(self.left_maxheap, -heapq.heappop(self.right_minheap))

    def findMedian(self) -> float:
        ''''''
        if (len(self.left_maxheap) + len(self.right_minheap)) % 2 == 1:
            if len(self.left_maxheap) > len(self.right_minheap):
                return -self.left_maxheap[0]
            else:
                return self.right_minheap[0]
        else:
            return (-self.left_maxheap[0] + self.right_minheap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
