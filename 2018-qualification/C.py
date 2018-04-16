import sys

def solve(A):
    l = int(A/3)+1
    t=l*3
    arr = [0]*t
    c = 2
    while True:
        s=str(c)+str(' ')+str(2)+'\n'
        sys.stdout.write(s)
        sys.stdout.flush()
        i,j = map(int, input().split())
        if i == 0 and j == 0:
            return
        arr[(i-1)*3+j-1]=1
        if c < l-1 and arr[(c-2)*3]==1 and arr[(c-2)*3+1]==1 and arr[(c-2)*3+2]==1:
            c+=1

if __name__ == "__main__":
    T = int(input())
    for n in range(T):
        A = int(input())
        solve(A)
