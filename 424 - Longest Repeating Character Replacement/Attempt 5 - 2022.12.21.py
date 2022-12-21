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
        1. Looks like sliding window.
        2. l = 0, r = 0, current_len = 0, max_len = 0
        3. while r < len(s) - 1
        4.  r += 1
        5.  if s[l] == s[r]:
        6.      current_len += 1
        7.      max_len = max(max_len, current_len)
        8.  else:
        9.      l += 1
        10.     current_len -= 1
        11. return max_len
        '''

        # Failed attempt. I need to create an O(26) dictionary to track each char's count in the window.
        # l = 0, r = 0, loop r to the end of the array. (((r-l+1) - maxf) > k) checks if the current window is invalid,
        # in which case we need to decrement the count of s[l], and then decrement l. Then update the max.

        l, r, current_len, max_len, sub_count = 0, 0, 0, 0, 0
        arr_s = list(s)
        while r < (len(arr_s) - 1):
            if arr_s[l] == arr_s[r]:
                r += 1
                current_len += 1
                max_len = max(max_len, current_len)
            elif sub_count < k:
                sub_count += 1
                r += 1
                current_len += 1
                max_len = max(max_len, current_len)
            else:
                l -= 1
                current_len -= 1
                sub_count -= 1
        return max_len

result = Solution()
print(result.characterReplacement("ABAB", 2))       # 4
print(result.characterReplacement("AABABBA", 1))    # 4

