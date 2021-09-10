# Weekly Challenge 6
def solution(weights, head2head):
    answer = []
    for i in range(len(weights)) :
        t = 0 ; r = 0; c = 0; w = weights[i]; idx = i+1
        for j in range(len(weights)) :
            if head2head[i][j] != "N" : t += 1
            if head2head[i][j] == "W" :
                r += 1
                if weights[i] < weights[j] : c += 1
        if t != 0 : answer.append((r/t, c, w, idx))
        else : answer.append((0, c, w, idx))
    answer = sorted(answer, key = lambda x : (-x[0], -x[1], -x[2], x[3]))
    return [a[3] for a in answer]


# Example
# weights = [50,82,75,120]
# head2head = ["NLWL","WNLL","LWNW","WWLN"]

# weights = [145,92,86]
# head2head = ["NLW","WNL","LWN"]

weights = [60,70,60]
head2head = ["NNN","NNN","NNN"]

print(solution(weights, head2head))