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
        2. Create a hashmap, which will contain the frequency of any given character in the window. Keys: char,
        value: count.
        3. Left, right = 0
        4. while right < len(s):
            6. Loop through the hashmap's keys and find the max frequency.
            7. If the max frequency is <= k, then the current window is valid, so hashmap[right]++, max(max_length,
            right-left+1),
            and right++
            8. Otherwise, we need to find a new valid window, so hashmap[left]--, and then left++
        '''
        # Failed attempt. Right needs to loop from 0 to end of the array, and at each iteration we add +1 to s[
        # right]. And then we handle the left pointer by doing a while loop by calculating (right-left+1) - max(
        # hashmap.values() > k. This checks if the current window is valid. And then at the end, we find the max of
        # max_len and right-left-1.

        import collections
        hashmap = collections.defaultdict(int)
        left, right = 0, 0
        max_length = 0

        while right < len(s):
            current_len = right-left+1
            max_freq = max(hashmap.values())
            if max_freq <= k:
                hashmap[right] += 1
                max_length = max(max_length, max_freq)
result = Solution()
print(result.characterReplacement("ABAB", 2))       # 2
print(result.characterReplacement("AABABBA", 1))    # 4

