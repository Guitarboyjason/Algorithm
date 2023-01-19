#나중에 다시 풀자

def merge_sort(A,p,r):
    if A[p]<A[r]:
        q = (p+r)//2
        merge_sort(A,p,q)
        merge_sort(A,q+1,r)
        merge(A,p,q,r)

def merge(A,p,q,r):
    i,j,t = p,q,-1
    while (i<=q and j <= r):
        if A[i] <= A[j]:

