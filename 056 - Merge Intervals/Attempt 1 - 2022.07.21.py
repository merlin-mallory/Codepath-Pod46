class Solution:
    def merge(self, intervals):
        """
        Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return
        an array of the non-overlapping intervals that cover all the intervals in the input.

        Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
        Output: [[1,6],[8,10],[15,18]]
        Explanation: Since intervals [1,3] and [2,6] overlap, merge them into [1,6].

        Input: intervals = [[1,4],[4,5]]
        Output: [[1,5]]
        Explanation: Intervals [1,4] and [4,5] are considered overlapping.

        Constraints:
        1 <= intervals.length <= 10^4
        intervals[i].length == 2
        0 <= starti <= endi <= 10^4

        1. Create an interval_queue, final_arr, loop through intervals, and add everything to the queue.
        2. Pop the queue, and loop through final_arr. If the popped min or max is in final_arr, then merge the popped
        interval with that index in final_arr, and break the loop. Otherwise, add a new list to the final arr with
        the popped interval.
        3. Keep going until the queue is empty.
        """

        intervals.sort(key=lambda x: x[0])

        merged = []
        for interval in intervals:
            # if the list of merged intervals is empty or if the current
            # interval does not overlap with the previous, simply append it.
            if not merged or merged[-1][1] < interval[0]:
                merged.append(interval)
            else:
                # otherwise, there is overlap, so we merge the current and previous
                # intervals.
                merged[-1][1] = max(merged[-1][1], interval[1])

        return merged

        # My failed attempt at O(n^2):
        # if not intervals:
        #     return []
        #
        # final_arr = intervals[0]
        #
        # for i in range(1, len(intervals)):
        #     cur_min, cur_max = intervals[i][0], intervals[i][1]
        #     j_modified = False
        #     for j in range(len(final_arr)):
        #         comp_min, comp_max = intervals[j][0], intervals[j][1]
        #         if cur_min >= comp_min and cur_min <= comp_max or cur_max >= comp_min:
        #             new_min = min(comp_min, cur_min)
        #             new_max = max(comp_max, cur_max)
        #             final_arr[j][0] = new_min
        #             final_arr[j][1] = new_max
        #             j_modified = True
        #             break
        #     if j_modified is not True:
        #         final_arr.append([cur_min, cur_max])
        #
        # return final_arr

result = Solution()
print(result.merge([[1,3],[2,6],[8,10],[15,18]]))
print(result.merge([[1,4],[4,5]]))
# print(result.merge([]))
# print(result.merge([]))
# print(result.merge([]))
# print(result.merge([]))



