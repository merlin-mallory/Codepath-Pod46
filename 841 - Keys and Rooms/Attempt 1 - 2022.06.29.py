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
        1. Calculate the number of rooms, len(rooms).
        2. Create a set that will contain visited_rooms_set. The values will be indexes corresponding to rooms.
        3. Create a helper function that will take a room index, unlock the room index, add the room index to the
        visited_rooms_set, and recursively explore every key's room. Each recursive call will return the updated
        visited_rooms_set.
        4. Call the helper function on room 0, and set it equal to visited_rooms_set.
        5. Compare the length of visited_room_set to number_of_rooms. If they're equal, then we've explored all of
        the rooms, so return True. Otherwise, return False.
        6. Time: O(n), Space: O(n). The keys are distinct, so we will never exceed n recursive calls.
        '''

        visited_rooms_set = set()

        def unlock_room(room, visited_rooms_set):
            this_rooms_keys = rooms[room]
            visited_rooms_set.add(room)

            for key in this_rooms_keys:
                if key not in visited_rooms_set:
                    visited_rooms_set = unlock_room(key, visited_rooms_set)

            return visited_rooms_set

        visited_rooms_set = unlock_room(0, visited_rooms_set)
        if len(visited_rooms_set) == len(rooms):
            return True
        else:
            return False
