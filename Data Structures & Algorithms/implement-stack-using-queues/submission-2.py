class MyStack:

    def __init__(self):
        from collections import deque
        self.stack_enq = deque()

    def push(self, x: int) -> None:
        self.stack_enq.append(x)
        for i in range(len(self.stack_enq)-1):
            self.stack_enq.append(self.stack_enq.popleft())

    def pop(self) -> int:
        return self.stack_enq.popleft()

    def top(self) -> int:
        return self.stack_enq[0]

    def empty(self) -> bool:
        return not self.stack_enq


# Your MyStack object will be instantiated and called as such:
# obj = MyStack()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.top()
# param_4 = obj.empty()