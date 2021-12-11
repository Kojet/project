import tkinter as tk
import reader
import manager

def frame():#初始界面
    global root
    root = tk.Tk()
    root.geometry('900x700')
    root.title('Library Management System')
    lable0 = tk.Label(root, text='Welcome to our library', bg='blue', font=('思源黑体', 60)).pack()#上
	#canvas是个画布，想要插入图片的话首先要定义个canvas
    canvas = tk.Canvas(root, height=900, width=700)#中
    image_file=tk.PhotoImage(file='cityu.gif')
    #图片文件的后缀必须是.gif，且亲测不能自行鼠标右键重命名更改成.gif，要用win10里内置的画图功能，打开图片然后另存为的时候选择.gif
    #图片文件必须放到你的项目目录里边才有效
    image = canvas.create_image(450, 150, image=image_file)
    canvas.place(x=0, y=90)

    lable1 = tk.Label(root, text='Please choose the user type:',font=('思源黑体', 30)).place(x=150, y=400)#下
    tk.Button(root, text='Reader', font=('思源黑体', 20), width=10, height=2, command=exit_reader).place(x=360, y=460)
    tk.Button(root, text='Administrator', font=('思源黑体', 20), width=10, height=2, command=exit_manager).place(x=360, y=550)

    root.mainloop()#必须要有这句话，你的页面才会动态刷新循环，否则页面不会显示

def exit_reader():#跳转至读者界面
    root.destroy()
    reader.frame()

def exit_manager():#跳转至管理员界面
    root.destroy()
    manager.frame()

if __name__ == '__main__':
    frame()