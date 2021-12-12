import tkinter as tk
import tkinter.messagebox as msg
from tkinter import ttk
import search
import ID
import datetime as dt#datetime
import pymysql

def frame():
    window2 = tk.Tk()
    window2.title('Reader')
    window2.geometry('900x700')
    lable0 = tk.Label(window2, text='Welcome to our library', bg='#E4007F', font=('Arial', 60)).pack()  # 上

    lable1 = tk.Label(window2, text='Please choose your desired operation:', font=('Arial', 30)).place(x=70, y=130)  # 下
    tk.Button(window2, text='Borrow', font=('Arial', 20), width=20, height=2,command=borrow).place(x=330, y=250)
    tk.Button(window2, text='Return', font=('Arial', 20), width=20, height=2,command=turnback).place(x=330, y=350)
    tk.Button(window2, text='Information Search', font=('Arial', 20), width=20, height=2,command=search.frame).place(x=330, y=450)
    window2.mainloop()

def borrow():
    global win
    win = tk.Tk()
    win.title('Reader')
    win.geometry('900x300')
    win.wm_attributes('-topmost', 1)
    lable1 = tk.Label(win, text='Please enter the borrowed information:(Make sure the book name and author are correct！)', bg='#E4007F', font=('Arial', 15)).place(x=30, y=100)

    global b_name
    tk.Label(win, text='Book Name：', font=('Arial', 12)).place(x=160, y=200)
    b_name = tk.Entry(win, font=('Arial', 12), width=10)
    b_name.place(x=250, y=200)

    global author
    tk.Label(win, text='Author：', font=('Arial', 12)).place(x=330, y=200)
    author = tk.Entry(win, font=('Arial', 12), width=10)
    author.place(x=400, y=200)

    global b_ID

    tk.Button(win, text='Confirm to borrow', font=('Arial', 12), width=20, command=confirm_borrow).place(x=600, y=195)

def confirm_borrow():
    db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
    cursor = db.cursor()
    if not b_name.get() or not author.get():
        #msg.showinfo(title='Error！', message='Please enter the book name and author name！')
        result = None
    else:
        sql0="SELECT bid FROM book WHERE name='%s' AND author='%s' AND bid NOT IN \
        (SELECT bid FROM borrow)" % (b_name.get(), author.get())
        cursor.execute(sql0)
        result=cursor.fetchone()
    if result:
        time = dt.datetime.now().strftime('%F')#得到的时间不是字符串型，我们要把时间转化成字符串型
        b_id = result[0]
        sql1 = "INSERT INTO borrow VALUES('%s','%s','%s')" % (b_id,ID.getid(),time)
        cursor.execute(sql1)
        db.commit()
        db.close()
        win.destroy()
        msg.showinfo(title='Success！', message='Borrow successfully！Please return within one month')
    else:
        msg.showinfo(title='Error！', message='Fail to locate the book！')

def turnback():#还书
    global win
    win = tk.Tk()
    win.title('Reader')
    win.geometry('550x600')

    db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
    cursor = db.cursor()
    sql0 = "SELECT COUNT(*) FROM borrow WHERE uid='%s'" % (ID.getid())
    cursor.execute(sql0)
    result = cursor.fetchone()
    if result[0]==0:
        msg.showinfo(title='Error', message='You do not have borrowed record！')
    else :
        lable1 = tk.Label(win, text='The following books are not returned：', bg='#E4007F', font=('Arial', 15)).place(x=50, y=20)
        tree = ttk.Treeview(win, columns=('1', '2', '3'), show="headings")
        tree.column('1', width=150, anchor='center')
        tree.column('2', width=150, anchor='center')
        tree.column('3', width=150, anchor='center')
        tree.heading('1', text='Book ID')
        tree.heading('2', text='Book Name')
        tree.heading('3', text='Author')
        tree.place(x=50, y=100)

        sql1 = "SELECT b.bid, b.name, b.author FROM borrow a, book b WHERE a.uid='%s' \
            AND b.bid=a.bid" % (ID.getid())
        cursor.execute(sql1)
        result1 = cursor.fetchall()
        for i in range(0,result[0]):
            tree.insert('', i, values=(result1[i]))

        lable2 = tk.Label(win, text='Please enter the returned information：', bg='#E4007F', font=('Arial', 15)).place(x=50, y=360)
        lable22=tk.Label(win, text='Make sure the book name and author are correct！', bg='#E4007F', font=('Arial', 15)).place(x=50, y=400)
        global b_ID
        tk.Label(win, text='Book ID：', font=('Arial', 12)).place(x=40, y=480)
        b_ID = tk.Entry(win, font=('Arial', 12), width=10)
        b_ID.place(x=130, y=480)

        global b_name
        tk.Label(win, text='Name：', font=('Arial', 12)).place(x=220, y=480)
        b_name = tk.Entry(win, font=('Arial', 12), width=10)
        b_name.place(x=280, y=480)

        tk.Button(win, text='Confirm to return', font=('Arial', 12), width=20, command=confirm_turnback).place(x=370, y=475)
    db.close()

def confirm_turnback():
    if not b_ID.get() and not b_name.get():
        msg.showinfo(title='Error', message='Please enter the book id or the book name!')
    else:
        if not b_ID.get() and b_name.get():
            sql0 = "SELECT bid FROM book WHERE name='%s' AND bid IN\
            (SELECT bid FROM borrow)" % (b_name.get())
        else:
            sql0 = "SELECT bid FROM borrow WHERE bid='%s' AND uid='%s'" % (b_ID.get(), ID.getid())

        db = pymysql.connect(host="120.79.31.91", user="visitor", password="1234", database="library")
        cursor = db.cursor()
        cursor.execute(sql0)
        result = cursor.fetchall()
        if result:
            b_id = result[0]
            time1=dt.datetime.now()#获取现在的时间
            sql1="SELECT date FROM borrow WHERE bid='%s'"%(b_id)
            cursor.execute(sql1)
            result1 = cursor.fetchone()
            day=(time1-result1[0]).days #得到时间差，检查图书是否超期
            print(day)
            if day>30:
                msg.showinfo(title='Return successfully', message='Return successfully，but you are overdue！Please return on time next time')
            else:
                msg.showinfo(title='Return successfully', message='Return successfully，and no more than 30 days')

            sql2 = "DELETE FROM borrow WHERE bid='%s'" % (b_id)
            cursor.execute(sql2)
            db.commit()
            db.close()
            win.destroy()
        else:
            msg.showinfo(title='Error', message='You do not have this borrowed record!')
            win.destroy()

