import tkinter as tk
import weiqi_rules as rule
import copy

class qipan():
    def __init__(self):    
        self.board=[] #棋盘
        for i in range(19):
            y=[]
            for j in range(19):
                y.append(2)
            self.board.append(y)
        self.board_window =tk.Tk()
        self.board_window.title('开始下棋吧~~')
        self.board_window.geometry('700x700')
        close_button=tk.Button(self.board_window,text="关闭",command=self.board_window.quit)
        close_button.pack(side="bottom")
        clear_button=tk.Button(self.board_window,text="清空",command=self.clear)
        clear_button.pack(side="bottom")
        board_canvas_size=540
        self.board_canvas = tk.Canvas(self.board_window, bg='goldenrod', height=board_canvas_size+80, width=board_canvas_size+80)

        self.board_canvas.create_line(40, 40, 40, board_canvas_size+40, fill='black', width=3)
        self.board_canvas.create_line(board_canvas_size+40, 40, board_canvas_size+40, board_canvas_size+40, fill='black', width=3)
        for i in range(18):
                self.board_canvas.create_line(i*(board_canvas_size/18)+40, 40, i*(board_canvas_size/18)+40, board_canvas_size+40, activefill='black', width=1)

        self.board_canvas.create_line(40, 40, board_canvas_size+40, 40, fill='black', width=3)
        self.board_canvas.create_line(40, board_canvas_size+40, board_canvas_size+40, board_canvas_size+40, fill='black', width=3)
        for i in range(18):
                self.board_canvas.create_line(40, i*(board_canvas_size/18)+40, board_canvas_size+40, i*(board_canvas_size/18)+40, activefill='black', width=1)

        self.board_canvas.create_oval((board_canvas_size/18)*3+40+3,(board_canvas_size/18)*3+40+3,(board_canvas_size/18)*3+40-3,(board_canvas_size/18)*3+40-3, fill='black')
        self.board_canvas.create_oval((board_canvas_size/18)*15+40+3, (board_canvas_size/18)*15+40+3, (board_canvas_size/18)*15+40-3, (board_canvas_size/18)*15+40-3, fill='black')
        self.board_canvas.create_oval((board_canvas_size/18)*15+40+3,(board_canvas_size/18)*3+40+3,(board_canvas_size/18)*15+40-3,(board_canvas_size/18)*3+40-3, fill='black')
        self.board_canvas.create_oval((board_canvas_size/18)*3+40+3,(board_canvas_size/18)*15+40+3,(board_canvas_size/18)*3+40-3,(board_canvas_size/18)*15+40-3, fill='black')
        self.board_canvas.create_oval(board_canvas_size/2+40+3,board_canvas_size/2+40+3,board_canvas_size/2+40-3,board_canvas_size/2+40-3, fill='black')
        
        self.steps=[] #储存下的每一步
        self.id={} #储存对应位置棋子的id
        self.board_canvas.bind("<Button-1>",self.callback)
        self.board_canvas.pack()
        self.board_window.mainloop()

    def callback(self,event):
        event.x=event.x-40
        event.y=event.y-40
        x=round(event.x/30)
        y=round(event.y/30)
        self.play(x,y)


    def play(self,x,y):
        color=['white','black']
        if (x>=0 and x<=18 and y>=0 and y<=18):
            if self.board[x][y]==2:
                self.steps.append((x,y))
                self.board[x][y]=(len(self.steps))%2 #1为黑棋，0为白棋
                self.id[(x,y)]=self.board_canvas.create_oval(x*30+40-15,y*30+40-15,x*30+40+15,y*30+40+15,fill=color[(len(self.steps))%2])
                self.judge()
    
    def judge(self):
        tempboard=copy.deepcopy(self.board)
        isalive = rule.live(self.board)
        for i in range(19):
            for j in range(19):
                if self.board[i][j] != 2:
                    # isalive=rule.live(self.board,i,j)
                    if isalive[(i,j)]== False: #棋子没有气了
                        self.board_canvas.delete(self.id[(i,j)])
                        tempboard[i][j]=2
        self.board=copy.deepcopy(tempboard)

    def clear(self):
        for x in self.id.keys():
                self.board_canvas.delete(self.id[x])
        for i in range(19):
            for j in range(19):
                self.board[i][j]=2
        self.steps=[]
        self.id={}
        self.board_canvas.bind("<Button-1>",self.callback)
        self.board_canvas.pack()
        self.board_window.mainloop()
        
def main():
    m=qipan()

main()
