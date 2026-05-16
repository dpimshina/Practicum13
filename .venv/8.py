from itertools import combinations

numbers = sorted(set(map(int, input().split())))
subsets: list[list[int]] = []

for size in range(len(numbers) + 1):
    for subset in combinations(numbers, size):
        subsets.append(list(subset))

print(subsets)