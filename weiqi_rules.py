def live(board):#1为黑棋，0为白棋，判断相应位置的棋子有没有气
    isalive={}
    for x in range(19):
            for y in range(19):
                if board[x][y] !=2:
                     isalive[(x,y)]=False
                     if board[x][addone(y)]==2 or board[x][subtractone(y)]==2 or board[addone(x)][y]==2 or board[subtractone(x)][y]==2:
                           isalive[(x,y)]=True
    for i in range(361):
        for x in range(19):
            for y in range(19):
                if board[x][y] !=2:
                    if isalive[(x,y)]==True:
                        if (board[x][addone(y)]==board[x][y]):
                            isalive[(x,addone(y))]=True
                        if board[x][subtractone(y)]==board[x][y]:
                            isalive[(x,subtractone(y))]=True
                        if board[addone(x)][y]==board[x][y]:
                            isalive[(addone(x),y)]=True
                        if board[subtractone(x)][y]==board[x][y]:
                            isalive[(subtractone(x),y)]=True
    return isalive
       
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
