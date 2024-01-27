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

        Plan:
        Sliding Window
        1. len_of_longest_substring = 0
        2. Create window dict. Keys: Chars in window, Values: Count of keys.
        3. have?
        4. l, r = 0, 0
        5. Loop while r > len(s).
            6. Add s[r] to window.
            7. Check if the current window is valid, by finding max(window), and seeing if (r-l+1) - max(window) is < k.
                8. If it is valid, then update len_of_longest_substring. And then remove and decrement l until its no
                longer valid.
            9. Otherwise, ?
        10. return len_of_longest_substring
        '''
        len_of_longest_substring = 0
        import collections
        window = collections.Counter()
        l, r = 0, 0
        while r < len(s):
            window[s[r]] += 1
            if ((r-l+1) - max(window.values())) > k:
                window[s[l]] -= 1
                l += 1
            else:
                len_of_longest_substring = max(len_of_longest_substring, r - l + 1)
            r += 1
        return len_of_longest_substring

result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

