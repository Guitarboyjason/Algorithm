N = int(input())
seats = list(input())

seats_with_cup_holder = ["*"]

couple_counter = 0
for seat_index in range(N):
    seats_with_cup_holder.append(seats[seat_index])
    if seats[seat_index] == "S":
        seats_with_cup_holder.append("*")
    elif couple_counter == 1:
        seats_with_cup_holder.append("*")
        couple_counter = 0
    else:
        couple_counter = 1
if seats_with_cup_holder[-1] != "*":
    seats_with_cup_holder.append("*")
    
# print(seats_with_cup_holder)

cnt = 0
for seat_index in range(len(seats_with_cup_holder)):
    if seats_with_cup_holder[seat_index] in ["S","L"]:
        if seats_with_cup_holder[seat_index-1] == "*":
            seats_with_cup_holder[seat_index-1] = "-"
            cnt += 1
        elif seats_with_cup_holder[seat_index+1] == "*":
            seats_with_cup_holder[seat_index+1] = "-"
            cnt += 1
print(cnt)
