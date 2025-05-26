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

        self.to_do_items = [
            ToDoItem("Buy groceries", "Milk, Bread, Eggs"),
            ToDoItem("Clean the house", "Living room, Kitchen, Bathroom"),
            ToDoItem("Finish project", "Due next week"),
            ToDoItem("Call mom", "Check in on her"),
            ToDoItem("Walk the dog", "30 minutes in the park")
        ]

        self.label_text = StringVar()
        label = Label(frame, text="Some label text", textvariable=self.label_text)
        label.pack()


        label.configure(font=("Courier", 44), text="New label text")

        self.entry_text = StringVar()
        entry = Entry(frame, textvariable=self.entry_text)
        entry.pack()


        button = Button(frame, text="Button text", command=self.press_button)
        button.pack()

        self.list_item_strings = ["Hey", "Hi", "Hello", "Howdy", "Greetings"]
        list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(frame, listvariable=list_items)
        listbox["height"] = 3
        listbox.bind("<<ListboxSelect>>", lambda s: self.select_item(listbox.curselection()))
        listbox.pack()
        #can also just past the first item of the tuple
        #listbox.bind("<<ListboxSelect>>", lambda event: self.select_item(listbox.curselection()[0]))

    def press_button(self):
        #print("Button pressed!")
        self.label_text.set(self.entry_text.get())

    def select_item(self, index):
        #print("Item selected:", index)
        #if you only pass the first item of the tuple it needs to change to:
        #selected_item = self.list_item_strings[index]
        selected_item = self.list_item_strings[index[0]]
        print("Item selected:", selected_item)


root = Tk()
ToDoListApp(root)
root.mainloop()