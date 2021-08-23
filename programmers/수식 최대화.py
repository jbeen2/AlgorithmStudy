def solution(expression):
    op = [
        ("+", "-", "*"), ("+", "*", "-"),
        ("-", "*", "+"), ("-", "+", "*"),
        ("*", "+", "-"), ("*", "-", "+")
    ] ; answer = 0
    for o in op :
        a = list(map(lambda x : list(map(lambda x : x.split(o[2]), x.split(o[1]))), expression.split(o[0])))
        for i in range(len(a)) :
            for j in range(len(a[i])) :
                a[i][j] = "(" + o[2].join(a[i][j]) + ")"
            a[i] = "(" + o[1].join(a[i]) + ")"
        a = "(" + o[0].join(a) + ")"
        if answer < abs(eval(a)) :
            answer = abs(eval(a))
    return answer

# 연산자 역순으로 진행됨!
print(solution("100-200*300-500+20"))
