from py2neo import Graph

from tkinter import *
from PIL import ImageTk, Image

g = Graph()

#Buttons functions
def getname(event):
    g.run("CREATE (n:Person {name:{name}}) RETURN n", name=e1.get())
    e1.delete(0, 'end')

def getrel(event):
    g.run("MATCH (a:Person),(b:Person) WHERE a.name = {namef} AND b.name = {namel} CREATE (a)-[r:Friend{name: {namer}}]->(b)",
        namef=e1.get(), namel=e1.get(), namer=e2.get())
    e2.delete(0, 'end')

def getcount(event):
    for i in range(int(e3.get())):
        g.run("CREATE (n:Person {name:{name}}) RETURN n", name="Student_" + str(i + 1))
    e3.delete(0, 'end')

def deleteall(event):
    g.run("match (n) detach delete n")

#Setting main window
root = Tk()
root.iconbitmap("iconbitmap.ico")
root.title("Museum")
root.geometry('900x300+{}+{}'.format(root.winfo_screenwidth()//2 - 350, root.winfo_screenheight()//2 - 300))
root.resizable(width=False, height=False)

#Create frames
left_frame = Frame(root,bg="blue",width=200, height=200)
left_frame.pack(side=LEFT,fill=Y)
center_frame = Frame(root,bg="white",width=200, height=200)
center_frame.pack(side=LEFT,fill=Y)
right_frame = Frame(root, bg="red",width=200, height=200)
right_frame.pack(side=LEFT,fill=Y)

#Load Img
im = Image.open("g.jpg")
img1 = ImageTk.PhotoImage(im.resize((100, 100)))

#Buttons
bt1 = Button(left_frame, text="Confirm")
bt2 = Button(left_frame, text="Confirm")
bt3 = Button(center_frame, text="Confirm")
bt4 = Button(right_frame, text="Confirm")

#Labels
l1 = Label(left_frame, text="Write Name")
l2 = Label(left_frame, text="Write relationship")
l3 = Label(center_frame, text="Write count")
l4 = Label(right_frame, text="Push to delete")
i1 = Label(center_frame, image=img1)
#i1.image = img1  # keep a reference!


#Entry
e1 = Entry(left_frame)
e2 = Entry(left_frame)
e3 = Entry(center_frame)

#Set Widgets
l1.grid(row=0,column=0,sticky=E)
e1.grid(row=0,column=1)
bt1.grid(row=0,column=2)
l2.grid(row=1,column=0)
e2.grid(row=1,column=1)
bt2.grid(row=1,column=2)

l3.grid(row=0,column=0)
e3.grid(row=0,column=1)
bt3.grid(row=0,column=2)
i1.grid(row=1,column=0)

l4.grid(row=0,column=0)
bt4.grid(row=0,column=1)

#Buttons actions
bt1.bind("<Button-1>", getname)
bt2.bind("<Button-1>", getrel)
bt3.bind("<Button-1>", getcount)
bt4.bind("<Button-1>", deleteall)

root.mainloop()