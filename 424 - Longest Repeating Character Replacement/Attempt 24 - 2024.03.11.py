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
        Sliding Window
        Create s_window.
        l, r = 0, 0
        Loop while r < len(s)
            Add s[r] to s_window
            while (r-l+1 - max(s_window.values()) > k:
                Remove s[l] from s_window
                l++
            Update max_len
            r++
        Time: O(n)
        Space: O(1)
        Edge: k could be 0, s could be 1
        '''
        import collections
        s_window = collections.Counter()
        max_len = 0
        l, r = 0, 0
        while r < len(s):
            s_window[s[r]] += 1
            while (r-l+1 - max(s_window.values())) > k:
                s_window[s[l]] -= 1
                l += 1
            max_len = max(max_len, r-l+1)
            r += 1
        return max_len

result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

