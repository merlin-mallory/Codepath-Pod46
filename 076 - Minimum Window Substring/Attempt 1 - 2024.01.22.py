class Solution:
    def minWindow(s: str, t: str) -> str:
        '''
        Minimum Window Substring

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
        1. Handle edge case where len(t) > len(s).
        2. Create tCounts dict. Keys: Chars in t, Values: Count of keys.
        3. Create sWindow dict. Starts empty, but will contain Keys: Chars in t's window, and Values: Count of keys.
        4. Initialize l = 0
        5. Loop with r until end of s.
            6. Add s[r] to sWindow
            7. If r > len(t), then
                8.
        '''

        if t == "" or (len(t) > len(s)):
            return ""

        import collections

        countT = collections.Counter(t)
        window = collections.Counter()
        have, need = 0, len(countT)
        min_win_substring, len_of_min_win_substring = [-1, -1], float('inf')
        l = 0

        for r in range(len(s)):
            current_char = s[r]
            window[current_char] = 1 + window.get(current_char, 0)

            if (current_char in countT) and (window[current_char] == countT[current_char]):
                have += 1

            while have == need:
                if (r - l + 1) < len_of_min_win_substring:
                    min_win_substring = [l, r]
                    len_of_min_win_substring = (r - l + 1)

                window[s[l]] -= 1
                if (s[l] in countT) and (window[s[l]] < countT[s[l]]):
                    have -= 1
                l += 1

        l, r = min_win_substring

        if len_of_min_win_substring != float('inf'):
            return s[l:r+1]
        else:
            return ""

result = Solution

print(result.minWindow("ADOBECODEBANC", "ABC")) # "BANC"
print(result.minWindow("a", "a"))               # "a"
print(result.minWindow("a", "aa"))              # ""