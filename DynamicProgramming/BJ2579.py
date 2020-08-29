n = int(input())
stair = [int(input()) for _ in range(n)]

d = [stair[0]]

def solve(n) :
    if d[n] > 0 :
        return d[n]

    d[n] = max(stair[n-1]+solve(n-3), solve(n-2))+stair[n]
    return d[n]

for i in range(3,n) :
    d.append(solve(i))

print(d)
