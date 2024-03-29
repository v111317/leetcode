#https://leetcode.com/problems/min-stack/

# Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

# Implement the MinStack class:

# MinStack() initializes the stack object.
# void push(int val) pushes the element val onto the stack.
# void pop() removes the element on the top of the stack.
# int top() gets the top element of the stack.
# int getMin() retrieves the minimum element in the stack.
# You must implement a solution with O(1) time complexity for each function.

class MinStack:

    def __init__(self):
        self.stk = []
        self.minNum = float('+inf')
        
    def push(self, val: int) -> None:
        
        self.minNum = min(self.minNum, val)
        self.stk.append([val, self.minNum])
        return

    def pop(self) -> None:
        self.stk.pop()
        if len(self.stk)==0:
            self.minNum = float('+inf')
        else:
            self.minNum = self.stk[len(self.stk)-1][1]
        return
        
    def top(self) -> int:
        n = len(self.stk)
        return self.stk[n-1][0]
        

    def getMin(self) -> int:
        n = len(self.stk)
        return self.stk[n-1][1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(-2)
# obj.push(0)
# obj.push(-3)
# print(obj.getMin())
# obj.pop()
# print(obj.top())
# print(obj.getMin())

obj = MinStack()
obj.push(2147483646)
obj.push(2147483646)
obj.push(2147483647)
print(obj.top())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())
print(obj.pop())
obj.push(2147483647)
print(obj.top())
print(obj.getMin())
obj.push(-2147483648)
print(obj.top())
print(obj.getMin())
print(obj.pop())
print(obj.getMin())

#output [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483646,null,-2147483648,-2147483648,null,2147483646]
#expect [null,null,null,null,2147483647,null,2147483646,null,2147483646,null,null,2147483647,2147483647,null,-2147483648,-2147483648,null,2147483647]