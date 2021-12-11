import tkinter as tk
import tkinter.messagebox as msg #这个是会弹出一个警告/提示小框
import initial
import pymysql
import ID

def frame():#管理员界面
    global root
    root= tk.Tk()
    root.geometry('900x700')
    root.title('Library Management System')
    lable0 = tk.Label(root, text='Administrator login', bg='#E4007F', font=('思源黑体', 60)).pack()  # 上
    canvas = tk.Canvas(root, height=900, width=700)#中
    image_file=tk.PhotoImage(file='cityu.gif')
    image = canvas.create_image(450, 150, image=image_file)
    canvas.place(x=0, y=90)

    lable1 = tk.Label(root, text='Please choose:', font=('思源黑体', 30)).place(x=80, y=415)  # 下
    tk.Button(root, text='Login', font=('思源黑体', 25), width=10, height=2, command=login).place(x=150, y=500)
    tk.Button(root, text='Register', font=('思源黑体', 25), width=10, height=2, command=register).place(x=350, y=500)
    tk.Button(root, text='Logout', font=('思源黑体', 25), width=10, height=2, command=exit_manager).place(x=550, y=500)
    root.mainloop()

def login():#登录小窗口
    global root1
    root1=tk.Tk()
    root1.wm_attributes('-topmost', 1)#将登录窗口置顶不至于被遮到下面
    root1.title('Administrator Login')
    root1.geometry('500x300')

    lable1 = tk.Label(root1, text='Account：', font=30).place(x=90,y=50)
    lable2 = tk.Label(root1, text='Password：', font=30).place(x=80, y=100)

    global entry_name, entry_key
    name = tk.StringVar()
    key = tk.StringVar()

    entry_name = tk.Entry(root1, textvariable=name, font=25)
    entry_name.place(x=180, y=50)
    entry_key = tk.Entry(root1, textvariable=key, font=25,show='*')
    entry_key.place(x=180, y=100)
    # 百度：tkinter要求由按钮（或者其它的插件）触发的控制器函数不能含有参数,若要给函数传递参数，需要在函数前添加lambda：
    button1 = tk.Button(root1, text='Confirm', height=2, width=10, command=lambda: ID.id_check('1'))
    button1.place(x=210, y=180)
#当我们输入账号和密码，点击确定时候，会调用ID模块里的id_check()函数，1是参数，表示其身份是管理员
def register():#注册小窗口
    global root2
    root2 = tk.Tk()
    root2.wm_attributes('-topmost', 1)
    root2.title('Administrator Registration')
    root2.geometry('500x300')

    lable1 = tk.Label(root2, text='Login：', font=20).place(x=120, y=50)
    lable2 = tk.Label(root2, text='Password：', font=20).place(x=90, y=100)
    lable2 = tk.Label(root2, text='Confirm Password：', font=20).place(x=10, y=150)

    global entry_name, entry_key, entry_confirm
    name = tk.StringVar()
    key = tk.StringVar()
    confirm = tk.StringVar()
    entry_name = tk.Entry(root2, textvariable=name, font=25)
    entry_name.place(x=180, y=50)
    entry_key = tk.Entry(root2, textvariable=key, font=25, show='*')
    entry_key.place(x=180, y=100)
    entry_confirm = tk.Entry(root2, textvariable=confirm,font=25, show='*')
    entry_confirm.place(x=180, y=150)
    # 百度：tkinter要求由按钮（或者其它的插件）触发的控制器函数不能含有参数,若要给函数传递参数，需要在函数前添加lambda：
    button1 = tk.Button(root2, text='Confirm', height=2, width=10, command=lambda: ID.id_write('1'))
    button1.place(x=210, y=200)
#当我们点击确定的时候，会调用ID模块里的id_write()函数，1是参数，表示其身份是管理员
def exit_manager():#退出管理员界面，跳转至初始界面
    root.destroy()
    initial.frame()