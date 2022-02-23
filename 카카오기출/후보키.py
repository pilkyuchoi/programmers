# set에서 remove는 에러나는데 discard는 에러 안 남

from itertools import combinations

def solution(relation):
    # 행, 열 크기
    n_row, n_col = len(relation), len(relation[0])
    

    # 칼럼 인덱스 조합
    combi = []
    for i in range(1, n_col+1):
        combi.extend(combinations(range(n_col), i))

    # 유일성 검사
    unique = []
    # 칼럼 인덱스 조합별로
    for col_idxs in combi:
        # 칼럼 인덱스에 맞게 데이터 가져와서 set했을 때 전체 행 수와 같은지
        # 리스트는 변경 가능해서 set 불가
        data = [tuple([row[col_idx] for col_idx in col_idxs]) for row in relation]
        if len(set(data)) == n_row:
            unique.append(col_idxs)
    answer = set(unique)

    # 최소성 검사
    # 하나씩 다음 조합들과 검사
    for i in range(len(unique)):
        for j in range(i+1, len(unique)):
            # 튜플이라 issubset이 안 됨, 교집합의 원소 수로 체크
            if len(unique[i]) == len(set(unique[i]).intersection(set(unique[j]))):
                # remove는 에러남
                answer.discard(unique[j])
    
    return len(answer)
    