class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:
        '''
        https://leetcode.com/problems/keys-and-rooms/

        There are n rooms labeled from 0 to n - 1 and all the rooms are locked except for room 0. Your goal is to
        visit all the rooms. However, you cannot enter a locked room without having its key.

        When you visit a room, you may find a set of distinct keys in it. Each key has a number on it, denoting which
        room it unlocks, and you can take all of them with you to unlock the other rooms.

        Given an array rooms where rooms[i] is the set of keys that you can obtain if you visited room i, return true
        if you can visit all the rooms, or false otherwise.

        Input: rooms = [[1],[2],[3],[]]
        Output: true
        Explanation:
        We visit room 0 and pick up key 1.
        We then visit room 1 and pick up key 2.
        We then visit room 2 and pick up key 3.
        We then visit room 3.
        Since we were able to visit every room, we return true.

        Input: rooms = [[1,3],[3,0,1],[2],[0]]
        Output: false
        Explanation: We can not enter room number 2 since the only key that unlocks it is in that room.

        Constraints:
        n == rooms.length
        2 <= n <= 1000
        0 <= rooms[i].length <= 1000
        1 <= sum(rooms[i].length) <= 3000
        0 <= rooms[i][j] < n
        All the values of rooms[i] are unique.

        Plan:

        1. Create visited_rooms_set.
        2. Recursively explore each room, adding each key to visited_rooms_set, and recursively explore each room
        matching each key.
        3. At the end of the recursion, check if the length of rooms = the length of visited_rooms_set. If they
        match, then we've explored every room, so return true. If there's a mismatch, then return false.
        4. Time: O(n^2), where n is the number of keys in the array.
        5. Space: O(n) for the visited_rooms_set
        '''

        visited_rooms_set = set()
        visited_rooms_set.add(0)

        def helper(visited_rooms_set, rooms, current_index):
            this_rooms_keys = rooms[current_index]

            for key in this_rooms_keys:
                if key not in visited_rooms_set:
                    visited_rooms_set.add(key)
                    visited_rooms_set = helper(visited_rooms_set, rooms, key)
            return visited_rooms_set

        final_visited_rooms_set = helper(visited_rooms_set, rooms, 0)
        return len(final_visited_rooms_set) == len(rooms)
