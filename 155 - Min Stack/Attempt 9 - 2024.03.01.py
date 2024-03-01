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

        Plan:
        Init: Create stack and min_stack arrs.
        Push: Append val to stack. Check if there is a stack, and stack[-1] < val. If so, append stack[-1] to the
        min_stack. Otherwise, append val to the min_stack.
        Pop: Pop from both stack and min_stack.
        Top: Return stack[-1]
        getMin: Return min_stack[-1]
        Time: O(1) for init, push, pop, top, getMin.
        Space: O(1) for init, push, pop, top, getMin.
        '''
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_stack and (self.min_stack[-1] < val):
            self.min_stack.append(self.min_stack[-1])
        else:
            self.min_stack.append(val)
        return None

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()
        return None

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
