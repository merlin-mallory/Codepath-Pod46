from typing import List
class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        """
        Given an integer n, return a string array answer (1-indexed) where:

        answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
        answer[i] == "Fizz" if i is divisible by 3.
        answer[i] == "Buzz" if i is divisible by 5.
        answer[i] == i (as a string) if none of the above conditions are true.

        Input: n = 3
        Output: ["1","2","Fizz"]

        Input: n = 5
        Output: ["1","2","Fizz","4","Buzz"]

        Input: n = 15
        Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]

        Constraints:
        1 <= n <= 10^4

        Plan:
        1. Create a loop that will go from (1, n). Create a final_arr.
        2. At each iteration, run through all of the conditions in order to figure out which one to append to the
        final array.
        3. Return the final array.
        4. Time: O(n). Space: O(n).
        """
        final_arr = []

        for i in range(1, n+1):
            if (i % 3 == 0) and (i % 5 == 0):
                final_arr.append("FizzBuzz")
            elif (i % 3 == 0):
                final_arr.append("Fizz")
            elif (i % 5 == 0):
                final_arr.append("Buzz")
            else:
                final_arr.append(str(i))

        return final_arr

result = Solution()
print(result.fizzBuzz(3))  # ["1","2","Fizz"]
print(result.fizzBuzz(5))  # ["1","2","Fizz","4","Buzz"]
print(result.fizzBuzz(15))  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
