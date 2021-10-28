# itertools #리스트로 만들면 원소는 튜플로

# product('ABCD', repeat=2) AA AB AC AD BA BB BC BD CA CB CC CD DA DB DC DD
# 모든 조합 허용. 사전적 정의는 중복순열

# permutations('ABCD', 2) AB AC AD BA BC BD CA CB CD DA DB DC
# 하나가 정해지면 다음 것은 정해진 것을 제외하고 선택됨.

# combinations('ABCD', 2) AB AC AD BC BD CD
# 한번 조합을 만들면 이후 같은 조합은 제외. 즉, AB가 한 번 나오면 BA는 같은 조합이므로 제외.
# 같은 글자는 비허용.

# combinations_with_replacement('ABCD', 2) AA AB AC AD BB BC BD CC CD DD
# 같은 글자 허용.


#set 원소추가는 add, 여러개는 update, 삭제는 remove, discard(없어도 에러 안 남)


from itertools import permutations, combinations
import math

def isPrime(n):
    if n <= 1:
            return False

    for i in range(2, int(math.sqrt(n))+1):
        if n % i == 0:
            return False
    
    return True

def solution(numbers):
    s = set()
    for i in range(1, len(numbers)+1):
        s.update([int(''.join(num)) for num in set(permutations(numbers, i))])

    answer = 0
    for num in s:
        if isPrime(num):
            answer += 1
    
    return answer

