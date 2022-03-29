genres = ["classic", "Newage", "pop", "classic", "classic", "pop", "Newage"]
plays =  [500, 1700, 600, 150, 800, 2500, 1500] 

from collections import defaultdict
import operator

def solution(genres, plays):
    answer = []

    record = defaultdict(list)
    cnt = defaultdict(int)
    for i, (genre, play) in enumerate(zip(genres, plays)):
        record[genre].append((i,play))
        cnt[genre] += play

    for genre, _ in sorted(cnt.items(), key=operator.itemgetter(1), reverse=True):
        for i, (idx, _) in enumerate(sorted(record[genre],key=lambda x: x[1], reverse=True)):
            if i > 1:
                break
            answer.append(idx)

    return answer

solution(genres, plays)
