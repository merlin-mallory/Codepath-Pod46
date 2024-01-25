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
        1. l = 0, longest_substring = [-1, -1]
        2. Handle s == "".
        3. Create window_dict. Keys: Chars in window, Values: Count of keys.
        4. Loop r to end of s.
            5. Add s[r] to window_dict.
            6. Check if max(window_dict) <= k (this means its a valid window)
                7. Calculate the current_len
                8. Update longest_substring.
            9. Otherwise, remove window_dict[l] and l+ 1 until that conditional is true.
        10. Deconstruct longest_substring and return max_len
        '''

        import collections
        counts = collections.Counter()
        max_len = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            current_len = r - l + 1

            if (current_len - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1
            else:
                max_len = max(max_len, current_len)

        return max_len


result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

