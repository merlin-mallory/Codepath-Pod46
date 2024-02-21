class TimeMap:
    '''
    981 - Time Based Key-Value Store

    https://leetcode.com/problems/time-based-key-value-store/

    Design a time-based key-value data structure that can store multiple values for the same key at different time
    stamps and retrieve the key's value at a certain timestamp.

    Implement the TimeMap class:

    TimeMap() Initializes the object of the data structure.
    void set(String key, String value, int timestamp) Stores the key key with the value value at the given time
    timestamp.
    String get(String key, int timestamp) Returns a value such that set was called previously, with
    timestamp_prev <= timestamp. If there are multiple such values, it returns the value associated with the
    largest timestamp_prev. If there are no values, it returns "".

    Example 1:
    Input:
    ["TimeMap", "set", "get", "get", "set", "get", "get"]
    [[], ["foo", "bar", 1], ["foo", 1], ["foo", 3], ["foo", "bar2", 4], ["foo", 4], ["foo", 5]]
    Output:
    [null, null, "bar", "bar", null, "bar2", "bar2"]
    Explanation:
    TimeMap timeMap = new TimeMap();
    timeMap.set("foo", "bar", 1);  // store the key "foo" and value "bar" along with timestamp = 1.
    timeMap.get("foo", 1);         // return "bar"
    timeMap.get("foo", 3);         // return "bar", since there is no value corresponding to foo at timestamp 3 and
                                   // timestamp 2, then the only value is at timestamp 1 is "bar".
    timeMap.set("foo", "bar2", 4); // store the key "foo" and value "bar2" along with timestamp = 4.
    timeMap.get("foo", 4);         // return "bar2"
    timeMap.get("foo", 5);         // return "bar2"

    Constraints:
    1 <= key.length, value.length <= 100
    key and value consist of lowercase English letters and digits.
    1 <= timestamp <= 10^7
    All the timestamps timestamp of set are strictly increasing.
    At most 2 * 10^5 calls will be made to set and get.
    '''

    def __init__(self):
        '''
        Create dict
        '''
        import collections
        self.dict = collections.defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        # Append [value, timestamp] to dict[key].
        self.dict[key].append([value, timestamp])
        return None

    def get(self, key: str, timestamp: int) -> str:
        if key not in self.dict:
            return ""
        cur_arr = self.dict[key]
        # Binary search through cur_arr. Set default_str to "". At each stage of binary search, check to update
        # default_str. If an exact match is found, then return that string. Otherwise, after the search completes,
        # return whatever is remaining in the default_str.
        default_str = ""
        l, r = 0, len(cur_arr) - 1
        while l <= r:
            m = (l + r) // 2
            cur_time = cur_arr[m][1]
            if cur_time == timestamp:
                return cur_arr[m][0]
            elif cur_time < timestamp:
                default_str = cur_arr[m][0]
                l = m + 1
            else:
                r = m - 1
        return default_str

# Time: O(1) for init and set, O(log(n) for get
# Space: O(1) for init, set, and get
# Edge: None

# Your TimeMap object will be instantiated and called as such:
# obj = TimeMap()
# obj.set(key,value,timestamp)
# param_2 = obj.get(key,timestamp)

timeMap = TimeMap()
timeMap.set("foo", "bar", 1)
print(timeMap.get("foo", 1))            # "bar"
print(timeMap.get("foo", 3))            # "bar"
timeMap.set("foo", "bar2", 4)
print(timeMap.get("foo", 4))            # "bar2"
print(timeMap.get("foo", 5))            # "bar2"
