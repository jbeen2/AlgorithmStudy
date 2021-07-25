def solution(progresses, speeds):
    last = [(100-p)//s if (100-p)%s==0 else (100-p)//s+1 for p, s in zip(progresses, speeds)]
    # print(last)

    answer, count = [], 1
    check = last.pop(0)

    # print(check)
    # print(last)
    # print("*")


    while last :
        if check >= last[0] : # !!
            count += 1
            last.pop(0)
            # print("#check:", check)
            # print("#last:", last)
            # print("#count:", count)
            # print("#")

        else :
            answer.append(count)
            count = 1
            check = last.pop(0)
            # print("$check:", check)
            # print("$last:", last)
            # print("$count:", count)
            # print("$")

        if not last:
            answer.append(count)

    # print("=====")
    # print(check)
    # print(last)
    # print(answer)

    return answer

print(solution(progresses, speeds))