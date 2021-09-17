def solution(record):
    user = dict() ; log = []
    for r in record :
        try : user[r.split()[1]] = r.split()[2]
        except : pass
    for r in record :
        if r.split()[0] == 'Enter' :
            log.append('{}님이 들어왔습니다.'.format(user[r.split()[1]]))
        elif r.split()[0] == 'Leave' :
            log.append('{}님이 나갔습니다.'.format(user[r.split()[1]]))
    return log


# Example
record = ["Enter uid1234 Muzi","Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]
result = ["Prodo님이 들어왔습니다.","Ryan님이 들어왔습니다.", "Prodo님이 나갔습니다.", "Prodo님이 들어왔습니다."]

print(solution(record))