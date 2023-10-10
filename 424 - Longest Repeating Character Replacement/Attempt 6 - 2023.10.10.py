class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        https://leetcode.com/problems/longest-repeating-character-replacement/

        You are given a string s and an integer k.
        You can choose any character of the string and change it to any other uppercase English character.
        You can perform this operation at most k times.

        Return the length of the longest substring containing the same letter you can get after performing the above
        operations.

        Input: s = "ABAB", k = 2
        Output: 4
        Explanation: Replace the two 'A's with two 'B's or vice versa.

        Input: s = "AABABBA", k = 1
        Output: 4
        Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
        The substring "BBBB" has the longest repeating letters, which is 4.

        Constraints:

        1 <= s.length <= 105
        s consists of only uppercase English letters.
        0 <= k <= s.length

        1. Create a counts dictionary of letters in s
        2. Loop through counts to find the letter with the highest frequency.
        3. Loop through s while k > 0, if current_char != highest_char, then k--. Otherwise,
        '''

        # Failed attempt

        chars_dict = {}
        for char in s:
            if char not in chars_dict:
                chars_dict[char] = 1
            else:
                chars_dict[char] += 1

        max_char_count = 0
        max_char = "null"

        for key in chars_dict:
            if chars_dict[key] > max_char_count:
                max_char = key

        current_substring_len =0
        max_substring_len = 0

        for char in s:
            if k == 0:
                break
            if char != max_char:
                current_substring_len += 1
                if current_substring_len > max_substring_len:
                    max_substring_len = current_substring_len
                k = k - 1
            elif char == max_char:
                current_substring_len += 1
                if current_substring_len > max_substring_len:
                    max_substring_len = current_substring_len

        return max_substring_len



result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

