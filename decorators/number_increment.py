def number_increment(numbers):

    def increase():
        new_numbers = []
        for num in numbers:
            num += 1
            new_numbers.append(num)
        return new_numbers
        

    return increase()

print(number_increment([1, 2, 3]))