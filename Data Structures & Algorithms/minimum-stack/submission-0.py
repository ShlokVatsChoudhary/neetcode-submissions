class MinStack:
    def __init__(self):
        self.stack = []
        # Auxiliary stack to store the minimum value at each state, dry run krna to understand if fas rha ho toh..
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)

        if self.min_stack: #agar new incoming chota hua toh val = chotu vs top in min
            val = min(val, self.min_stack[-1])
        self.min_stack.append(val)

    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]