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
        1. Way to check that substring is valid: t_dict[i] <= s_dict[i].
        2. Way to compare lengths. (r - l - 1) compared to min_len.
        3. We need to loop through the entirety of s to make sure that we've found the minimum window.
        4. We need to add s[r] to s_dict each r++, and subtract s[l] from s_dict each l--.
        5. After we find a matching substring, we should advance l until we no longer have a matching substring. We
        need to remove [s]l from s_dict each iteration.
        6. Handle edge case of len(t) > len(s).
        '''
        import collections

        if (len(t) > len(s)) or (t == ""):
            return ""

        t_dict = collections.Counter(t)
        s_dict = collections.Counter()

        have, need = 0, len(t_dict)

        len_of_min_win_substring = float('inf')
        min_win_substring = [-1, -1]
        l = 0

        for r in range(len(s)):
            current_char = s[r]
            s_dict[current_char] += 1

            if (current_char in t_dict) and (s_dict[current_char] == t_dict[current_char]):
                have += 1

            while have == need:
                if (r - l + 1) < len_of_min_win_substring:
                    min_win_substring = [l, r]
                    len_of_min_win_substring = r - l + 1

                s_dict[s[l]] -= 1
                if (s[l] in t_dict) and (s_dict[s[l]] < t_dict[s[l]]):
                    have -= 1

                l += 1

        l, r = min_win_substring

        return s[l:r+1]


result = Solution()

print(result.minWindow("ADOBECODEBANC", "ABC")) # "ABC"
print(result.minWindow("a", "a"))               # "a"
print(result.minWindow("a", "aa"))              # ""