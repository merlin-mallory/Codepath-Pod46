class MinStack:

    def __init__(self):
        '''
        155 - Min Stack

        https://leetcode.com/problems/min-stack/

        Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

        Implement the MinStack class:

        MinStack() initializes the stack object.
        void push(int val) pushes the element val onto the stack.
        void pop() removes the element on the top of the stack.
        int top() gets the top element of the stack.
        int getMin() retrieves the minimum element in the stack.
        You must implement a solution with O(1) time complexity for each function.
        You may assume that every stack operation will be valid.

        Example 1:

        Input
        ["MinStack","push","push","push","getMin","pop","top","getMin"]
        [[],[-2],[0],[-3],[],[],[],[]]

        Output
        [null,null,null,null,-3,null,0,-2]

        Explanation
        MinStack minStack = new MinStack();
        minStack.push(-2);
        minStack.push(0);
        minStack.push(-3);
        minStack.getMin(); // return -3
        minStack.pop();
        minStack.top();    // return 0
        minStack.getMin(); // return -2

        Constraints:

        -2^31 <= val <= 2^31 - 1
        Methods pop, top and getMin operations will always be called on non-empty stacks.
        At most 3 * 10^4 calls will be made to push, pop, top, and getMin.
        '''
        self.min_stack = []
        self.cur_min = []

    def push(self, val: int) -> None:
        self.min_stack.append(val)
        if self.cur_min and (self.cur_min[-1] < val):
            self.cur_min.append(self.cur_min[-1])
        else:
            self.cur_min.append(val)
        return None

    def pop(self) -> None:
        self.min_stack.pop()
        self.cur_min.pop()
        return None

    def top(self) -> int:
        return self.min_stack[-1]

    def getMin(self) -> int:
        return self.cur_min[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
