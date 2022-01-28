# H-index는 인덱스로

def solution(citations):
    citations = sorted(citations, reverse=True)
    for idx, citation in enumerate(citations):
        if idx >= citation:
            return idx
    
    return len(citations)