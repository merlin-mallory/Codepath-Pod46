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
        1. Initialize len_of_longest_substring, len_of_current_substring, l, r
        2. Create counts dict (keys: chars, value: count of key in the current substring.
        3. Loop while r < end of the string
            4. Check if the current substring is valid by comparing the max of the counts dict with k.
                5. If its valid, then update len_of_longest_substring, and advance r.
                6. Otherwise, decrement counts[l], and then increment l.
        7. Return len_of_longest_substring
        '''
        import collections

        len_of_longest_substring = 0
        counts = collections.defaultdict(int)

        l, r = 0, 0

        for r in range(len(s)):
            counts[s[r]] += 1
            len_of_current_substring = r - l + 1

            if len_of_current_substring - max(counts.values()) > k:
                counts[s[l]] -= 1
                l += 1

            len_of_longest_substring = max(len_of_longest_substring, r-l+1)

        return len_of_longest_substring

result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

