#정규식 표현 알아두기
#re.compile('[a-z0-9._-]').findall('abc123abc')
#isalpha(), isdigit()
#lstrip('a') 앞쪽의 a 지우는 것

import re

def solution(new_id):
    new_id = new_id.lower()
    new_id = ''.join(re.compile('[a-z0-9_.-]').findall(new_id))
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    new_id = new_id.lstrip('.').rstrip('.')
    if not new_id:
        new_id = 'a'
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id[-1] == '.':
            new_id = new_id[:-1]
    if len(new_id) <= 2:
        while len(new_id) < 3:
            new_id += new_id[-1]

    return new_id

