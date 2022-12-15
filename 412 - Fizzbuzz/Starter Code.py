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
        """

result = Solution()
print(result.fizzBuzz(3))  # ["1","2","Fizz"]
print(result.fizzBuzz(5))  # ["1","2","Fizz","4","Buzz"]
print(result.fizzBuzz(15))  # ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
