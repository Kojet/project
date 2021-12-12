import tkinter as tk
import reader
import manager

def frame(): #front page
    global root
    root = tk.Tk()
    root.geometry('900x700')
    root.title('Library Management System')
    lable0 = tk.Label(root, text='Welcome to our library', bg='#E4007F', font=('Arial', 60)).pack()#上
    canvas = tk.Canvas(root, height=900, width=700)#中
    image_file=tk.PhotoImage(file='cityu.gif')
    image = canvas.create_image(450, 150, image=image_file)
    canvas.place(x=0, y=90)

    lable1 = tk.Label(root, text='Please choose the user type:',font=('Arial', 20)).place(x=150, y=415)#下
    tk.Button(root, text='Reader', font=('Arial', 20), width=20, height=2, command=exit_reader).place(x=310, y=460)
    tk.Button(root, text='Administrator', font=('Arial', 20), width=20, height=2, command=exit_manager).place(x=310, y=550)

    root.mainloop() #necessary

def exit_reader(): #jump to reader login page
    root.destroy()
    reader.frame()

def exit_manager(): #jump to manager login page
    root.destroy()
    manager.frame()

if __name__ == '__main__':
    frame()