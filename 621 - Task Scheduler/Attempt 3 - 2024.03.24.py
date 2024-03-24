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
        Heap
        Create cd_deque.
        Create tasks counter dict.
        Set maxheap = tasks.values()
        Negify maxheap.
        Heapify maxheap.
        time = 0
        Loop while maxheap or cd_deque
            time += 1
            if maxheap:
                val = heappop(maxheap)
                if val != -1:
                    cd_deque.append([val-1, time+n])
            if cd_deque:
                if time >= cd_deque[0][1]:
                    val, time = cd_deque.popleft()
                    heappush(val)
        return time
        Time: O(n log n)
        Space: O(n)
        Edge: None
        '''
        import collections, heapq
        tasks_dict = collections.Counter(tasks)
        maxheap = tasks_dict.values()
        maxheap = [-val for val in maxheap]
        heapq.heapify(maxheap)
        time = 0
        cd_deque = collections.deque()
        while maxheap or cd_deque:
            time += 1
            if maxheap:
                val = heapq.heappop(maxheap)
                if val != -1:
                    cd_deque.append([val+1, time+n])
            if cd_deque:
                if time >= cd_deque[0][1]:
                    val, _ = cd_deque.popleft()
                    heapq.heappush(maxheap, val)
        return time
