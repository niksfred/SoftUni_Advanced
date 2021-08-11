class reverse_iter:
    def __init__(self, obj) -> None:
        self.obj = obj
        self.index = len(obj) - 1
        self.end = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < self.end:
            raise StopIteration
        current_index = self.index
        self.index -= 1
        return self.obj[current_index]

reversed_list = reverse_iter([1, 2, 3, 4])
for item in reversed_list:
    print(item)
