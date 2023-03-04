N,r,c = map(int,input().split())

start = 0
status_dict = {"before":0,"after":1}
def find_Z(N,r,c):
    global start
    if N == 0:
        return start
    
    if r < 2**N // 2 :
        r_status =status_dict["before"]
    else:
        r_status = status_dict["after"]
    
    if c < 2**N//2:
        s_status = status_dict["before"]
    else:
        s_status = status_dict["after"]
    start += 2*4**(N-1) * r_status + 4**(N-1) * s_status
    return find_Z(N-1,r-2**N//2*r_status,c-2**N//2*s_status)
print(find_Z(N,r,c))    


# 1 = 2
# 2 = 8
# 3 = 32

# 1 = 1
# 2 = 4
# 3 = 16