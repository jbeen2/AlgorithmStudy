def solution(triangle):
    answer = [triangle[0]]
    for i in range(1, len(triangle)) :
        tmp = []
        for j in range(len(triangle[i])) :
            if j == 0 :
                tmp.append(answer[i-1][j] + triangle[i][j])
            elif j == len(triangle[i])-1 :
                tmp.append(answer[i-1][j-1] + triangle[i][j])
            else :
                tmp.append(max(answer[i-1][j-1] + triangle[i][j], answer[i-1][j] + triangle[i][j]))
        answer.append(tmp)
    return max(answer[-1])

# ???
solution = lambda t, l = []: max(l) if not t else solution(t[1:], [max(x,y)+z for x,y,z in zip([0]+l, l+[0], t[0])])
