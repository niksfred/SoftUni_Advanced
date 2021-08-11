def possible_permutations(elements):
    if len(elements) <=1:
        yield elements
    else:
        results = []
        for x in elements:
            for y in elements:
                for z in elements:
                    if [x , y, z] not in results:
                        if x != y and x != z and y != z:
                            yield [x , y, z]
                        


[print(n) for n in possible_permutations([1, 2, 3])]