T = int(input())
def bottom_up(n) :
    d = [0] * 100
    d[0], d[1], d[2], d[3] = 0, 1, 2, 4

    for i in range(4,12) :
        d[i] = d[i-1] + d[i-2] + d[i-3]
    return d[n]

for _ in range(T) :
    n = int(input())
    print(bottom_up(n))