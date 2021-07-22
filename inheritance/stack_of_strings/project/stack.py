class Stack:
    def __init__(self, data: list = []):
        self.data = data

    def push(self, element):
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]
    
    def is_empty(self):
        if len(self.data) == 0:
            return True
        else:
            return False

    def __str__(self):
        res = ""
        res += "["
        for index in range(len(self.data)-1, -1, -1):
            res += f"{self.data[index]}"
            if index != 0:
                res += ", "
        res += "]"
        return res

stack = Stack()
stack.push("apple")
stack.push("carrot")
stack.push("carrot2")
stack.push("carrot3")
print(stack)