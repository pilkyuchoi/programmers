# re.split, re.findall 외우기
# 정규표현식 쓰는 법 익히기

expression = "100-200*300-500+20"

# '-100*-520'.count('-')

from itertools import permutations
import re

operators = list(permutations(['+','-','*'],3))
operators

top = 0
for oper in operators:
    express = expression
    for op in oper:
        for i in range(express.count(op)):
            e = re.findall(f'\d+\{op}-?\d+', express)[0]
            print(e)
            express = express.replace(e,str(eval(e)))
    top = max(top, abs(eval(express)))

top