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
        Hashmap
        1. Initialize l = 0, r = 0, len_of_longest_substring = 0, current_window = set()
        2. Loop while r < len(s).
            3. Check if s[r] in current_window. If so, then iterate and remove s[l] from the set until s[r] is not in
            the current window.
            4. Add s[r] to the current window
            5. Calculate the current_window_len = r - l +1
            6. Update the len_of_longest_substring.
        7. Return len_of_longest_substring.
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
