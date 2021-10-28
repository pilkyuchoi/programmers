# 기본적인 소수 판별 방법(2부터 n-1까지 돌려보기)
def is_prime_num(n):
    for i in range(2, n):
        if n % i == 0:
            return False # i로 나누어 떨어지면 소수가 아니므로 False 리턴
    
    return True # False가 리턴되지 않고 for문을 빠져나왔다면 소수이므로 True 리턴
  


# 제곱근까지만 보고 소수를 판별하는 함수
import math

def is_prime_num(n):
    for i in range(2, int(math.sqrt(n))+1): # n의 제곱근을 정수화 시켜준 후 + 1
        if n % i == 0:
            return False

    return True



# 소수 판별 함수(에라토스테네스의 체)
import math

def is_prime_number(n):
    # 2부터 n까지의 모든 수에 대하여 소수 판별
    array = [True for i in range(n+1)] # 처음엔 모든 수가 소수(True)인 것으로 초기화(0과 1은 제외)

    # 에라토스테네스의 체
    for i in range(2, int(math.sqrt(n)) + 1): #2부터 n의 제곱근까지의 모든 수를 확인하며
        if array[i] == True: # i가 소수인 경우(남은 수인 경우)
            # i를 제외한 i의 모든 배수를 지우기
            j = 2
            while i * j <= n:
                array[i * j] = False
                j += 1

    return [ i for i in range(2, n+1) if array[i] ]



