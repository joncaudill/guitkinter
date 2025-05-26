from tkinter import * 
import tkinter as tk

class ToDoItem:
    def __init__(self, name, description):
        self.name = name
        self.description = description

class ToDoListApp:
    def __init__(self, root):
        root.title("To Do List")

        frame = Frame(root, borderwidth=2, relief="sunken")
        frame.grid(column=1, row=1, sticky=(N, S, E, W))
        #weight 1 means that the frame will expand to fill the available space
        root.columnconfigure(1, weight=1)
        root.rowconfigure(1, weight=1)

        list_label = Label(frame, text="All Items")
        list_label.grid(column=1, row=1, sticky=(S, W))

        self.to_do_items = [
            ToDoItem("Buy groceries", "Milk, Bread, Eggs"),
            ToDoItem("Clean the house", "Living room, Kitchen, Bathroom"),
            ToDoItem("Finish project", "Due next week"),
            ToDoItem("Call mom", "Check in on her"),
            ToDoItem("Walk the dog", "30 minutes in the park")
        ]

        self.to_do_names = StringVar(value=list(map(lambda item: item.name, self.to_do_items)))

        items_list = Listbox(frame, listvariable=self.to_do_names)
        items_list.bind("<<ListboxSelect>>", lambda s: self.select_item(items_list.curselection()))
        items_list.grid(column=1, row=2, sticky=(W, E), rowspan=5)
        #can also just past the first item of the tuple
        #listbox.bind("<<ListboxSelect>>", lambda event: self.select_item(items_list.curselection()[0]))

        self.selected_description = StringVar()
        selected_description_label = Label(frame, textvariable=self.selected_description, 
                                           wraplength=200)
        selected_description_label.grid(column=1, row=7, sticky=(W, E))

        to_do_label = Label(frame, text="New Item")
        to_do_label.grid(column=2, row=1, sticky=(S, W))

        name_label = Label(frame, text="Item name", font='TkHeadingFont')
        name_label.grid(column=2, row=2, sticky=(S, W))

        self.name = StringVar()
        name_entry = Entry(frame, textvariable=self.name)
        name_entry.grid(column=2, row=3, sticky=(W, N, E))

        description_label = Label(frame, text="Item description", font='TkHeadingFont')
        description_label.grid(column=2, row=4, sticky=(S, W))

        self.description = StringVar()
        description_entry = Entry(frame, textvariable=self.description)
        description_entry.grid(column=2, row=5, sticky=(W, N, E))

        save = tk.Button(frame, text="Save", command=self.save_item)
        save.grid(column=2, row=6, sticky=E)

    def save_item(self):
        new_item = ToDoItem(self.name.get(), self.description.get())
        self.to_do_items.append(new_item)
        self.to_do_names.set(list(map(lambda item: item.name, self.to_do_items)))
        self.name.set("")
        self.description.set("")
        print("Item saved:", new_item.name, "-", new_item.description)


    def select_item(self, index):
        #if you only pass the first item of the tuple it needs to change to:
        #selected_item = self.to_do_items[index]
        selected_item = self.to_do_items[index[0]]
        self.selected_description.set(selected_item.description)
        print("Item selected:")

root = Tk()
ToDoListApp(root)
root.mainloop()