class take_skip:
    def __init__(self, step, count) -> None:
        self.step = step
        self.count = count
        self.counter = 0
    
    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.count:
            raise StopIteration
        multiplier = self.counter
        self.counter += 1
        return multiplier * self.step

numbers = take_skip(2, 6)
for number in numbers:
    print(number)

