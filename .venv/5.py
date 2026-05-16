def main_task5():
    n = int(input().strip())
    if n < 2:
        print()
        return

    numbers = set(range(2, n))
    primes = set()

    while numbers:
        p = min(numbers)
        primes.add(p)
        numbers -= set(range(p, n, p))

    print(*sorted(primes))