# Weekly Challenge 4
def solution(table, languages, preference):
    score = {t.split()[0]:t.split()[1:][::-1] for t in table}
    answer = {t.split()[0]: 0 for t in table}
    for comp, lang in score.items() :
        for l, p in zip(languages, preference) :
            if l in lang :
                answer[comp] += (lang.index(l)+1) * p
    answer = sorted(answer.items(), key = lambda x: (-x[1], x[0]))
    return answer[0][0]

table = ["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"]
languages = ["JAVA", "JAVASCRIPT"]
preference = [7, 5]

print(solution(table, languages, preference))

