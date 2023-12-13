n=int(input())

# n x n
grid = []
for _ in range(n):
    t = list(map(int,input().split()))
    grid.append(t)

def test(rows,rowe,cols,cole):
    num_of_coin = 0

    for row in range(rows,rowe+1):
        for col in range(cols,cole+1):
            num_of_coin += grid[row][col]

    return num_of_coin

answer=0
for row in range(n):
    for col in range(n):
        if row + 2 >= n or col + 2 >= n:
            continue
        
        num_of_coin  = test(row,row+2,col,col+2)

        answer = max(answer,num_of_coin)

print(answer)