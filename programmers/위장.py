# -*- coding: utf-8 -*-
def solution(clothes) :
    spy, answer = dict(), 1
    for c in clothes :
        spy.setdefault(c[1], []).append(c[0])

    for type in spy.keys() :
        answer *= (len(spy[type]) + 1)

    return answer - 1

print(solution(clothes))

# =======================================================

import itertools
def solution2(clothes):
    spy = dict()
    for c in clothes :
        spy.setdefault(c[1], []).append(c[0])

    answer = len(clothes)
    for i in range(2, len(spy)+1) :
        combinations = list(itertools.combinations(spy.keys(), i))

        for comb in combinations :
            mul = 1
            for cb in comb :
                mul *= len(spy[cb])
            answer += mul

    return answer

# =======================================================
from functools import reduce
answer = reduce(lambda x, y: x*(y+1), cnt.values(), 1) - 1  # 리스트 내 원소 다 곱해주는 함수!