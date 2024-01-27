class Solution:
    def minWindow(self, s: str, t: str) -> str:
        '''
        567 - Minimum Window Substring

        https://leetcode.com/problems/minimum-window-substring/

        Given two strings s and t of lengths m and n respectively, return the minimum window substring of s such that
        every character in t (including duplicates) is included in the window. If there is no such substring, return
        the empty string "".

        The testcases will be generated such that the answer is unique.

        Example 1:

        Input: s = "ADOBECODEBANC", t = "ABC"
        Output: "BANC"
        Explanation: The minimum window substring "BANC" includes 'A', 'B', and 'C' from string t.
        Example 2:

        Input: s = "a", t = "a"
        Output: "a"
        Explanation: The entire string s is the minimum window.
        Example 3:

        Input: s = "a", t = "aa"
        Output: ""
        Explanation: Both 'a's from t must be included in the window.
        Since the largest window of s only has one 'a', return empty string.

        Constraints:

        m == s.length
        n == t.length
        1 <= m, n <= 10^5
        s and t consist of uppercase and lowercase English letters.

        Plan:
        1. Create t_counts dict, initialized with t. Keys: Chars in t, Values: Count of keys.
        2. Create s_window dict, initialized empty. Keys: Chars in s's window, Values: Count of keys.
        3. have = 0, need = len(t_counts)
        4. l = 0, r = 0
        5. min_len = float('inf'), minimum_substring = [-1, -1]
        6. Loop while r < len(s)
            7. Add s[r] to s_window.
            8. Compare s_window[s[r]] and t_counts[s[r]] to see if we need to update "have".
            9. While have == need, loop
                10. Calculate current_len
                11. Update min_len
                12. Remove s[l] from s_window
                13. Compare s_window[s[l]] and t_counts[s[l]] to see if we need to update "have".
                14. l++
            15. r++
        16. Deconstruct minimum_substring and return the desired slice.
        Time: O(n), Space: O(n)
        Edge Cases: Handle min_len = float('inf')
        '''
        import collections
        t_counts = collections.Counter(t)
        s_window = collections.Counter()
        have, need = 0, len(t_counts)
        min_len, min_substring = float('inf'), [-1, -1]
        l, r = 0, 0

        while r < len(s):
            s_window[s[r]] += 1
            if s_window[s[r]] == t_counts[s[r]]:
                have += 1
            while have == need:
                current_len = r - l + 1
                if current_len < min_len:
                    min_substring = [l, r]
                    min_len = current_len
                s_window[s[l]] -= 1
                if s_window[s[l]] < t_counts[s[l]]:
                    have -= 1
                l += 1
            r += 1
        l, r = min_substring
        if min_len == float('inf'):
            return ""
        else:
            return s[l:r+1]


result = Solution()

print(result.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(result.minWindow("a", "a"))               # "a"
print(result.minWindow("a", "aa"))              # ""