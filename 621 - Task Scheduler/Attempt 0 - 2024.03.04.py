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
        Maxheap and Queue.
        Create tasks_dict. Keys: Unique chars in tasks, Values: Count of keys.
        Create maxheap and deque.
        Negify tasks_dict.values()
        Heapify tasks_dict.values().
        Set time = 0
        Loop while maxheap or cd_deque.
            time += 1
            if maxheap:
                new_count = 1 + heapq.heappop(maxheap)
                if new_count != 0:
                    deque.append([new_count, time+n])
            if cd_deque and cd_deque[0][1] == time:
                heapq.heappush(maxheap, cd_deque.popleft()[0])
        return time
        '''
        import collections, heapq
        count = collections.Counter(tasks)
        max_heap = [-val for val in count.values()]
        heapq.heapify(max_heap)
        time = 0
        q = collections.deque()
        while max_heap or q:
            time += 1
            if max_heap:
                new_count = 1 + heapq.heappop(max_heap)
                if new_count != 0:
                    q.append([new_count, time + n])
            if q and q[0][1] == time:
                heapq.heappush(max_heap, q.popleft()[0])
        return time
