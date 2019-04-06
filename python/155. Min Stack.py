class MinStack:

    def __init__(self):
        
        #maintain two lists, one of them contain minimum values
        
        self.data = []
        self.minData = []
        

    def push(self, x: int) -> None:
        self.data.append(x)
        # if new vaule is less than or equal to current minimum value
        # keep storing minimum values, e.g. 50(push) 40(push) 42 43 45 30(push), 
        # so when pop value, the minimum stack still have smallest value 
        if len(self.minData)==0 or x<=self.minData[-1]:
            self.minData.append(x)

    def pop(self) -> None:
        if(len(self.data)==0):
            return None
        else:
            if self.data[-1] == self.minData[-1]:
                self.minData.pop()
            self.data.pop()

    def top(self) -> int:
        if len(self.data)==0:
            return None
        else:
            return self.data[-1]

    def getMin(self) -> int:
        if len(self.data)==0:
            return None
        else:
            return self.minData[-1]

# Your MinStack object will be instantiated and called as such:
obj = MinStack()
obj.push(60)
obj.push(50)
obj.push(52)
obj.push(40)
obj.pop()
param_3 = obj.top()
param_4 = obj.getMin()
print(param_3)
print(param_4)

# april 5, 2019 : 824 ms