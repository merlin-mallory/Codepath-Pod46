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

        Plan: Sliding Window
        1. Create window dict. Keys: Chars in window, Values: Count of chars in window.
        2. Init len_of_longest_substring = 0, l = 0, r = 0.
        3. Loop while r < len(s).
            4. Add s[r] to window_dict.
            5. Check if the current window is valid. (r-l+ 1 - max(window_dict).values < k).
                6. If its valid, then update len_of_longest_substring.
            7.  Otherwise, remove s[l] and advance l until it is valid again.
        9. r++
        10. Return len_of_longest_substring
        Edge Cases: If k == 0, then return empty string.
        Time: O(n)
        Space: O(26)
        '''
        import collections
        window = collections.Counter()
        len_of_longest_substring = 0
        l, r = 0, 0

        while r < len(s):
            window[s[r]] += 1
            if (r - l + 1 - max(window.values())) <= k:
                len_of_longest_substring = max(len_of_longest_substring, r - l + 1)
            else:
                # while (r - l + 1 - max(window.values())) > k:
                window[s[l]] -= 1
                l += 1
            r += 1

        return len_of_longest_substring

result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

