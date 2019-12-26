import tkinter
from tkinter import messagebox
import json
from PIL import ImageTk, Image
from py2neo import Graph

graph = Graph()

hallname = ""
ex = ""
glauthor = ""
glcat = ""
glloc = ""

with open('1.json', encoding='utf-8') as data_file:
    json = json.load(data_file)

def mainWindow(*w, **kw):
    root = tkinter.Tk()
    root.title('Главное окно')

    def butHalls():
        root.destroy()
        HallsWindow()

    def butAdmin():
        root.destroy()
        adminWindow()

    def import_data():
        graph.delete_all()
        query = """
        WITH {json} AS bd
        UNWIND bd.hall AS hall
        UNWIND hall.exhibits AS ex
        MERGE (h:Hall {name: hall.name})
        MERGE (e:Exhibit {id: ex.id})
        ON CREATE SET e.type = ex.type, e.location = ex.location, e.author = ex.author, e.date = ex.date, e.name = ex.name
        MERGE (h)-[:HAS]->(e)
        """
        graph.cypher.execute(query, json=json)

    def export_data():
        pass

    first_window_label = tkinter.Label(root, text='Приложение для ведения базы данных Музея')
    first_window_label.grid(column=0, row=0, pady=10, padx=10, sticky=(tkinter.N))

    first_window_user = tkinter.Button(root, text="Продолжить как Гость", command=butHalls)
    first_window_user.grid(column=0, row=1, pady=10, sticky=(tkinter.N))
    first_window_next_button = tkinter.Button(root, text="Продолжить как Администратор",
                                              command=butAdmin)
    first_window_next_button.grid(column=0, row=2, pady=10, sticky=(tkinter.N))
    first_window_import = tkinter.Button(root, text="Импорт", command=import_data)
    first_window_import.grid(column=5, row=3, pady=10, sticky=(tkinter.N))
    first_window_export = tkinter.Button(root, text="Экспорт", command=export_data)
    first_window_export.grid(column=6, row=3, pady=10, sticky=(tkinter.N))

    root.mainloop()

def adminWindow(*w, **kw):
    root = tkinter.Tk()
    root.title('Окно администратора')

    def next():
        if ((name.get()=="gleb" and password.get()=="gleb") or (name.get()=="anton" and password.get()=="anton")):
            root.destroy()
            nextWin()
        else:
            messagebox.showinfo("Ошибка", "Повторите ввод")

    def butCallback():
        root.destroy()
        mainWindow()

    first_window_user = tkinter.Button(root, text="<", command=butCallback)
    first_window_user.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    name = tkinter.StringVar()
    password = tkinter.StringVar()

    name_label = tkinter.Label(text="Введите ник:")
    surname_label = tkinter.Label(text="Введите пароль:")

    name_label.grid(row=1, column=0, sticky="w")
    surname_label.grid(row=2, column=0, sticky="w")

    name_entry = tkinter.Entry(textvariable=name)
    surname_entry = tkinter.Entry(textvariable=password)

    name_entry.grid(row=1, column=1, padx=5, pady=5)
    surname_entry.grid(row=2, column=1, padx=5, pady=5)

    next_button = tkinter.Button(text="Sign in", command=next)
    next_button.grid(row=3, column=1, padx=5, pady=5, sticky="e")

    root.mainloop()

def nextWin(*w, **kw):

    root = tkinter.Tk()
    root.title('Admin')

    def butCallback():
        root.destroy()
        adminWindow()

    def add():
        root.destroy()
        AddWindow()

    def delete():
        root.destroy()
        DeleteWindow()

    def stat():
        root.destroy()
        StatWindow()

    first_window_user = tkinter.Button(root, text="<", command=butCallback)
    first_window_user.grid(column=0, row=0, pady=10, sticky=(tkinter.N))

    addButton = tkinter.Button(root, text = "Добавить экспонат", command=add)
    addButton.grid(column=1, row=4, pady=10, sticky=(tkinter.N))
    deleteButton = tkinter.Button(root, text = "Удалить экспонат", command=delete)
    deleteButton.grid(column=1, row=5, pady=10, sticky=(tkinter.N))
    statButton = tkinter.Button(root, text = "Редактировать экспонат", command=stat)
    statButton.grid(column=1, row=6, pady=10, sticky=(tkinter.N))

    root.mainloop()

