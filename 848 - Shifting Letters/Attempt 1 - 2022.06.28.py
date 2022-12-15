class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        '''
        https://leetcode.com/problems/shifting-letters/
        You are given a string s of lowercase English letters and an integer array shifts of the same length.
        Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

        For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

        Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.
        Return the final string after all such shifts to s are applied.

        Input: s = "abc", shifts = [3,5,9]
        Output: "rpl"
        Explanation:
        We start with "abc".
        After shifting the first 1 letters of s by 3, we have "dbc".
        After shifting the first 2 letters of s by 5, we have "igc".
        After shifting the first 3 letters of s by 9, we have "rpl", the answer.

        Input: s = "aaa", shifts = [1,2,3]
        Output: "gfd"

        Constraints:
        1 <= s.length <= 105
        s consists of lowercase English letters.
        shifts.length == s.length
        0 <= shifts[i] <= 109

        Plan 1:
        1. Construct a dictionary, mapping each char to its +1 shift.
        2. Loop through s and shifts, doing k dict calls on every letter
        '''


        letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h',
                   'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q',
                   'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

        new_string = []
        index = 0
        sum_current = sum(shifts)
        for i in s:
            index_of_letter = letters.index(i)
            if index != 0:
                sum_current -= shifts[index - 1]
            index_of_letter += sum_current
            new_string.append(letters[index_of_letter % 26])
            index += 1

        return ''.join(new_string)

        # final_arr = []
        # actual_shift = sum(shifts) % 26
        # for i, char in enumerate(s):
        #     index = ord(char) - ord('a')
        #     final_arr.append(chr(ord('a') + (index + actual_shift) % 26))
        #     actual_shift = (actual_shift - shifts[i]) % 26
        # return "".join(final_arr)
