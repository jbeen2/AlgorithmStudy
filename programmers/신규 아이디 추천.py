def solution(new_id):
    import re

    # phase 1
    new_id = new_id.lower()

    # phase 2
    new_id = re.sub(r'[^a-z0-9\-\_\.]', '', new_id)

    # phase 3
    new_id = re.sub(r'\.\.+', '.', new_id)

    # phase 4
    if new_id.startswith('.'):
        new_id = new_id[1:]

    if new_id.endswith('.'):
        new_id = new_id[:-1]

    # phase 5
    if new_id == '':
        new_id = 'a'

    # phase 6
    if len(new_id) >= 16:
        new_id = new_id[:15]

        if new_id.endswith('.'):
            new_id = new_id[:-1]

    # phase 7
    if len(new_id) == 1:
        new_id = new_id * 3
    elif len(new_id) == 2:
        new_id = new_id + new_id[-1]

    return new_id