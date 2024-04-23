from typing import List
class Solution:
    def alienOrder(self, words: List[str]) -> str:
        '''
        269 - Alien Dictionary

        https://leetcode.com/problems/alien-dictionary/

        There is a new alien language that uses the English alphabet. However, the order of the letters is unknown to
        you.

        You are given a list of strings words from the alien language's dictionary. Now it is claimed that the strings
        in words are sorted lexicographically by the rules of this new language.

        If this claim is incorrect, and the given arrangement of string in words cannot correspond to any order of
        letters, return "".

        Otherwise, return a string of the unique letters in the new alien language sorted in lexicographically
        increasing order by the new language's rules. If there are multiple solutions, return any of them.

        Constraints:
        1 <= words.length <= 100
        1 <= words[i].length <= 100
        words[i] consists of only lowercase English letters.

        Plan:
        Topological Sort
        Time: O(s), where s = sum total of all words in the input list
        Space: O(1) or (O(u + min(u^2,n)), where u = total number of unique letters in the alien alphabet (not just
        in input) and n = sum total len of words
        Edge: ?
        '''
        adj = { c: set() for w in words for c in w }

        for i in range(len(words)-1):
            w1, w2 = words[i], words[i+1]
            minLen = min(len(w1), len(w2))
            if len(w1) > len(w2) and w1[:minLen] == w2[:minLen]:
                return ""
            for j in range(minLen):
                if w1[j] != w2[j]:
                    adj[w1[j]].add(w2[j])
                    break
        visit = {}
        res = []

        def dfs(c):
            if c in visit: return visit[c]

            visit[c] = True
            for nei in adj[c]:
                if dfs(nei): return True
            visit[c] = False
            res.append(c)

        for c in adj:
            if dfs(c): return ""

        res.reverse()
        return "".join(res)

solution = Solution()
print(solution.alienOrder(["wrt","wrf","er","ett","rftt"]))     # "wertf"
print(solution.alienOrder(["z","x"]))                           # "zx"
print(solution.alienOrder(["z","x","z"]))                       # ""
# Explanation: The order is invalid, so return "".
