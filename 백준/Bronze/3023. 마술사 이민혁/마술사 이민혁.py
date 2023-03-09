R,C = map(int,input().split())

card = [input()for _ in range(R)]
error = list(map(int,input().split()))
for i in range(R):
    for j in range(C-1,-1,-1):
        card[i]+=(card[i][j])

for i in range(R-1,-1,-1):
    card.append(card[i])

if card[error[0]-1][error[1]-1] == '.':
    card[error[0]-1] = card[error[0]-1][:error[1]-1] + '#' + card[error[0]-1][error[1]:]
else:
    card[error[0]-1] = card[error[0]-1][:error[1]-1] + '.' + card[error[0]-1][error[1]:]
for i in card:
    print(i)