def AddWindow():
    root = tkinter.Tk()
    root.title('Окно добавления')

    def add():
        graph.cypher.execute(
            "CREATE (a:Exhibit {date:{date}, name:{name}, location:{location}, id:{id}, type:{type}, author:{author}})<-[:HAS]-(b:Hall {name:{hallName}})",
            hallName=hall.get(),
            date=int(date),
            name=name.get(),
            location=location.get(),
            id=int(id),
            type=type.get(),
            author=author.get())

    def butCallback():
        root.destroy()
        nextWin()

    first_window_user = tkinter.Button(root, text="<", command=butCallback)
    first_window_user.grid(column=0, row=1, pady=10, sticky=(tkinter.N))

    nameLabel = tkinter.Label(text="Название: ", fg="#eee", bg="#333")
    nameLabel.grid(column=0, row=2, pady=10, padx=10, sticky=(tkinter.N))
    authorLabel = tkinter.Label(text="Автор: ", fg="#eee", bg="#333")
    authorLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))
    dateLabel = tkinter.Label(text="Дата: ", fg="#eee", bg="#333")
    dateLabel.grid(column=0, row=4, pady=10, padx=10, sticky=(tkinter.N))
    locationLabel = tkinter.Label(text="Место: ", fg="#eee", bg="#333")
    locationLabel.grid(column=0, row=5, pady=10, padx=10, sticky=(tkinter.N))
    typeLabel = tkinter.Label(text="Тип: ", fg="#eee", bg="#333")
    typeLabel.grid(column=0, row=6, pady=10, padx=10, sticky=(tkinter.N))
    idLabel = tkinter.Label(text="Id: ", fg="#eee", bg="#333")
    idLabel.grid(column=0, row=7, pady=10, padx=10, sticky=(tkinter.N))
    hallLabel = tkinter.Label(text="Зал: ", fg="#eee", bg="#333")
    hallLabel.grid(column=0, row=8, pady=10, padx=10, sticky=(tkinter.N))

    name = tkinter.StringVar()
    author = tkinter.StringVar()
    date = tkinter.StringVar()
    location = tkinter.StringVar()
    type = tkinter.StringVar()
    id = tkinter.StringVar()
    hall = tkinter.StringVar()

    name = tkinter.Entry(textvariable=name)
    name.grid(column=1, row=2, pady=10, padx=10, sticky=(tkinter.N))
    author = tkinter.Entry(textvariable=author)
    author.grid(column=1, row=3, pady=10, padx=10, sticky=(tkinter.N))
    date = tkinter.Entry(textvariable=date)
    date.grid(column=1, row=4, pady=10, padx=10, sticky=(tkinter.N))
    location = tkinter.Entry(textvariable=location)
    location.grid(column=1, row=5, pady=10, padx=10, sticky=(tkinter.N))
    type = tkinter.Entry(textvariable=type)
    type.grid(column=1, row=6, pady=10, padx=10, sticky=(tkinter.N))
    id = tkinter.Entry(textvariable=id)
    id.grid(column=1, row=7, pady=10, padx=10, sticky=(tkinter.N))
    hall = tkinter.Entry(textvariable=hall)
    hall.grid(column=1, row=8, pady=10, padx=10, sticky=(tkinter.N))
    print(type(str(hall)))
    addBut = tkinter.Button(text="Добавить", command=add)
    addBut.grid(row=9, column=3)




    root.mainloop()

def DeleteWindow():
    root = tkinter.Tk()
    root.title('Окно удаления')

    def butCallback():
        root.destroy()
        nextWin()

    def delete():
        print(graph.cypher.execute("MATCH (n:Exhibit { id: {input} }) DETACH DELETE n", input=int(delId.get())))

    first_window_user = tkinter.Button(root, text="<", command=butCallback)
    first_window_user.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    delIdLabel = tkinter.Label(text = "Введите id для удаления: ")
    delIdLabel.grid(column = 1, row = 1, pady=10, sticky=(tkinter.N))

    delId = tkinter.StringVar()

    id_entry = tkinter.Entry(textvariable=delId)
    id_entry.grid(row=1, column=2, padx=5, pady=5)

    delBut = tkinter.Button(text="Удалить", command = delete)
    delBut.grid(row=2, column=3)

    root.mainloop()

