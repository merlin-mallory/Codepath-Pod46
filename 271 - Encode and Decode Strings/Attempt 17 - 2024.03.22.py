class Codec:
    """
    Design an algorithm to encode a list of strings to a string. The encoded string is then sent over the network and
    is decoded back to the original list of strings.

    Machine 1 (sender) has the function:

    string encode(vector<string> strs) {
      // ... your code
      return encoded_string;
    }
    Machine 2 (receiver) has the function:
    vector<string> decode(string s) {
      //... your code
      return strs;
    }
    So Machine 1 does:

    string encoded_string = encode(strs);
    and Machine 2 does:

    vector<string> strs2 = decode(encoded_string);
    strs2 in Machine 2 should be the same as strs in Machine 1.

    Implement the encode and decode methods.

    You are not allowed to solve the problem using any serialize methods (such as eval).

    Input: dummy_input = ["Hello","World"]
    Output: ["Hello","World"]
    Explanation:
    Machine 1:
    Codec encoder = new Codec();
    String msg = encoder.encode(strs);
    Machine 1 ---msg---> Machine 2

    Machine 2:
    Codec decoder = new Codec();
    String[] strs = decoder.decode(msg);
    Example 2:

    Input: dummy_input = [""]
    Output: [""]
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        Plan:
        Create encoded_str array.
        Loop cur_str through strs.
            Calc cur_str_len.
            Append str(cur_str_len) + "#" + cur_str to encoded_str.
        Join and return encoded_str.
        Time: O(n)
        Space: O(1) or O(n) depending upon classification of output
        Edge: None
        """
        encoded_str = []
        for cur_str in strs:
            cur_str_len = len(cur_str)
            encoded_str.append(str(cur_str_len) + "#" + cur_str)
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        Plan:
        Create decoded_strs array.
        i = 0
        Loop while i < len(s).
            Set len_arr = []
            Loop while s[i].isdigit()
                Append s[i] to len_arr
                i++
            Set cur_str_len = int(joined len_arr)
            i++
            Set cur_str = s[i:i+cur_str_len]
            Append cur_str to decoded_strs.
            i += cur_str_len
        Return decoded_strs
        Time: O(n)
        Space: O(1)
        Edge: None
        """
        decoded_strs = []
        i = 0
        while i < len(s):
            len_arr = []
            while s[i].isdigit():
                len_arr.append(s[i])
                i += 1
            cur_str_len = int(''.join(len_arr))
            i += 1
            cur_str = s[i:i+cur_str_len]
            decoded_strs.append(cur_str)
            i += cur_str_len
        return decoded_strs

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
