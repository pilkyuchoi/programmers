from collections import defaultdict

def solution(id_list, report, k):
    report = [(ids.split()[0], ids.split()[1]) for ids in set(report)]
    reporter_list = defaultdict(list)
    reported_cnt = defaultdict(int)

    for reporter, reported in report:
        reporter_list[reporter].append(reported)
        reported_cnt[reported] += 1

    answer = []
    for id in id_list:
        cnt = 0
        for reported in reporter_list[id]:
            if reported_cnt[reported] >= k:
                cnt += 1
        answer.append(cnt)

    return answer
