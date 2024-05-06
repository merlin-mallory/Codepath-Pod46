class TrieNode():
    def __init__(self):
        self.children = {}
        self.is_end = False

class WordDictionary:
    '''
    211 - Design Add and Search Words Data Structure

    https://leetcode.com/problems/design-add-and-search-words-data-structure/

    Design a data structure that supports adding new words and finding if a string matches any previously added string.

    Implement the WordDictionary class:

    WordDictionary() Initializes the object.
    void addWord(word) Adds word to the data structure, it can be matched later.
    bool search(word) Returns true if there is any string in the data structure that matches word or false otherwise.
    word may contain dots '.' where dots can be matched with any letter.

    Example:
    Input
    ["WordDictionary","addWord","addWord","addWord","search","search","search","search"]
    [[],["bad"],["dad"],["mad"],["pad"],["bad"],[".ad"],["b.."]]
    Output
    [null,null,null,null,false,true,true,true]

    Explanation
    WordDictionary wordDictionary = new WordDictionary();
    wordDictionary.addWord("bad");
    wordDictionary.addWord("dad");
    wordDictionary.addWord("mad");
    wordDictionary.search("pad"); // return False
    wordDictionary.search("bad"); // return True
    wordDictionary.search(".ad"); // return True
    wordDictionary.search("b.."); // return True

    Constraints:
    1 <= word.length <= 25
    word in addWord consists of lowercase English letters.
    word in search consist of '.' or lowercase English letters.
    There will be at most 2 dots in word for search queries.
    At most 10^4 calls will be made to addWord and search.

    Plan:
    Trie with Backtracking
    Time: O(n * 2^n)
    Space: O(n)
    Edge: None
    '''
    def __init__(self):
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        cur = self.root
        for c in word:
            if c not in cur.children: cur.children[c] = TrieNode()
            cur = cur.children[c]
        cur.is_end = True
        return None

    def search(self, word: str) -> bool:
        def dfs(i, cur):
            for j in range(i, len(word)):
                c = word[j]
                if c == ".":
                    for child in cur.children.values():
                        if dfs(j+1, child): return True
                    return False
                if c not in cur.children: return False
                cur = cur.children[c]
            return cur.is_end

        return dfs(0, self.root)

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)