def solution(n) :
    i, k = 1, 3
    m = n
    number = [1,2,4]

    if n <= 3 :
        return number[n-1]

    while m > k :
        i += 1
        m -= k
        k *= 3

        if m <= k :
            answer = []

            print(m)
            print(k)
            print(i)    # 3 : 0 1 2
            print("===")
            print(3**(i-1))
            print((m-1)//(3**(i-1)))
            print("===")


            new_m = m
            for num in range(i-1, -1, -1) :   # 2 1 0
                print(num)
                print(3**num)
                print((new_m-1) // (3**num))
                new_m -= (3 ** num)
                print(new_m)
                print('---')
            print(new_m)

n = int(input())
print(solution(n))