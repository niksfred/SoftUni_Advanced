from collections import deque

class dictionary_iter:
    def __init__(self, dict: dict) -> None:
        self.dict = dict
        self.end = len(dict) - 1
        self.index = 0
        self.keys = deque([key for key in self.dict.keys()])
        self.values = deque([value for value in self.dict.values()])
    
    def __iter__(self):
        return self

    def __next__(self):
        if len(self.keys) == 0:
            raise StopIteration
        return self.keys.popleft(), self.values.popleft()

result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)


