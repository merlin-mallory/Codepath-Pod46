class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """
        https://leetcode.com/problems/longest-substring-without-repeating-characters/

        Given a string s, find the length of the longest substring without repeating characters.

        Input: s = "abcabcbb"
        Output: 3
        Explanation: The answer is "abc", with the length of 3.

        Input: s = "bbbbb"
        Output: 1
        Explanation: The answer is "b", with the length of 1.

        Input: s = "pwwkew"
        Output: 3
        Explanation: The answer is "wke", with the length of 3.
        Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

        Constraints:
        0 <= s.length <= 5 * 10^4
        s consists of English letters, digits, symbols and spaces.

        Plan:
        Sliding Window
        1. Create s_set, initialized to empty. This will contain the chars in the current window.
        2. Create max_len, current_len
        3. Loop through s.
            4. If s[i] in s_set, then we need to reset current_len to 1, reinitialize s_set, and append s[i]
            5. Otherwise, add s[i] to s_set, and current_len ++, and update max_len.
        6. Return max_len
        Edge Case: len(s) == 0
        """
        if len(s) == 0:
            return 0

        l, r = 0, 0
        len_of_longest_substring = 0
        current_window = set()

        while r < len(s):
            while s[r] in current_window:
                current_window.remove(s[l])
                l += 1

            current_window.add(s[r])

            current_window_len = r - l + 1
            len_of_longest_substring = max(len_of_longest_substring, current_window_len)
            r += 1
        return len_of_longest_substring



result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
