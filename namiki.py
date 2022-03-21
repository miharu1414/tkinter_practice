# namiki
import tkinter as tk
import tkinter.ttk as ttk


def tab1_main(tab1):
    #文字を表示する。
    global tk
    param_name = tk.Label(tab1, text="タブ1の内容")
    param_name.place(x=10, y=10)
    return 0