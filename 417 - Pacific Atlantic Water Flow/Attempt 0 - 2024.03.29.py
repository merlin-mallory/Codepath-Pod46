from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        '''
        417 - Pacific Atlantic Water Flow

        https://leetcode.com/problems/pacific-atlantic-water-flow/

        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean
        touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

        The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where
        heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

        The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south,
        east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water
        can flow from any cell adjacent to an ocean into the ocean.

        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from
        cell (ri, ci) to both the Pacific and Atlantic oceans.

        Example 1:
        Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
        Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
        Explanation: The following cells can flow to the Pacific and Atlantic oceans, as shown below:
        [0,4]: [0,4] -> Pacific Ocean
               [0,4] -> Atlantic Ocean
        [1,3]: [1,3] -> [0,3] -> Pacific Ocean
               [1,3] -> [1,4] -> Atlantic Ocean
        [1,4]: [1,4] -> [1,3] -> [0,3] -> Pacific Ocean
               [1,4] -> Atlantic Ocean
        [2,2]: [2,2] -> [1,2] -> [0,2] -> Pacific Ocean
               [2,2] -> [2,3] -> [2,4] -> Atlantic Ocean
        [3,0]: [3,0] -> Pacific Ocean
               [3,0] -> [4,0] -> Atlantic Ocean
        [3,1]: [3,1] -> [3,0] -> Pacific Ocean
               [3,1] -> [4,1] -> Atlantic Ocean
        [4,0]: [4,0] -> Pacific Ocean
               [4,0] -> Atlantic Ocean
        Note that there are other possible paths for these cells to flow to the Pacific and Atlantic oceans.

        Example 2:
        Input: heights = [[1]]
        Output: [[0,0]]
        Explanation: The water can flow from the only cell to the Pacific and Atlantic oceans.

        Constraints:

        m == heights.length
        n == heights[r].length
        1 <= m, n <= 200
        0 <= heights[r][c] <= 10^5

        Time: O(2*m*n)
        Space: O(2*m*n)
        Edge: None
        '''
        rows = len(heights)
        cols = len(heights[0])
        pacific_set = set()
        atlantic_set = set()

        # Explore function has 4 parameters: row, col, the set being used during the exploration (either pacific or
        # atlantic), and the previous height.
        # Explore function has 6 base cases: 4 out-of-bounds checks, the relevant visited_set check, and also a
        # comparison of the cur_height with prev_height. All of these return None.
        # Then we immediately add the (r,c) pair to the visited set.
        # Then we expand the exploration in 4 directions. At each call we'll change the coordinates, but pass down
        # the same visited_set and heights[r][c] as the previous height value.
        # There will be no return statement, the goal of the explore function is simply to fill up the pacific_set
        # and atlantic_set.
        def explore(r, c, visited_set, prev_height):
            if (((r,c)) in visited_set or (r < 0) or (c < 0) or (r == rows) or (c == cols) or heights[r][c] <
                    prev_height):
                return
            visited_set.add((r,c))
            explore(r+1, c, visited_set, heights[r][c])
            explore(r-1, c, visited_set, heights[r][c])
            explore(r, c+1, visited_set, heights[r][c])
            explore(r, c-1, visited_set, heights[r][c])

        # Iteratively explore from the left edge (Pacific Ocean) and right edge (Atlantic Ocean)
        for r in range(rows):
            explore(r, 0, pacific_set, heights[r][0])
            explore(r, cols-1, atlantic_set, heights[r][cols - 1])

        # Iteratively explore from the top edge (Pacific Ocean) and bottom edge (Atlantic Ocean)
        for c in range(cols):
            explore(0, c, pacific_set, heights[0][c])
            explore(rows-1, c, atlantic_set, heights[rows-1][c])

        # Append the intersection of the pacific_set and atlantic_set to final_arr, and return.
        final_arr = []
        for r, c in pacific_set:
            if (r,c) in atlantic_set:
                final_arr.append([r,c])
        return final_arr


solution = Solution()

grid1 = [
    [1, 2, 2, 3, 5],
    [3, 2, 3, 4, 4],
    [2, 4, 5, 3, 1],
    [6, 7, 1, 4, 5],
    [5, 1, 1, 2, 4]]
print(solution.pacificAtlantic(grid1))
# [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

grid2 = [
    [1]
]
print(solution.pacificAtlantic(grid2))
# [[0,0]]
