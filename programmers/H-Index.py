def solution(citations):
    count = [0] * (max(citations) + 1)
    h, c = [], 0

    for i in range(len(citations)) :
        count[citations[i]] += 1
    for j in range(len(count)) :
        h.append(sum(count[j:]))
    for idx, n in enumerate(h) :
        if idx <= n :
            c += 1

    return c-1


# 1
def solution(citations):
    citations = sorted(citations)
    l = len(citations)
    for i in range(l):
        if citations[i] >= l-i:
            return l-i
    return 0


# 2
def solution(citations):
    citations.sort(reverse=True)
    answer = max(map(min, enumerate(citations, start=1)))
    return answer