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
        1. Handle len(0)
        2. l = 0, r = 0, len_of_longest_substring = 0, set_of_window = ()
        3. while r < len(s)
            4. len_of_current_substring = r - l + 1
            5. if s[r] not in set_of_window:
                6. set_of_window.add(s[r])
                7. len_of_longest_substring = max(len_of_longest_substring, len_of_current_substring)
                8. r += 1
            9. else
                10. set_of_window.remove(s[l])
                11. l += 1
        12. return len_of_longest_substring
        """

        l, r = 0, 0
        len_of_longest_substring = 0
        set_of_window = set()

        while r < len(s):
            len_of_current_substring = r - l + 1
            if s[r] not in set_of_window:
                set_of_window.add(s[r])
                len_of_longest_substring = max(len_of_longest_substring, len_of_current_substring)
                r += 1
            else:
                while s[r] in set_of_window:
                    set_of_window.remove(s[l])
                    l += 1
        return len_of_longest_substring



result = Solution()
print(result.lengthOfLongestSubstring("abcabcbb"))  # 3
print(result.lengthOfLongestSubstring("bbbbb"))     # 1
print(result.lengthOfLongestSubstring("pwwkew"))    # 3
