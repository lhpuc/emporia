# Online Python - IDE, Editor, Compiler, Interpreter

def travelEmporia(x,y,m,n,arr,visit):
    # out of matrix or obstacle 
    if x < 0 or x>=m or y <0 or y>=n or arr[x][y] == 1:
        return 0
    # finish 
    elif arr[x][y]==3:
        return 0 if sum([sum(i) for i in visit])<m*n else 1
    # visited 
    elif visit[x][y] == 1:
        return 0
    else:
        visit[x][y] = 1
        count = travelEmporia(x-1,y,m,n,arr,visit) + travelEmporia(x+1,y,m,n,arr,visit) +travelEmporia(x,y+1,m,n,arr,visit) + travelEmporia(x,y-1,m,n,arr,visit) 
        visit[x][y] = 0
        return count
def main():
    # input 
    arr = [int(x) for x in input().split()]
    m,n = arr[0],arr[1]
    matrix = [[int(x) for x in input().split()] for i in range(0,m)]
    visit = []
    xStart,yStart=0,0
    for i in range(0,m):
        visit.append([])
        for j in range(0,n):
            if matrix[i][j] in [3,1]:
                visit[i].append(1)
            elif matrix[i][j] == 2:
                xStart,yStart = i,j
                visit[i].append(0)
            else:
                visit[i].append(0)
                
    print(travelEmporia(xStart,yStart,m,n,matrix,visit))

if __name__=="__main__": 
    main()