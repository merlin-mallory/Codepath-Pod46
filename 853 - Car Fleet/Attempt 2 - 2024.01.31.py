from typing import List
class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        '''
        There are n cars going to the same destination along a one-lane road. The destination is target miles away.

        You are given two integer array position and speed, both of length n, where position[i] is the position of the
        ith car and speed[i] is the speed of the ith car (in miles per hour).

        A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the
        same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars
        is ignored (i.e., they are assumed to have the same position).

        A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car
        is also a car fleet.

        If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

        Return the number of car fleets that will arrive at the destination.

        Example 1:
        Input: target = 12, position = [10,8,0,5,3], speed = [2,4,1,1,3]
        Output: 3
        Explanation:
        The cars starting at 10 (speed 2) and 8 (speed 4) become a fleet, meeting each other at 12.
        The car starting at 0 does not catch up to any other car, so it is a fleet by itself.
        The cars starting at 5 (speed 1) and 3 (speed 3) become a fleet, meeting each other at 6. The fleet moves at
        speed 1 until it reaches target.
        Note that no other cars meet these fleets before the destination, so the answer is 3.

        Example 2:
        Input: target = 10, position = [3], speed = [3]
        Output: 1
        Explanation: There is only one car, hence there is only one fleet.

        Example 3:
        Input: target = 100, position = [0,2,4], speed = [4,2,1]
        Output: 1
        Explanation:
        The cars starting at 0 (speed 4) and 2 (speed 2) become a fleet, meeting each other at 4. The fleet moves at
        speed 2.
        Then, the fleet (speed 2) and the car starting at 4 (speed 1) become one fleet, meeting each other at 6. The
        fleet moves at speed 1 until it reaches target.

        Constraints:
        n == position.length == speed.length
        1 <= n <= 10^5
        0 < target <= 10^6
        0 <= position[i] < target
        All the values of position are unique.
        0 < speed[i] <= 10^6

        Plan:
        Stack
        1. stack = [], cars = [] (will hold subarrays containing [position[i], speed[i]])
        2. Reverse sort cars, so the car in the position closest to the target will be in the zero-index.
        3. Loop through cars, from the closest car to the target, to the furthest car from the target.
            4. Append time_finished ((target - pos)/speed) to the stack.
            5. If there are 2 or more elements on the stack, then compare stack[-1] with stack[-2]. If stack[-1]'s
            time_finished is less than stack[-2], then that means they will form a car fleet before the destination
            is reached. So stack.pop(). Otherwise, we've found a new fleet, and we'll use that time_finished to
            compare with subsequent cars to see if they form extra fleets, so we'll just let the len of stack
            increase by 1.
        6. Return the len of the stack.
        '''
        stack = []
        cars = []
        for i in range(len(speed)):
            cars.append([position[i], speed[i]])
        cars = sorted(cars)[::-1]

        for pos, speed in cars:
            stack.append((target - pos)/speed)
            if len(stack) >= 2 and stack[-1] <= stack[-2]:
                stack.pop()
        return len(stack)



result = Solution()
print(result.carFleet(12, [10,8,0,5,3], [2,4,1,1,3]))   # 3
print(result.carFleet(10, [3], [3]))                    # 1
print(result.carFleet(100, [0,2,4], [4,2,1]))           # 1
