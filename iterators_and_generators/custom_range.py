class custom_range:
    def __init__(self, start, end) -> None:
        self.start = start
        self.end = end
        self.current = self.start
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.current > self.end:
            raise StopIteration
        temp = self.current
        self.current += 1 
        return temp

for el in custom_range(0, 10):
    print(el)