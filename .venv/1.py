def get_repeated_numbers(numbers: List[int]) -> set[int]:
    """
    Возвращает множество повторяющихся чисел.
    """
    numbers = list(map(int, input().strip().split()))
    target = int(input().strip())

    seen = set()
    repeats = set()

    for num in numbers:
        if num in seen:
            repeats.add(num)
        else:
            seen.add(num)

    print("YES" if target in repeats else "NO")