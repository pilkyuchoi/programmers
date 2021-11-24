# datetime은 기본 모듈
# datetime.date(연, 월, 일).strftime('%a')하면 요일 나옴
# date 객체에 year, month, day, weekday 가능
# timedelta는 연산 가능

import datetime

def solution(a, b):
    return datetime.date(2016,a,b).strftime('%a').upper()