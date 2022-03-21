import tkinter as tk
import tkinter.ttk as ttk


# takumi
def tab2_main(tab2):
    from tkinter import messagebox as mb
    #入力内容をcsvに保存
    def shows():
        mess_show = mess.get()
        user_show = user.get()
        with open('mess.csv', 'a', encoding="utf_8_sig" ) as f :
            f.write(user_show + ',' + mess_show + '\n')
        mb.showinfo('確認', user_show +'さんが投稿しました')
    
    #csvの保存内容を出力
    def write():
        rows = [] 
        f_r = open('mess.csv', 'r', encoding="utf_8_sig")
        l = f_r.readline()
        while l:
            fixed_l = l.rstrip()
            rows.append(fixed_l.split(','))
            l = f_r.readline()
        for i in rows :
                user_write = tk.Label(tab2, 
                                      text='ユーザー名：' + i[0] +' /内容：' + i[1], 
                                      fg = 'orange'
                                      )
                user_write.pack()
                
            
        f_r.close()
    
    #伝言入力フォームの挿入。
    user_name = tk.Label(tab2, 
                         text="ユーザー名を入力", 
                         foreground = '#ff0000'
                         )
    user_name.pack()
  
    user = tk.Entry(tab2, 
                    justify= 'center', 
                    width=50,
                    )
    user.pack()
    
    mess_name = tk.Label(tab2, 
                         text="伝言を入力", 
                         foreground = '#ff0000'
                         )
    mess_name.pack()
    
    mess = tk.Entry(tab2, 
                    width=50,
                    )
    mess.pack()
    
    #ボタン
    mess_button = tk.Button(tab2, 
                            text=u'投稿',
                            command = shows
                            )
    mess_button.pack()

    write_button = tk.Button(tab2, 
                             text=u'投稿内容を見る',
                             command = write
                             )
    write_button.pack()
    
    tab2.mainloop()
    return 0
