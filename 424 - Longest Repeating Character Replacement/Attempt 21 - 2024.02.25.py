class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        '''
        424 - Longest Repeating Character Replacement

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

        Plan:
        Create s_window counter dict. Init empty. Keys: Chars in current window. Values: Count of keys.
        l, r = 0, 0.
        max_len = 0
        Loop through s.
            Add s[r] to s_window.
            Check if the current window is valid. If (r - l + 1 - max(dict.values()) <= k, then it's valid. If that's
            the case, then update max_len. Otherwise remove s[l] from s_window and l++ until the window is valid again.
            r++
        Return max_len
        Time: O(n)
        Space: O(26)
        Edge: None
        '''
        import collections
        s_window = collections.Counter()
        max_len = 0
        l, r = 0, 0
        while r < len(s):
            s_window[s[r]] += 1
            while (r - l + 1 - max(s_window.values())) > k:
                s_window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len



result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

