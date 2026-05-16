def main_task4():
    set1 = set(input().strip().split())
    set2 = set(input().strip().split())
    target = input().strip()

    intersection = set1 & set2
    print("YES" if target in intersection else "NO")