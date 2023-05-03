def solution(name, yearning, photo):
    answer = []
    # missing = {i:0 for i in name}
    missing = dict()
    for idx,miss in zip(name,yearning):
        missing[idx] = miss
    for ph in photo:
        answer.append(sum([missing[i] for i in ph if i in missing]))
    return answer