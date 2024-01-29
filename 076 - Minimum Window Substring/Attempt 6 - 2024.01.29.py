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
        1 <= m, n <= 105
        s and t consist of uppercase and lowercase English letters.

        Plan:
        Sliding Window
        1. Create t_counts dict, init t. Keys: Chars in window, Values: Count of keys.
        2. Create window dict, init empty. Keys: Chars in window, Values: Count of keys.
        3. Init min_substring = [-1, -1], min_len = float('inf')
        4. have = 0, need = len(t_counts)
        5. l, r = 0, 0
        6. Loop until r > len(s).
            7. Add s[r] to window.
            8. Loop while have == need
                9. Calculate current_len
                10. Update min_len and min_substring
                11. Remove s[l] from window, and l++
        12. Return min_len
        '''

        import collections
        t_counts = collections.Counter(t)
        window = collections.Counter()
        min_substring = [-1, -1]
        min_len = float('inf')
        have, need = 0, len(t_counts)
        l, r = 0, 0

        while r < len(s):
            window[s[r]] += 1

            if window[s[r]] == t_counts[s[r]]:
                have += 1

            while have == need:
                current_len = r - l + 1
                if current_len < min_len:
                    min_len = current_len
                    min_substring = l, r
                min_len = min(min_len, current_len)
                if window[s[l]] == t_counts[s[l]]:
                    have -= 1
                window[s[l]] -= 1
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