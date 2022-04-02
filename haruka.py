import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg, NavigationToolbar2Tk

# haruka
def tab3_main(tab3):
    #文字を表示する。
    param_name = tk.Label(tab3, text="test score", anchor = tk.S, font=("MSゴシック", "20", "bold"))
    param_name.place(x=1, y=1)
    #背景
    tab3.configure(bg = 'light steel blue')
    
    #ラベル
    lb1 = tk.Label(tab3, text = '国語')
    lb1.place(x = 10, y = 110)
    lb2 = tk.Label(tab3, text = '数学')
    lb2.place(x = 10, y = 130)
    lb3 = tk.Label(tab3, text = '理科')
    lb3.place(x = 10, y = 150)
    lb4 = tk.Label(tab3, text = '社会')
    lb4.place(x = 10, y = 170)
    lb5 = tk.Label(tab3, text = '英語')
    lb5.place(x = 10, y = 190)
    lb6 = tk.Label(tab3, text = '自分の点数')
    lb6.place(x = 80, y = 80)
    lb7 = tk.Label(tab3, text = '平均点')
    lb7.place(x = 240, y = 80)
    
    
    #テキストボックス
    tk1 = tk.Entry(tab3, width = 20)
    tk1.place(x = 50, y = 110)
    tk2 = tk.Entry(tab3, width = 20)
    tk2.place(x = 50, y = 130)
    tk3 = tk.Entry(tab3, width = 20)
    tk3.place(x = 50, y = 150)
    tk4 = tk.Entry(tab3, width = 20)
    tk4.place(x = 50, y = 170)
    tk5 = tk.Entry(tab3, width = 20)
    tk5.place(x = 50, y = 190)
    
    tk6 = tk.Entry(tab3, width = 20)
    tk6.place(x = 200, y = 110)
    tk7 = tk.Entry(tab3, width = 20)
    tk7.place(x = 200, y = 130)
    tk8 = tk.Entry(tab3, width = 20)
    tk8.place(x = 200, y = 150)
    tk9 = tk.Entry(tab3, width = 20)
    tk9.place(x = 200, y = 170)
    tk10 = tk.Entry(tab3, width = 20)
    tk10.place(x = 200, y = 190)
    
   #グラフを表示する関数 
    def btn_push():
        fig = plt.figure()
        
        labels = ['Japanese', 'Math', 'Science', 'Society', 'English']
        width = 0.2
        height1 = [int(tk1.get()), int(tk2.get()), int(tk3.get()),int(tk4.get()), int(tk5.get())]
        height2 = [int(tk6.get()), int(tk7.get()), int(tk8.get()),int(tk9.get()), int(tk10.get())]
        x = np.arange(len(height1))
        plt.bar(x, height1, color = 'r',tick_label = labels, width = 0.2)
        plt.bar(x + width, height2, color = 'b',tick_label = labels, width = 0.2)
        plt.xticks(x + width/2, labels)
        plt.ylim(0, 100)
        plt.show()
        
        canvas = FigureCanvasTkAgg(fig, tab3)  
        canvas.draw()
        canvas.get_tk_widget().pack()
           
    #ボタン
    btn = tk.Button(tab3, text = '実行', command = btn_push)
    btn.place(x =170, y = 220)
    
    
    return 0
