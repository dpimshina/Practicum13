from itertools import permutations

numbers = sorted(set(map(int, input().split())))
result = list(permutations(numbers))

print(result)