def StatWindow():
    root = tkinter.Tk()
    root.title('Окно статистики')

    def butCallback():
        root.destroy()
        nextWin()

    first_window_user = tkinter.Button(root, text="<", command=butCallback)
    first_window_user.grid(column=0, row=1, pady=10, sticky=(tkinter.N))

    root.mainloop()

def HallsWindow(*w, **kw):
    root = tkinter.Tk()
    root.title('Залы')

    Hall1 = Image.open("Halls/Портрет.jpg")
    Hall2 = Image.open("Halls/Сказки.jpg")
    Hall3 = Image.open("Halls/Город.jpg")
    Hall4 = Image.open("Halls/Скульптура.jpg")
    Hall5 = Image.open("Halls/Посуда.jpg")
    #
    image1 = ImageTk.PhotoImage(Hall1)
    image2 = ImageTk.PhotoImage(Hall2)
    image3 = ImageTk.PhotoImage(Hall3)
    image4 = ImageTk.PhotoImage(Hall4)
    image5 = ImageTk.PhotoImage(Hall5)

    def next(event, name):
        global hallname
        hallname = name
        root.destroy()
        HallWindow()

    def butCallback():
        root.destroy()
        mainWindow()

    def butCallall():
        root.destroy()
        AllExhibitWindow()

    def butAuthor():
        root.destroy()
        AuthorWindow()

    def butCategory():
        root.destroy()
        CategoryWindow()

    def butLocation():
        root.destroy()
        LocationWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text='Меню')
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text='Выберите зал')
    second_window_label.grid(column=0, row=1, columnspan=3, pady=10, padx=10, sticky=(tkinter.N))
    second_window_author = tkinter.Button(root, text="Автор", command=butAuthor)
    second_window_author.grid(column=4, row=1, pady=10, padx=10, sticky=(tkinter.N))
    second_window_category = tkinter.Button(root, text="Категория", command=butCategory)
    second_window_category.grid(column=5, row=1, pady=10, padx=10, sticky=(tkinter.N))
    second_window_key = tkinter.Button(root, text="Территория", command=butLocation)
    second_window_key.grid(column=6, row=1, pady=10, padx=10, sticky=(tkinter.N))

    c = tkinter.Canvas(root, width=700, height=350, bg='white')
    c.grid(row=2, column=0, columnspan=10)
    l1 = tkinter.Label(c, image=image1)
    l1.place(x=0, y=0)
    l1.bind('<Button-1>', lambda event: next(event, "Портрет"))
    l2 = tkinter.Label(c, image=image2)
    l2.place(x=175, y=0)
    l2.bind('<Button-1>', lambda event: next(event, "Сказки"))
    l3 = tkinter.Label(c, image=image3)
    l3.place(x=350, y=0)
    l3.bind('<Button-1>', lambda event: next(event, "Город"))
    l4 = tkinter.Label(c, image=image4)
    l4.place(x=0, y=190)
    l4.bind('<Button-1>', lambda event: next(event, "Скульптура"))
    l5 = tkinter.Label(c, image=image5)
    l5.place(x=175, y=190)
    l5.bind('<Button-1>', lambda event: next(event, "Посуда"))
    # l6 = tkinter.Label(c, image=image6)
    # l6.place(x=175,y=175)
    # l6.bind('<Button-1>', lambda event: ok(event, "Натюрморт"))
    count = 1
    x = 0
    y = 0
    r = graph.cypher.execute("MATCH (n:Hall) RETURN n.name")
    for i in range(len(r)):
        if (count % 3 == 1):
            x = 0
            l1 = tkinter.Label(c, text=r[i][0])
            l1.place(x=x, y=y + 150)
            count += 1
        elif (count % 3 == 2):
            x += 175
            l1 = tkinter.Label(c, text=r[i][0])
            l1.place(x=x, y=y + 150)
            count += 1
        elif (count % 3 == 0):
            x += 175
            l1 = tkinter.Label(c, text=r[i][0])
            l1.place(x=x, y=y + 150)
            y += 175
            count += 1
        #print(r[i][0])

    second_window_all = tkinter.Button(root, text="Все", command=butCallall)
    second_window_all.grid(column=9, row=3, pady=10, padx=10, sticky=(tkinter.N))

    root.mainloop()

