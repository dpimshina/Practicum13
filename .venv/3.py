def main_task3():
    sweet = set(input().strip().split())
    n = int(input().strip())

    friends = set()
    for _ in range(n):
        friends |= set(input().strip().split())

    only_sweet = sweet - friends
    print(len(only_sweet))