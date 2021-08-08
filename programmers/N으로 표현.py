def solution(N, number):
    answer = [[N]]
    for i in range(2, 9) :
        tmp = [int(str(N)*i)]
        for j in answer[i-2] :
            tmp.extend([int(j+N), int(j-N), int(N-j), int(j*N)])
            if j != 0 :
                tmp.append(int(j//N))
        #tmp = [t for t in tmp if t > 0]
        answer.append(list(set(tmp)))

    for k in range(len(answer)) :
        if number in answer[k] :
            return k+1
    return -1

print(solution(1,1121))

# 왜 다른 사람 풀이는 올 패스인데 내껀 안 되는 것인가 ...
def solution(N, number):
    S = [0, {N}]
    for i in range(2, 9):
        case_set = {int(str(N)*i)}
        for i_half in range(1, i//2+1):  # S[i_half] S[1]
            for x in S[i_half]:
                for y in S[i-i_half]:
                    case_set.add(x+y)
                    case_set.add(x-y)
                    case_set.add(y-x) # y-x 케이스 추가
                    case_set.add(x*y)
                    if x != 0:
                        case_set.add(y//x)
                    if y != 0:
                        case_set.add(x//y)
        if number in case_set:
            return i
        S.append(case_set)
        if N == 1 or N == number: return N % number + 1
    return -1