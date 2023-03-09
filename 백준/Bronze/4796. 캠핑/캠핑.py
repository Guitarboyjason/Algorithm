

L, P, V = map(int, input().split())
case_counter = 0
while L != 0:
    case_counter += 1
    summary = 0
    summary += V//P * L

    if V % P < L:
        summary += V % P
    else:
        summary += L
    print("Case {}: {}".format(case_counter, summary))
    L, P, V = map(int, input().split())
