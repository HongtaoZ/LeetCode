class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.data = list()

    def push(self, x: int) -> None:
        self.data.append(x)

    def pop(self) -> None:
        self.data.pop()

    def top(self) -> int:
        if len(self.data)==0:
            return None
        else:
            return self.data[self.data.__len__()-1]

    def getMin(self) -> int:
        if len(self.data)==0:
            return None
        else:
            return min(self.data)


# Your MinStack object will be instantiated and called as such:
obj = MinStack()
x=50
obj.push(x)
obj.push(x)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)

# april 5, 2019 : 824 ms