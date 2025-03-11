import os

os.environ["OPENBLAS_NUM_THREADS"] = "1"

def change_matrix(matrix,n,i,j):
    directions = [(1,0),(0,1),(-1,0),(0,-1),(1,1),(-1,-1),(-1,1),(1,-1)]
    counter =0
    for di,dj in directions:
        newi,newj = i+di,j+dj
        if 0<= newi <n and 0<=newj<n:
            if matrix[newi][newj] == "#":
                counter+=1
    return str(counter)



if __name__ == "__main__":
    N= int(input())

    matrix = [list(input().split("   ")) for _ in range(N)]

    result_matrix = [
        [ change_matrix(matrix,N,i,j) if matrix[i][j]=="-" else "#"  for j in range(N)]
        for i in range(N)
    ]

    for row in result_matrix:
        print("   ".join(row))
