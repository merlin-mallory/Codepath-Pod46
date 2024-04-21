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
    Time: O(log n) for addnum, O(1) for findMedian
    Space: O(n), where n = total number of nums added
    Edge: None

    Follow-Up Scenarios Optimization Discussion
    All Integers in the Range [0, 100]:
    If all integers are guaranteed to be within a specific small range (e.g., [0, 100]), using two heaps might not be
    the most space-efficient method. An alternative could be using a counting sort-like approach with an array of size
    101 (for each possible value between 0 and 100). Each entry in this array would count the number of times a number
    appears. This would allow for constant-time updates (O(1)) and potentially faster median finding by iterating over
    the array to find the middle value based on counts, especially efficient if there's a high frequency of certain
    numbers.
    99% of Integers in the Range [0, 100]:
    For scenarios where most but not all numbers fall within a certain range, a hybrid approach could be utilized.
    Maintain a counting array for the common range and use heaps for numbers outside of that range. This method would
    handle the bulk of data efficiently with the array, while still accommodating outliers with heaps. This would
    reduce the number of elements in the heaps and improve performance for both addNum and findMedian operations for
    the majority of inputs.
    '''

    def __init__(self):
        ''''''
        self.left_max_heap = []
        self.right_min_heap = []
        self.total_len = 0

    def addNum(self, num: int) -> None:
        ''''''
        import heapq
        if (not self.left_max_heap) or (num <= -self.left_max_heap[0]):
            heapq.heappush(self.left_max_heap, -num)
        else:
            heapq.heappush(self.right_min_heap, num)

        if len(self.left_max_heap) > (len(self.right_min_heap) + 1):
            heapq.heappush(self.right_min_heap, -heapq.heappop(self.left_max_heap))
        elif len(self.right_min_heap) > (len(self.left_max_heap) + 1):
            heapq.heappush(self.left_max_heap, -heapq.heappop(self.right_min_heap))

        self.total_len += 1

    def findMedian(self) -> float:
        ''''''
        if self.total_len % 2 == 1:
            if len(self.left_max_heap) > len(self.right_min_heap):
                return -self.left_max_heap[0]
            else:
                return self.right_min_heap[0]
        else:
            return (-self.left_max_heap[0] + self.right_min_heap[0]) / 2

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()
