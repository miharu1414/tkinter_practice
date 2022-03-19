#タブを3つ持つGUIウィンドウを作成する。

#import
import tkinter as tk
import tkinter.ttk as ttk

def main():

    #メインウィンドウ作成
    main_view = tk.Tk()

    #メインウィンドウのタイトルを変更
    main_view.title("東京いいなぁ班のアプリ")

    #メインウィンドウの大きさを設定
    main_view.geometry("1000x500")

    #メインウィンドウにnotebookを作成する。
    nb = ttk.Notebook(main_view)

    #notebookに関するフレームを3つ作る。
    tab1 = tk.Frame(nb)
    tab2 = tk.Frame(nb)
    tab3 = tk.Frame(nb)

    #notebookに対してtab1, 2, 3をそれぞれ追加する。
    nb.add(tab1, text="tab1", padding=3)
    nb.add(tab2, text="tab2", padding=3)
    nb.add(tab3, text="tab3", padding=3)

    #メインフレームでのnotebook配置を決定する。
    nb.pack(expand=1, fill="both")

    #各タブの内容を記載する。
    tab1_main(tab1)
    tab2_main(tab2)
    tab3_main(tab3)

    #main_viewを表示する無限ループ
    main_view.mainloop()

    return 0


# namiki
def tab1_main(tab1):
    #文字を表示する。
    param_name = tk.Label(tab1, text="タブ1の内容")
    param_name.place(x=10, y=10)
    return 0

# takumi
def tab2_main(tab2):
    #文字を表示する。
    param_name = tk.Label(tab2, text="タブ2の内容")
    param_name.place(x=10, y=20)
    return 0

# haruka
def tab3_main(tab3):
    #文字を表示する。
    param_name = tk.Label(tab3, text="タブ3の内容")
    param_name.place(x=10, y=30)
    return 0

if __name__ == "__main__":
    main()