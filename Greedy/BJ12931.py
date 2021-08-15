N = int(input())
B = list(map(int, input().split()))

def check(B) :
    global count
    if [b%2 for b in B] == [0]*N :
        count += 1
        return [b//2 for b in B]
    else :
        for i in range(len(B)) :
            if B[i]%2 != 0 :
                count += 1
                B[i] -= 1
        return B

count = 0
while True :
    if B == [0]*N :
        break
    B = check(B)
print(count)