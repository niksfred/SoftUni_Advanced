def permutation(remaining, candidate=""):
    if len(remaining) == 0:
        print(candidate)

    for i in range(len(remaining)):
        new_candidate = candidate + remaining[i]
        new_remaining = remaining[0:i] + remaining[i+1:]

        permutation(new_remaining, new_candidate)

start_str = input()
permutation(start_str)