def HallWindow(*w, **kw):
    root = tkinter.Tk()
    root.title(hallname)

    r = graph.cypher.execute("MATCH (a:Hall {name: {name}})-->(b) RETURN b", name=hallname)

    def next(event,but):
        print(but['text'])
        global ex
        ex = but['text']
        root.destroy()
        ExhibitWindow()

    def butCallback():
        root.destroy()
        HallsWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text=hallname)
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    buttons = []
    buttons.clear()
    count=1
    row=0
    col=2
    for i in range(len(r)):
        if (count%3==1):
            col=2
            button = tkinter.Button(root, text=r[i][0]["name"])
            button.bind('<Button-1>', lambda event, but=button: next(event, but))
            button.grid(column=col, row=row+1, pady=10, padx=10, sticky=(tkinter.N))
            buttons.append(button)
            count+=1
        elif (count%3==2):
            col+=1
            button = tkinter.Button(root, text=r[i][0]["name"])
            button.bind('<Button-1>', lambda event, but=button: next(event, but))
            button.grid(column=col, row=row+1, pady=10, padx=10, sticky=(tkinter.N))
            buttons.append(button)
            count += 1
        elif (count%3==0):
            col+=1
            button = tkinter.Button(root, text=r[i][0]["name"])
            button.bind('<Button-1>', lambda event, but=button: next(event, but))
            button.grid(column=col, row=row+1, pady=10, padx=10, sticky=(tkinter.N))
            buttons.append(button)
            row+=1
            count += 1
    #for i in range(len(buttons)):
    #    buttons[i].bind('<Button-1>', lambda event, but=buttons[i]: next(event, but))

    root.mainloop()

def ExhibitWindow(*w, **kw):
    root = tkinter.Tk()
    root.title(ex)

    r = graph.cypher.execute("MATCH (a:Exhibit {name:{name}}) RETURN a", name=ex)

    def butCallback():
        root.destroy()
        HallWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text=ex, font="Arial 14")
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))

    nameLabel = tkinter.Label(text = "Название: ", fg="#eee", bg="#333")
    nameLabel.grid(column=0, row=1, pady=10, padx=10, sticky=(tkinter.N))
    authorLabel = tkinter.Label(text = "Автор: ", fg="#eee", bg="#333")
    authorLabel.grid(column=0, row=2, pady=10, padx=10, sticky=(tkinter.N))
    dateLabel = tkinter.Label(text = "Дата: ", fg="#eee", bg="#333")
    dateLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))
    locationLabel = tkinter.Label(text = "Место: ", fg="#eee", bg="#333")
    locationLabel.grid(column=0, row=4, pady=10, padx=10, sticky=(tkinter.N))
    typeLabel = tkinter.Label(text = "Тип: ", fg="#eee", bg="#333")
    typeLabel.grid(column=0, row=5, pady=10, padx=10, sticky=(tkinter.N))

    name = tkinter.Label(text = r[0][0]["name"])
    name.grid(column=1, row=1, pady=10, padx=10, sticky=(tkinter.N))
    author = tkinter.Label(text = r[0][0]["author"])
    author.grid(column=1, row=2, pady=10, padx=10, sticky=(tkinter.N))
    date = tkinter.Label(text = r[0][0]["date"])
    date.grid(column=1, row=3, pady=10, padx=10, sticky=(tkinter.N))
    location = tkinter.Label(text = r[0][0]["location"])
    location.grid(column=1, row=4, pady=10, padx=10, sticky=(tkinter.N))
    type = tkinter.Label(text = r[0][0]["type"])
    type.grid(column=1, row=5, pady=10, padx=10, sticky=(tkinter.N))

    root.mainloop()

def AllExhibitWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Все экспонаты")

    r = graph.cypher.execute("MATCH (n:Exhibit) RETURN n")

    def butCallback():
        root.destroy()
        HallsWindow()

    def next(event,but):
        print(but['text'])
        global ex
        ex = but['text']
        root.destroy()
        OneExhibitWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    #second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Все экспонаты", font="Arial 14")
    #second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
        button = tkinter.Button(frame, text=r[i][0]["name"])
        button.bind('<Button-1>', lambda event, but=button: next(event, but))
        button.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')

    root.mainloop()

