import tkinter as tk
import reader
import manager

def frame():#初始界面
    global root
    root = tk.Tk()
    root.geometry('900x700')
    root.title('Library Management System')
    lable0 = tk.Label(root, text='Welcome to our library', bg='#E4007F', font=('Arial', 60)).pack()#上
	#canvas是个画布，想要插入图片的话首先要定义个canvas
    canvas = tk.Canvas(root, height=900, width=700)#中
    image_file=tk.PhotoImage(file='cityu.gif')
    image = canvas.create_image(450, 150, image=image_file)
    canvas.place(x=0, y=90)

    lable1 = tk.Label(root, text='Please choose the user type:',font=('Arial', 20)).place(x=150, y=415)#下
    tk.Button(root, text='Reader', font=('Arial', 20), width=20, height=2, command=exit_reader).place(x=310, y=460)
    tk.Button(root, text='Administrator', font=('Arial', 20), width=20, height=2, command=exit_manager).place(x=310, y=550)

    root.mainloop()#必须要有这句话，你的页面才会动态刷新循环，否则页面不会显示

def exit_reader():#跳转至读者界面
    root.destroy()
    reader.frame()

def exit_manager():#跳转至管理员界面
    root.destroy()
    manager.frame()

if __name__ == '__main__':
    frame()