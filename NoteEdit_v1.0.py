import tkinter as tk

window = tk.Tk()
window.title("NoteEdit *untitled*") #初始化
window.geometry("2000x1000")

text = tk.Text(window, show=None, width=1000, height=50)
text.pack()
path = tk.Entry(window, show=None, width=1000)
path.pack()

def _save(): #保存
    with open(path.get(),"w") as file:
        #清除文件内容
        file.truncate(0)
        #写入
        file.write(text.get())

def _close(): #关闭
    path.delete(0, "end")
    text.delete("1.0", "end")
    _set_title("/*untitled*")

def _open(): #打开
    with open(path.get(),"r") as file:
        text.delete("1.0", "end")
        text.insert("insert", file.read())
        _set_title(path.get())

def _set_title(_str): #设置标题
    i = 0
    note = []
    while i != len(_str):
        if _str[i] == "/":
            note.append(i)
        i += 1
    i = note[len(note) - 1] + 1
    _note = ""
    while i != len(_str):
        _note += _str[i]
        i += 1
    window.title("NoteEdit "  + _note)

#文件操作
Save = tk.Button(window, text='保存', font=('System', 10), width=5, height=1, command=_save)
Save.pack(side="left")
Close = tk.Button(window, text='关闭', font=('System', 10), width=5, height=1, command=_close)
Close.pack(side="left")
Open = tk.Button(window, text='打开', font=('System', 10), width=5, height=1, command=_open)
Open.pack(side="left")

window.mainloop()
