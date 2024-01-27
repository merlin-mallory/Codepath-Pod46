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

        Plan:
        1. Create two arrays on init. stack will contain values in the stack. min_stack will contain values which
        indicate the minimum value at any corresponding index of stack.
        2. Create push. Pushing a value should append to stack, and we should also push the minimum of the value and
        whatever the min_stack[-1] value is.
        3. Create pop. Pop from both stack and min_stack.
        4. Create top. Return stack[-1].
        5. Create getMin. Return min_stack[-1]
        '''
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        self.min_stack.append(min(val, self.min_stack[-1] if self.min_stack else val))
    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]

# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()
