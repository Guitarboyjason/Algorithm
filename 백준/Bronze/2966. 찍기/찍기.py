N = int(input())
answer = input()

sang_guess = ['A','B','C'] * 34
chang_guess = ["B","A","B","C"] * 25
hyun_guess = ["C","C","A","A","B","B"] * 17

sang_score = 0
chang_score = 0
hyun_score = 0

for i in range(N):
    if answer[i] == sang_guess[i]:
        sang_score+=1
    if answer[i] == chang_guess[i]:
        chang_score += 1
    if answer[i] == hyun_guess[i]:
        hyun_score += 1

max_score = max(sang_score,chang_score,hyun_score)
print(max_score)
if max_score == sang_score:
    print("Adrian")
if max_score == chang_score:
    print("Bruno")
if max_score == hyun_score:
    print("Goran")
