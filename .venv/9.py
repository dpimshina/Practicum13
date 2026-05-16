from itertools import combinations

numbers = sorted(set(map(int, input().split())))
k = int(input())

result: list[list[int]] = []

for subset in combinations(numbers, k):
    result.append(list(subset))

print(result)