def get_primes(integers: list):
    for num in integers:
        is_prime = True
        if num <= 1:
            is_prime = False
            
        for divider in range(2, num):
            if num % divider == 0:
                is_prime = False
                break
        if is_prime:
            yield num

print(list(get_primes([2, 4, 3, 5, 6, 9, 1, 0])))

