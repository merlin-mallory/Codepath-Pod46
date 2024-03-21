class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        '''
        621 - Task Scheduler

        https://leetcode.com/problems/task-scheduler/

        You are given an array of CPU tasks, each represented by letters A to Z, and a cooling time, n. Each cycle or
        interval allows the completion of one task. Tasks can be completed in any order, but there's a constraint:
        identical tasks must be separated by at least n intervals due to cooling time.
        
        Return the minimum number of intervals required to complete all tasks.

        Example 1:
        Input: tasks = ["A","A","A","B","B","B"], n = 2
        Output: 8
        Explanation: A possible sequence is: A -> B -> idle -> A -> B -> idle -> A -> B.

        After completing task A, you must wait two cycles before doing A again. The same applies to task B. In the 3rd
        interval, neither A nor B can be done, so you idle. By the 4th cycle, you can do A again as 2 intervals have
        passed.

        Example 2:
        Input: tasks = ["A","C","A","B","D","B"], n = 1
        Output: 6

        Explanation: A possible sequence is: A -> B -> C -> D -> A -> B.
        With a cooling interval of 1, you can repeat a task after just one other task.

        Example 3:
        Input: tasks = ["A","A","A", "B","B","B"], n = 3
        Output: 10
        Explanation: A possible sequence is: A -> B -> idle -> idle -> A -> B -> idle -> idle -> A -> B.

        There are only two types of tasks, A and B, which need to be separated by 3 intervals. This leads to idling
        twice between repetitions of these tasks.

        Constraints:
        1 <= tasks.length <= 10^4
        tasks[i] is an uppercase English letter.
        0 <= n <= 100

        Plan:
        Heap to grab the largest count task, Deque to manage the cooling time
        Create tasks_counts dict. Init with tasks.
        Negify tasks_counts.values, create maxheap.
        Create deque.
        Set time = 0
        Loop while maxheap or deque.
            time++
            if maxheap:
                Heappop maxheap, set to cur_count.
                If cur_count != -1, then append [cur_count-1, time+n] to the deque.
            if deque:
                if deque[-1][1] == time, deque.popleft and heappush(deque[-1][0])
        Return time
        Time: O(n log n) but not sure
        Space: O(n)
        Edge: n could be 0
        '''
        import collections, heapq
        tasks_counts = collections.Counter(tasks)
        maxheap = tasks_counts.values()
        maxheap = [-val for val in maxheap]
        heapq.heapify(maxheap)
        deque = collections.deque()
        time = 0
        while maxheap or deque:
            time += 1
            if maxheap:
                cur_count = heapq.heappop(maxheap)
                if cur_count != -1: deque.append([cur_count+1, time+n])
            if deque:
                if deque[0][1] <= time:
                    cur_count, _ = deque.popleft()
                    heapq.heappush(maxheap, cur_count)
        return time
