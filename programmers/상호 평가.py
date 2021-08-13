def alphabet(score) :
    if score >= 90 : return "A"
    elif 80 <= score < 90 : return "B"
    elif 70 <= score < 80 : return "C"
    elif 50 <= score < 70 : return "D"
    else : return "F"

def solution(scores):
    scores = [[scores[y][x] for y in range(len(scores))] for x in range(len(scores))]
    answer = []
    for i in range(len(scores)) :
        tmp = scores[i]
        if scores[i].index(max(scores[i])) == i and len([t for t in scores[i] if t == max(scores[i])]) == 1 : del tmp[i]
        if scores[i].index(min(scores[i])) == i and len([t for t in scores[i] if t == min(scores[i])]) == 1: del tmp[i]
        answer.append(tmp)
    answer = [alphabet(sum(score)/len(score)) for score in answer]
    return ''.join(answer)

scores = [[75, 50, 100], [75, 100, 20], [100, 100, 20]]
print(solution(scores))



# 다른 풀이 ..
from collections import Counter
def solution2(scores):
    answer = ''

    for idx, score in enumerate(list(map(list, zip(*scores)))):
        length = len(score)
        if Counter(score)[score[idx]] == 1 and (max(score) == score[idx] or min(score) == score[idx]):
            del score[idx]
            length -= 1

        grade = sum(score) / length

        if grade >= 90:
            answer += 'A'
        elif grade >= 80:
            answer += 'B'
        elif grade >= 70:
            answer += 'C'
        elif grade >= 50:
            answer += 'D'
        else:
            answer += 'F'

    return answer


for idx, score in enumerate(list(map(list, zip(*scores)))):
    print(idx, score)
'''
output
0 [75, 75, 100]
1 [50, 100, 100]
2 [100, 20, 20]
'''

for idx, score in enumerate(scores) :
    print(idx, score)
'''
output
0 [75, 75, 100]
1 [50, 100, 100]
2 [100, 20, 20]
'''