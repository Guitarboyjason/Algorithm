import sys
sys.stdin = open("baekjoon/input.txt","rt")

dict_score = {"A+":4.5,
"A0":4.0,
"B+":3.5,
"B0":3.0,
"C+":2.5,
"C0":2.0,
"D+":1.5,
"D0":1.0,
"F"	:0.0
}

all_credits = 0
all_score = 0
for _ in range(20):
    subject,credit,score = input().split()
    if score == "P":
        continue
    all_credits += int(credit[0])
    all_score += dict_score[score] * int(credit[0])
print(all_score/all_credits)
        