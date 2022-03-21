# tkinterのインポート
import tkinter as tk

# rootメインウィンドウの設定
root = tk.Tk()
root.title("Frame")
root.geometry("300x300")

frame = tk.Frame(root)
frame.grid(row=0,column=1)
entry = tk.Entry(frame)
#StringVar変数を使う
var=tk.StringVar()

#entryに入力された値をvar(StringVar)にセットする
def btnclick():
    var.set(entry.get())

#ラベルに入力する文字列はvarに入力された値
label = tk.Label(frame, textvariable=var)

#ボタンがクリックされたら「def btnclickを実行する」
button = tk.Button(frame, text='ボタン',command=btnclick)

label.grid(row=0,column=2)
entry.grid(row=1,column=2)
button.grid(row=2,column=2)
root.mainloop()
