for hod in range(100, 334):
    mat = hod * 3

    if mat > 999:
        continue

    digits = str(hod) + str(mat)

    if len(set(digits)) == 6:
        print(f"{hod}+{hod}+{hod}={mat}")