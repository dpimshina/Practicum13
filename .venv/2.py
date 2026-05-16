def get_common_courses(student_count: int) -> Set[str]:
    """
    Возвращает множество курсов,
    выбранных всеми студентами.
    """
    n = int(input().strip())
    all_courses = []

    for _ in range(n):
        courses = set(input().strip().split())
        all_courses.append(courses)

    if not all_courses:
        print(0)
        return

    common = all_courses[0].copy()
    for courses in all_courses[1:]:
        common &= courses

    print(len(common))