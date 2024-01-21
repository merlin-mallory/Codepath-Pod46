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

    Encode Plan:
    Array
    1. Initialize encoded_str. Loop through strs.
        2. Calculate the len of each str.
        3. Append len + "#" + current_str to encoded_str.
    4. Join and return encoded_str.
    Time: O(n), Space: O(n)

    Decode Plan:
    Array:
    1. Loop through s.
        2. Collect numeric values, and convert into an int.
        3. Increment +1 to bypass the "#" character.
        4. Slice the desired substring, and append to decoded_str
    5 Return decoded_str
    Time: O(n), Space: O(n)
    """
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        encoded_str = []
        for current_str in strs:
            len_of_current_str = len(current_str)
            encoded_str.append(str(len_of_current_str) + "#" + current_str)
        return ''.join(encoded_str)

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        decoded_str = []

        i = 0
        while i < len(s):
            temp_arr = []
            while s[i].isdigit():
                temp_arr.append(s[i])
                i += 1
            len_of_current_str = int(''.join(temp_arr))

            i += 1

            decoded_str.append(s[i:i+len_of_current_str])
            i += len_of_current_str

        return decoded_str

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))
