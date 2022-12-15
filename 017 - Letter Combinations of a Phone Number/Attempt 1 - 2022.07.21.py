class Solution:
    def letterCombinations(self, digits):
        """
        https://leetcode.com/problems/letter-combinations-of-a-phone-number/

        Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number
        could represent. Return the answer in any order.

        A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map
        to any letters.

        Constraints:
        0 <= digits.length <= 4
        digits[i] is a digit in the range ['2', '9'].

        Plan:
        1. Create a mapping_dict. Keys: digits, values: List of string characters.
        2. Create a final_arr. Iterate through the string and recursively add characters to create a substring. When
        len(substring) == len(digits), append that substring and return up the call stack.
        """
        # If the input is empty, immediately return an empty answer array
        if len(digits) == 0:
            return []

        # Map all the digits to their corresponding letters
        letters = {"2": "abc", "3": "def", "4": "ghi", "5": "jkl",
                   "6": "mno", "7": "pqrs", "8": "tuv", "9": "wxyz"}

        def backtrack(index, path):
            # If the path is the same length as digits, we have a complete combination
            if len(path) == len(digits):
                combinations.append("".join(path))
                return  # Backtrack

            # Get the letters that the current digit maps to, and loop through them
            possible_letters = letters[digits[index]]
            for letter in possible_letters:
                # Add the letter to our current path
                path.append(letter)
                # Move on to the next digit
                backtrack(index + 1, path)
                # Backtrack by removing the letter before moving onto the next
                path.pop()

        # Initiate backtracking with an empty path and starting index of 0
        combinations = []
        backtrack(0, [])
        return combinations

        # Failed attempt at BFS solution
        # import collections
        #
        # if len(digits) == 0:
        #     return []
        #
        # mapping_dict = {
        #     "2": ["a", "b", "c"],
        #     "3": ["d", "e", "f"],
        #     "4": ["g", "h", "i"],
        #     "5": ["j", "k", "l"],
        #     "6": ["m", "n", "o"],
        #     "7": ["p", "q" , "r", "s"],
        #     "8": ["t", "u", "v"],
        #     "9": ["w", "x", "y", "z"]
        #     }
        #
        # if len(digits) == 1:
        #     return mapping_dict[0]
        #
        # substring = ""
        # final_arr = []
        #
        # queue = collections.deque([digits[0]])
        # while queue:
        #     result = queue.popleft()
        #     for letter in result:
        #         substring += letter
        #         if len(substring) == len(digits):
        #             final_arr.append(substring)
        #             substring = substring[:-1]
        #             continue
        #         else:
        #             queue.append(substring)
        #             substring = substring[:-1]
        #
        # return final_arr



        # Failed attempt at DFS recursive solution
        # if len(digits) == 0:
        #     return []
        #
        # mapping_dict = {
        #     "2": ["a", "b", "c"],
        #     "3": ["d", "e", "f"],
        #     "4": ["g", "h", "i"],
        #     "5": ["j", "k", "l"],
        #     "6": ["m", "n", "o"],
        #     "7": ["p", "q" , "r", "s"],
        #     "8": ["t", "u", "v"],
        #     "9": ["w", "x", "y", "z"]
        #     }
        #
        # if len(digits) == 1:
        #     return mapping_dict.get(digits[0])
        #
        # def helper(substring, mapping_dict, current_digit_index, digits, final_arr):
        #     # if len(substring) == len(digits):
        #     #     final_arr.append(substring)
        #     #     return final_arr
        #
        #     current_list = mapping_dict.get(digits[current_digit_index])
        #
        #     for i in range(len(current_list)):
        #         substring += current_list[i]
        #         if current_digit_index + 1 <= len(digits)-1:
        #             final_arr = helper(substring, mapping_dict, current_digit_index + 1, digits, final_arr)
        #         else:
        #             final_arr.append(substring)
        #             return final_arr
        #
        #     return final_arr
        #
        # return helper("", mapping_dict, 0, digits, [])



result = Solution()
print(result.letterCombinations("23"))  # ["ad","ae","af","bd","be","bf","cd","ce","cf"]
print(result.letterCombinations(""))  # []
print(result.letterCombinations("2"))  # ["a","b","c"]