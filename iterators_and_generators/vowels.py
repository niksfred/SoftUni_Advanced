class vowels:
    vowels_list = ["a", "e", "o", "i", "y", "u", "A", "E", "O", "I", "Y", "U"]
    def __init__(self,string) -> None:
        self.string = string
        self.start = 0
        self.vowels = [char for char in self.string if char in self.vowels_list]
        self.end = len(self.vowels) - 1
        current_index = self.start

    def __iter__(self):
        return self

    def __next__(self):
        if self.start > self.end:
            raise StopIteration
        current_index = self.start
        self.start += 1
        return self.vowels[current_index]

my_string = vowels('Abcedifuty0o')
for char in my_string:
    print(char)
