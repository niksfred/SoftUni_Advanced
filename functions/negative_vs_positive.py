def compare(nums):
    positive = []
    negative = []
    for num in nums:
        if num > 0:
            positive.append(num)
        else:
            negative.append(num)

    print(sum(negative))
    print(sum(positive))

    if abs(sum(negative)) > sum(positive):
        print("The negatives are stronger than the positives")
    else:
        print("The positives are stronger than the negatives")


numbers = [int(el) for el in input().split()]
compare(numbers)
