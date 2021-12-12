import tkinter as tk
import tkinter.messagebox as msg
import search
from tkinter import ttk
import pymysql


def frame():
    window = tk.Tk()
    window.title('Administrator')
    window.geometry('900x700')
    lable0 = tk.Label(window, text='Welcome to our library', bg='#E4007F', font=('思源黑体', 60)).pack()  # 上

    lable1 = tk.Label(window, text='Please choose your desired operation:', font=('思源黑体', 30)).place(x=80, y=130)  # 下
    tk.Button(window, text='Book Purchase', font=('思源黑体', 20), width=20, height=2, command=purchase).place(x=330, y=250)
    tk.Button(window, text='Book Cancellation', font=('思源黑体', 20), width=20, height=2, command=cancel).place(x=330, y=350)
    tk.Button(window, text='Information Search', font=('思源黑体', 20), width=20, height=2, command=search.frame).place(x=330, y=450)
    window.mainloop()


def purchase():  # 进购图书
    global win
    win = tk.Tk()
    win.title('Administrator')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='Please enter the purchased information:', font=('思源黑体', 30)).place(x=30, y=100)

    tk.Label(win, text='Book Category：', font=('宋体', 12)).place(x=30, y=200)
    global lis  # 这个是一个下拉页表项，只能从下面的list['values']里边选
    comvalue = tk.StringVar()
    lis = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
    lis.place(x=100, y=200)
    lis['values'] = ('ALL', 'Humanity', 'Art', 'Computer', 'Technology', 'Magazine')
    lis.current(0)  # 默认显示'全部'

    global b_name
    tk.Label(win, text='Book Name：', font=('宋体', 12)).place(x=200, y=200)
    b_name = tk.Entry(win, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(win, text='Author：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(win, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    global price
    tk.Label(win, text='Price：', font=('宋体', 12)).place(x=460, y=200)
    price = tk.Entry(win, font=('宋体', 12), width=10)
    price.place(x=510, y=200)

    global amount
    tk.Label(win, text='Count：', font=('宋体', 12)).place(x=560, y=200)
    amount = tk.Entry(win, font=('宋体', 12), width=5)
    amount.place(x=610, y=200)

    tk.Button(win, text='Confirm to add', font=('宋体', 12), width=10, command=add).place(x=700, y=195)


def add():  # 添加图书信息到数据库中
    #*******************************
    b_type = lis.get()
    num = amount.get()
    sql_count = "SELECT COUNT(*) FROM book WHERE book.type = '%s'"%(b_type)
    if b_type == 'ALL':
        b_type = 'ALL'
    else:
        b_type = b_type[0]
    db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
    #建立游标cursor，这个游标可以类比指针，这样理解比较直观
    cursor = db.cursor()
    cursor.execute(sql_count) #sql语句被执行
    result = cursor.fetchone()#得到的结果返回给result数组
    b_id = b_type + str(result[0] + 1)
    if int(num) > 1:
        for i in range(int(num)):
            b_id = b_type + str(result[0] + 1 + i)
            sql = "INSERT INTO book VALUES('%s','%s','%s','%s','%s')" % (
            b_id, b_name.get(), author.get(), lis.get(), price.get())
            db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
            cursor = db.cursor()
            cursor.execute(sql)
            db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
    else:
        sql = "INSERT INTO book VALUES('%s','%s','%s','%s','%s')" % (
        b_id, b_name.get(), author.get(), lis.get(), price.get())
        db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
    db.close()
    msg.showinfo(title='Success！', message='The new book has been put in storage！')

def cancel():  # 撤销图书
    global win
    win = tk.Tk()
    win.title('Administrator')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='Please enter the cancelled information:', font=('思源黑体', 30)).place(x=30, y=100)

    tk.Label(win, text='Book Category：', font=('宋体', 12)).place(x=30, y=200)
    global lis
    comvalue = tk.StringVar()
    lis = ttk.Combobox(win, textvariable=comvalue, height=10, width=10)
    lis.place(x=100, y=200)
    lis['values'] = ('All', 'Humanity', 'Art', 'Computer', 'Technology', 'Magazine')
    lis.current(0)

    global b_name
    tk.Label(win, text='Book Name：', font=('宋体', 12)).place(x=200, y=200)
    b_name = tk.Entry(win, font=('宋体', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(win, text='Author：', font=('宋体', 12)).place(x=350, y=200)
    author = tk.Entry(win, font=('宋体', 12), width=10)
    author.place(x=400, y=200)

    tk.Button(win, text='Confirm to cancel', font=('宋体', 12), width=10, command=delete).place(x=600, y=195)


def delete():
    b_type = lis.get()
    if b_type == 'ALL':
        b_type = 'ALL'
    else:
        b_type = b_type[0]
    sql_d = "SELECT bid FROM book WHERE bid LIKE '{}%' AND name='{}' AND author='{}' LIMIT 1".format(b_type, b_name.get(), author.get())
    db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
    cursor = db.cursor()
    cursor.execute(sql_d)
    result=cursor.fetchone()
    if result:
        b_id = result[0]
        sql = "DELETE FROM book WHERE bid='%s'" % (b_id)
        cursor = db.cursor()
        cursor.execute(sql)
        db.commit()  # 这句不可或缺，当我们修改数据完成后必须要确认才能真正作用到数据库里
        msg.showinfo(title='Success！', message='This book is deleted！')
    else:
        msg.showinfo(title='Error！', message='No such book！')