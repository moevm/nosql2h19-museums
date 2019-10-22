from tkinter import *
from PIL import ImageTk, Image

root_window = Tk()
root_window.iconbitmap("iconbitmap.ico")
root_window.title("Museum")
root_window.geometry('600x400+{}+{}'.format(root_window.winfo_screenwidth()//2 - 350, root_window.winfo_screenheight()//2 - 300))
root_window.resizable(width=False, height=False)

im = Image.open("g.jpg")
img1 = ImageTk.PhotoImage(im.resize((300, 300)))

def create_widgets_in_first_frame():
    f1 = Frame(first_frame)
    f1.pack(side=LEFT)

    bt0 = Button(f1,text="1st")
    bt1 = Button(f1,text="2st")
    bt2 = Button(f1,text="3st")
    bt3 = Button(f1,text="4st")
    bt4 = Button(f1,text="5st")
    bt5 = Button(f1,text="Next", command = call_second_frame_on_top)
    bt6 = Button(f1,text="Exit", command = quit_program)

    l0 = Label(f1, text="First Item")
    l1 = Label(f1, text="Second Item")
    l2 = Label(f1, text="Third Item")
    l3 = Label(f1, text="Fourth Item")
    l4 = Label(f1, text="Fifth Item")

    i1 = Label(f1, image=img1)

    e0 = Entry(f1)
    e1 = Entry(f1)
    e2 = Entry(f1)
    e3 = Entry(f1)
    e4 = Entry(f1)

    l0.grid(row=0,column=0)
    l1.grid(row=1,column=0)
    l2.grid(row=2,column=0)
    l3.grid(row=3,column=0)
    l4.grid(row=4,column=0)

    e0.grid(row=0, column=1)
    e1.grid(row=1, column=1)
    e2.grid(row=2, column=1)
    e3.grid(row=3, column=1)
    e4.grid(row=4, column=1)

    bt0.grid(row=0, column=2)
    bt1.grid(row=1, column=2)
    bt2.grid(row=2, column=2)
    bt3.grid(row=3, column=2)
    bt4.grid(row=4, column=2)
    bt5.grid(row=5, column=0)
    bt6.grid(row=5, column=2)

    i1.grid(row=0,rowspan=12,column=3,columnspan=7, padx=50)

def create_widgets_in_second_frame():
    l1 = Label(second_frame,text="The second label")
    l1.grid(row=0,column=0)
    l2 = Label(second_frame,text="Sort by:")
    l2.grid(row=1,column=0)
    variable = StringVar(second_frame)
    variable.set("A-Z")

    w = OptionMenu(second_frame, variable, "A-Z", "Z-A", "Data", "Rating")
    w.grid(row=1,column=1, columnspan=2)

def call_second_frame_on_top():
    first_frame.grid_forget()
    second_frame.pack()

def quit_program():
    root_window.destroy()

first_frame=Frame(root_window)
first_frame.grid(column=0, row=0)

second_frame=Frame(root_window)
second_frame.grid(column=0, row=0)

create_widgets_in_second_frame()
create_widgets_in_first_frame()

second_frame.grid_forget()

root_window.mainloop()