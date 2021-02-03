def solution(strings, n):
    strings = sorted(strings)

    check = [(idx, s[n]) for idx, s in enumerate(strings)]
    check = sorted(check, key=(lambda x: x[1]))

    order = [c[0] for c in check]
    answer = []
    for o in order:
        answer.append(strings[o])

    return answer