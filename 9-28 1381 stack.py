'''
1381. Design a Stack With Increment Operation
Design a stack that supports increment operations on its elements.

Implement the CustomStack class:

CustomStack(int maxSize) Initializes the object with maxSize which is the maximum number of elements in the stack.
void push(int x) Adds x to the top of the stack if the stack has not reached the maxSize.
int pop() Pops and returns the top of the stack or -1 if the stack is empty.
void inc(int k, int val) Increments the bottom k elements of the stack by val. If there are less than k elements in the stack, increment all the elements in the stack.
'''


'''

'''

class CustomStack:

    def __init__(self, maxSize: int):
        self.max = maxSize
        self.li = []

    def push(self, x: int) -> None:
        if self.max > len(self.li):
            self.li.append(x)
    def pop(self) -> int:
        if self.li:
            return self.li.pop()
        else:
            return -1

    def increment(self, k: int, val: int) -> None:
        for i in range(k):
            if i < len(self.li):
                self.li[i] += val
            else:
                break
        



# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)