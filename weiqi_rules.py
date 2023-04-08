import sys
sys.setrecursionlimit(9000000)

def alive(board,x,y,z):#判断相应位置的棋子死活,z=0初始，z=1向上扩展，z=2,向下扩展，z=3,向左扩展，z=4,向右扩展
    if board[x][addone(y)]==2 or board[x][subtractone(y)]==2 or board[addone(x)][y]==2 or board[subtractone(x)][y]==2:
        return True
    if board[x][addone(y)]==1-board[x][y] and board[x][subtractone(y)]==1-board[x][y] and board[addone(x)][y]==1-board[x][y] and board[subtractone(x)][y]==1-board[x][y]:
        return False
    else:
        isalive = False
        if board[x][addone(y)] == board[x][y] and z!=1:
            isalive = alive(board,x,addone(y),2)
        if board[x][subtractone(y)] == board[x][y] and z!=2:
            isalive = alive(board,x,subtractone(y),z=1)
        if board[addone(x)][y] == board[x][y] and z!=3:
            isalive = alive(board,addone(x),y,4)
        if board[subtractone(x)][y] == board[x][y] and z!=4:
            isalive = alive(board,subtractone(x),y,3)
        return isalive
    return False

def addone(z):
    if z<18 and z>=0:
        return z+1
    elif z==18:
        return z-1

def subtractone(z):
    if z>0 and z<=18:
        return z-1
    elif z==0:
        return z+1
