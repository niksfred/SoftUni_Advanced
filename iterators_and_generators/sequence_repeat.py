class sequence_repeat:
    def __init__(self, sequence: str, number: int) -> None:
        self.sequence = sequence
        self.number = number
        self.counter = 0
        self.sequence_counter = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.counter == self.number:
            raise StopIteration
        if self.sequence_counter == len(self.sequence):
            self.sequence_counter = 0
        current_index = self.sequence_counter
        self.sequence_counter += 1
        self.counter += 1
        return self.sequence[current_index]

result = sequence_repeat('abc', 5)
for item in result:
    print(item, end ='')

