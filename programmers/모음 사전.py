# Weekly Challenge 5
def solution(word):
    r=0 ; a=[(5**5+5**4+5**3+5**2+5**1)//5, (5**4+5**3+5**2+5**1)//5, (5**3+5**2+5**1)//5, (5**2+5**1)//5, (5**1)//5]
    for i in range(len(word)) :
        r += "AEIOU".find(word[i]) * a[i] + 1
    return r

print(solution('I'))
