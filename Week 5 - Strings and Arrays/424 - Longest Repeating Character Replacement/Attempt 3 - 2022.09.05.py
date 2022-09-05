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
        1. Insight: The longest substring is going to be the most frequent character plus k, up to a maximum of the
        length of s.
        2. Is that true? "AAABBBAAA", k = 3, result = 9. "AABBBAA", k = 2, result = 5. "ABABBA", k = 2,
        3. Not sure.
        '''
        # Failed attempt.
        import collections
        mapping_dict = collections.defaultdict(int)
        max_freq_char_count = 0
        max_freq_char = None

        for char in s:
            mapping_dict[char] += 1
            if mapping_dict.get(char) > max_freq_char_count:
                max_freq_char_count = mapping_dict.get(char)
                max_freq_char = char

        while max_freq_char_count < len(s) and k:
            max_freq_char_count += 1
            k -= 1

        return max_freq_char_count


result = Solution()
print(result.characterReplacement("ABAB", 2))       # 2
print(result.characterReplacement("AABABBA", 1))    # 4