def OneExhibitWindow(*w, **kw):
    root = tkinter.Tk()
    root.title(ex)

    r = graph.cypher.execute("MATCH (a:Exhibit {name:{name}}) RETURN a", name=ex)

    def butCallback():
        root.destroy()
        AllExhibitWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text=ex, font="Arial 14")
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))

    nameLabel = tkinter.Label(text = "Название: ", fg="#eee", bg="#333")
    nameLabel.grid(column=0, row=1, pady=10, padx=10, sticky=(tkinter.N))
    authorLabel = tkinter.Label(text = "Автор: ", fg="#eee", bg="#333")
    authorLabel.grid(column=0, row=2, pady=10, padx=10, sticky=(tkinter.N))
    dateLabel = tkinter.Label(text = "Дата: ", fg="#eee", bg="#333")
    dateLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))
    locationLabel = tkinter.Label(text = "Место: ", fg="#eee", bg="#333")
    locationLabel.grid(column=0, row=4, pady=10, padx=10, sticky=(tkinter.N))
    typeLabel = tkinter.Label(text = "Тип: ", fg="#eee", bg="#333")
    typeLabel.grid(column=0, row=5, pady=10, padx=10, sticky=(tkinter.N))

    name = tkinter.Label(text = r[0][0]["name"])
    name.grid(column=1, row=1, pady=10, padx=10, sticky=(tkinter.N))
    author = tkinter.Label(text = r[0][0]["author"])
    author.grid(column=1, row=2, pady=10, padx=10, sticky=(tkinter.N))
    date = tkinter.Label(text = r[0][0]["date"])
    date.grid(column=1, row=3, pady=10, padx=10, sticky=(tkinter.N))
    location = tkinter.Label(text = r[0][0]["location"])
    location.grid(column=1, row=4, pady=10, padx=10, sticky=(tkinter.N))
    type = tkinter.Label(text = r[0][0]["type"])
    type.grid(column=1, row=5, pady=10, padx=10, sticky=(tkinter.N))

    root.mainloop()

def AuthorWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Авторы")

    r = graph.cypher.execute("MATCH (a:Exhibit) RETURN DISTINCT a.author")

    def butCallback():
        root.destroy()
        HallsWindow()

    def next(event,but):
        #print(but['text'])
        global glauthor
        glauthor = but['text']
        root.destroy()
        ExhibitAuthorWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    # second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Все авторы", font="Arial 14")
    # second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
        but = tkinter.Button(frame, text=r[i][0])
        #print(r[i][0])
        but.bind('<Button-1>', lambda event, but=but: next(event, but))
        but.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')

    root.mainloop()

def ExhibitAuthorWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Экспонаты автора")

    r = graph.cypher.execute("MATCH (a:Exhibit {author: {ChosenAuthor}}) RETURN a", ChosenAuthor = glauthor)

    def butCallback():
        root.destroy()
        AuthorWindow()

    def next(event, but):
        print(but['text'])
        global ex
        ex = but['text']
        root.destroy()
        OneExhibitAuthorWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    # second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Экспонаты", font="Arial 14")
    # second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
       but = tkinter.Button(frame, text=r[i][0]["name"])
       but.bind('<Button-1>', lambda event, but=but: next(event, but))
       but.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')
    root.mainloop()

def OneExhibitAuthorWindow():
    root = tkinter.Tk()
    root.title(ex)

    r = graph.cypher.execute("MATCH (a:Exhibit {name:{name}}) RETURN a", name=ex)

    def butCallback():
        root.destroy()
        ExhibitAuthorWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text=ex, font="Arial 14")
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))

    nameLabel = tkinter.Label(text="Название: ", fg="#eee", bg="#333")
    nameLabel.grid(column=0, row=1, pady=10, padx=10, sticky=(tkinter.N))
    authorLabel = tkinter.Label(text="Автор: ", fg="#eee", bg="#333")
    authorLabel.grid(column=0, row=2, pady=10, padx=10, sticky=(tkinter.N))
    dateLabel = tkinter.Label(text="Дата: ", fg="#eee", bg="#333")
    dateLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))
    locationLabel = tkinter.Label(text="Место: ", fg="#eee", bg="#333")
    locationLabel.grid(column=0, row=4, pady=10, padx=10, sticky=(tkinter.N))
    typeLabel = tkinter.Label(text="Тип: ", fg="#eee", bg="#333")
    typeLabel.grid(column=0, row=5, pady=10, padx=10, sticky=(tkinter.N))

    name = tkinter.Label(text=r[0][0]["name"])
    name.grid(column=1, row=1, pady=10, padx=10, sticky=(tkinter.N))
    author = tkinter.Label(text=r[0][0]["author"])
    author.grid(column=1, row=2, pady=10, padx=10, sticky=(tkinter.N))
    date = tkinter.Label(text=r[0][0]["date"])
    date.grid(column=1, row=3, pady=10, padx=10, sticky=(tkinter.N))
    location = tkinter.Label(text=r[0][0]["location"])
    location.grid(column=1, row=4, pady=10, padx=10, sticky=(tkinter.N))
    type = tkinter.Label(text=r[0][0]["type"])
    type.grid(column=1, row=5, pady=10, padx=10, sticky=(tkinter.N))

    root.mainloop()

def CategoryWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Категории")

    r = graph.cypher.execute("MATCH (a:Exhibit) RETURN DISTINCT a.type")

    def butCallback():
        root.destroy()
        HallsWindow()

    def next(event, but):
        #print(but['text'])
        global glcat
        glcat = but['text']
        root.destroy()
        ExhibitCatWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    # second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Все категории", font="Arial 14")
    # second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
        but = tkinter.Button(frame, text=r[i][0])
        but.bind('<Button-1>', lambda event, but=but: next(event, but))
        but.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')

    root.mainloop()


def ExhibitCatWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Экспонаты категории")

    r = graph.cypher.execute("MATCH (a:Exhibit {type: {ChosenType}}) RETURN a", ChosenType=glcat)

    def butCallback():
        root.destroy()
        CategoryWindow()

    def next(event, but):
        print(but['text'])
        global ex
        ex = but['text']
        root.destroy()
        OneExhibitCatWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    # second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Экспонаты", font="Arial 14")
    # second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
        print(r[i][0])
        but = tkinter.Button(frame, text=r[i][0]["name"])
        but.bind('<Button-1>', lambda event, but=but: next(event, but))
        but.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')
    root.mainloop()


def OneExhibitCatWindow():
    root = tkinter.Tk()
    root.title(ex)

    r = graph.cypher.execute("MATCH (a:Exhibit {name:{name}}) RETURN a", name=ex)

    def butCallback():
        root.destroy()
        ExhibitCatWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text=ex, font="Arial 14")
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))

    nameLabel = tkinter.Label(text="Название: ", fg="#eee", bg="#333")
    nameLabel.grid(column=0, row=1, pady=10, padx=10, sticky=(tkinter.N))
    authorLabel = tkinter.Label(text="Автор: ", fg="#eee", bg="#333")
    authorLabel.grid(column=0, row=2, pady=10, padx=10, sticky=(tkinter.N))
    dateLabel = tkinter.Label(text="Дата: ", fg="#eee", bg="#333")
    dateLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))
    locationLabel = tkinter.Label(text="Место: ", fg="#eee", bg="#333")
    locationLabel.grid(column=0, row=4, pady=10, padx=10, sticky=(tkinter.N))
    typeLabel = tkinter.Label(text="Тип: ", fg="#eee", bg="#333")
    typeLabel.grid(column=0, row=5, pady=10, padx=10, sticky=(tkinter.N))

    name = tkinter.Label(text=r[0][0]["name"])
    name.grid(column=1, row=1, pady=10, padx=10, sticky=(tkinter.N))
    author = tkinter.Label(text=r[0][0]["author"])
    author.grid(column=1, row=2, pady=10, padx=10, sticky=(tkinter.N))
    date = tkinter.Label(text=r[0][0]["date"])
    date.grid(column=1, row=3, pady=10, padx=10, sticky=(tkinter.N))
    location = tkinter.Label(text=r[0][0]["location"])
    location.grid(column=1, row=4, pady=10, padx=10, sticky=(tkinter.N))
    type = tkinter.Label(text=r[0][0]["type"])
    type.grid(column=1, row=5, pady=10, padx=10, sticky=(tkinter.N))

    root.mainloop()

def LocationWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Территория")

    r = graph.cypher.execute("MATCH (a:Exhibit) RETURN DISTINCT a.location")

    def butCallback():
        root.destroy()
        HallsWindow()

    def next(event, but):
        # print(but['text'])
        global glloc
        glloc = but['text']
        root.destroy()
        ExhibitLocWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    # second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Все государства", font="Arial 14")
    # second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)

    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
        but = tkinter.Button(frame, text=r[i][0])
        but.bind('<Button-1>', lambda event, but=but: next(event, but))
        but.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')

    root.mainloop()


def ExhibitLocWindow(*w, **kw):
    root = tkinter.Tk()
    root.title("Экспонаты по территории")

    r = graph.cypher.execute("MATCH (a:Exhibit {location: {ChosenLocation}}) RETURN a", ChosenLocation=glloc)

    def butCallback():
        root.destroy()
        LocationWindow()

    def next(event, but):
        global ex
        ex = but['text']
        root.destroy()
        OneExhibitLocWindow()

    canv = tkinter.Canvas(root)
    second_window_back_button = tkinter.Button(canv, text="<", command=butCallback)
    # second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_back_button.pack(side=tkinter.LEFT)
    second_window_label = tkinter.Label(canv, text="Экспонаты", font="Arial 14")
    # second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))
    second_window_label.pack(side=tkinter.LEFT)

    canvas = tkinter.Canvas(root)
    scroll_y = tkinter.Scrollbar(root, orient="vertical", command=canvas.yview)
    frame = tkinter.Frame(canvas)
    for i in range(len(r)):
        but = tkinter.Button(frame, text=r[i][0]["name"])
        but.bind('<Button-1>', lambda event, but=but: next(event, but))
        but.pack()
    canvas.create_window(0, 0, anchor='nw', window=frame)
    canvas.update_idletasks()

    canvas.configure(scrollregion=canvas.bbox('all'),
                     yscrollcommand=scroll_y.set)

    canv.pack()
    canvas.pack(fill='both', expand=True, side=tkinter.LEFT)
    scroll_y.pack(fill='y', side='right')
    root.mainloop()


def OneExhibitLocWindow():
    root = tkinter.Tk()
    root.title(ex)

    r = graph.cypher.execute("MATCH (a:Exhibit {name:{name}}) RETURN a", name=ex)

    def butCallback():
        root.destroy()
        ExhibitLocWindow()

    second_window_back_button = tkinter.Button(root, text="<", command=butCallback)
    second_window_back_button.grid(column=0, row=0, pady=10, sticky=(tkinter.N))
    second_window_label = tkinter.Label(root, text=ex, font="Arial 14")
    second_window_label.grid(column=1, row=0, pady=10, padx=10, sticky=(tkinter.N))

    nameLabel = tkinter.Label(text="Название: ", fg="#eee", bg="#333")
    nameLabel.grid(column=0, row=1, pady=10, padx=10, sticky=(tkinter.N))
    authorLabel = tkinter.Label(text="Автор: ", fg="#eee", bg="#333")
    authorLabel.grid(column=0, row=2, pady=10, padx=10, sticky=(tkinter.N))
    dateLabel = tkinter.Label(text="Дата: ", fg="#eee", bg="#333")
    dateLabel.grid(column=0, row=3, pady=10, padx=10, sticky=(tkinter.N))
    locationLabel = tkinter.Label(text="Место: ", fg="#eee", bg="#333")
    locationLabel.grid(column=0, row=4, pady=10, padx=10, sticky=(tkinter.N))
    typeLabel = tkinter.Label(text="Тип: ", fg="#eee", bg="#333")
    typeLabel.grid(column=0, row=5, pady=10, padx=10, sticky=(tkinter.N))

    name = tkinter.Label(text=r[0][0]["name"])
    name.grid(column=1, row=1, pady=10, padx=10, sticky=(tkinter.N))
    author = tkinter.Label(text=r[0][0]["author"])
    author.grid(column=1, row=2, pady=10, padx=10, sticky=(tkinter.N))
    date = tkinter.Label(text=r[0][0]["date"])
    date.grid(column=1, row=3, pady=10, padx=10, sticky=(tkinter.N))
    location = tkinter.Label(text=r[0][0]["location"])
    location.grid(column=1, row=4, pady=10, padx=10, sticky=(tkinter.N))
    type = tkinter.Label(text=r[0][0]["type"])
    type.grid(column=1, row=5, pady=10, padx=10, sticky=(tkinter.N))

    root.mainloop()

if __name__ == '__main__':
    mainWindow()