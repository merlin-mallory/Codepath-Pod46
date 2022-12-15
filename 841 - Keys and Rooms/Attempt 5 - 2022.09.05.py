from typing import List
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
        1. Create an unlock_room function. It will take a room_index. It will add room_index to the
        unlocked_rooms_set. It will create a list of all the keys found in
        that room. It will loop through the keys, and if the key is not in the unlocked_rooms_set, then it will
        unlock that room.
        2. Recursively explore all accessible rooms.
        3. At the end, check if the length of the unlocked_rooms_set equals the length of rooms. If there's a match,
        then every room is accessible, so return True. Otherwise return False.
        '''
        unlocked_rooms_set = self.unlock_room(0, set(),rooms)
        return len(unlocked_rooms_set) == len(rooms)

    def unlock_room(self, room_index, unlocked_rooms_set, rooms):
        unlocked_rooms_set.add(room_index)
        for key in rooms[room_index]:
            if key not in unlocked_rooms_set:
                unlocked_rooms_set = self.unlock_room(key, unlocked_rooms_set, rooms)
        return unlocked_rooms_set


result = Solution()
print(result.canVisitAllRooms([[1],[2],[3],[]]))        # True
print(result.canVisitAllRooms([[1,3],[3,0,1],[2],[0]])) # False
