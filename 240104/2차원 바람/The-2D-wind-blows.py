n,m,q = map(int,input().split())
_matrix = [list(map(int,input().split())) for _ in range(n)]
matrix = [[elem for elem in row] for row in _matrix]
pos = [tuple(map(int,input().split())) for _ in range(q)]

# def _get_sq(r1,c1,r2,c2):
#     sq = [[matrix[row][col] for col in range(c1-1,c2)] for row in range(r1-1,r2)]
#     return sq

def _rotate(r1,c1,r2,c2):
    r1,c1,r2,c2 = r1-1,c1-1,r2-1,c2-1
    popped = matrix[r1][c1]
    for i in range(r1,r2):
        matrix[i][c1] = matrix[i+1][c1]
    for i in range(c1,c2):
        matrix[r2][i] = matrix[r2][i+1]
    for i in range(r2,r1,-1):
        matrix[i][c2] = matrix[i-1][c2]
    for i in range(c2,c1,-1):
        matrix[r1][i] = matrix[r1][i-1]
    matrix[r1][c1+1] = popped

from math import floor
def _mean(r,c):
    arr = [matrix[r][c]]
    drs,dcs = (-1,0,1,0),(0,1,0,-1)
    for dr,dc in zip(drs,dcs):
        nr,nc = r+dr,c+dc
        if 0<=nr<n and 0<=nc<m:
            arr.append(matrix[nr][nc])
    return floor(sum(arr)/len(arr))

def get_mean(r1,c1,r2,c2):
    # rotate(r1,c1,r2,c2)
    _rotate(r1,c1,r2,c2)
    sq = [[_mean(r,c) for c in range(c1-1,c2)] for r in range(r1-1,r2)]
    w,h = abs(c2-c1),abs(r2-r1)
    for row in range(h+1):
        for col in range(w+1):
            matrix[r1+row-1][c1+col-1] = sq[row][col]

for r1,c1,r2,c2 in pos:
    get_mean(r1,c1,r2,c2)

for row in matrix:
    print(*row)