station = []
for _ in range(4):
    out,person_in = map(int,input().split())
    if station:
        station.append(station[-1]-out+person_in)
    else:
        station.append(person_in)
print(max(station))
        