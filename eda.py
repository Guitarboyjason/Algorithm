import sys
sys.stdin = open('input.txt')
input = sys.stdin.readlines

hard = input()
# print(a)
# hard = [i[:-1] for i in hard if i != '\n']

# hard = input()
hard = [int(i.replace("\t","").replace("\n","")) for i in hard if i != '\n']
# print(hard)
print(len(list(set(hard))))

# hard_wr = open("confusing.txt","w")
# hard_wr.write(str(sorted(list(set(hard))))[1:-1])