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
        1. Create a counts dict. Keys: Char in s, Values: Count of that char in the substring.
        2. Initialize len_of_longest_substring, l=0
        3. Loop through s (iterator will act as r).
            4. Add s[r] into counts.
            4. Calculate the len_of_window.
            5. Check counts to see if len_of_window is valid. len_of_window - max(counts) < k.
            6. If the window is valid, then update len_of_longest_substring, and continue. Otherwise, remove s[l]
            from counts, and then l++
        7. Return len_of_longest_substring
        '''

        import collections

        counts = collections.defaultdict(int)
        len_of_longest_substring = 0
        l = 0

        for r in range(len(s)):
            counts[s[r]] += 1
            len_of_window = r - l + 1

            if (len_of_window - max(counts.values())) > k:
                counts[s[l]] -= 1
                l += 1
            else:
                len_of_longest_substring = max(len_of_longest_substring, len_of_window)

        return len_of_longest_substring

result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

