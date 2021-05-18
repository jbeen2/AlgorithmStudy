N = int(input())
meetings = sorted([list(map(int, input().split())) for _ in range(N)])
meetings = sorted(meetings, key = lambda x : x[1])

last, cnt = 0, 0
for start, end in meetings :
    if start >= last :
        cnt += 1
        last = end

print(cnt)

# ============ Time Exceed ============
# meetings = sorted([list(map(int, input().split())) for _ in range(N)])
#
# answer = []
# for i in range(len(meetings)//2) :
#     temp = [meetings[i]]
#     for j in range(i+1, len(meetings)) :
#         start, end = meetings[j][0], meetings[j][1]
#         if start >= temp[-1][1] :
#             temp.append([start, end])
#     answer.append(temp)
#
# print(meetings)
# print(answer)
# print(max([len(a) for a in answer]))
