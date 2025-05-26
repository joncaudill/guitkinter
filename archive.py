from tkinter import * 
import tkinter as tk

class MyApp:
    def __init__(self, root):
        root.title("My app")
        root.geometry("500x400")
        root.maxsize(1000, 800)

        frame = Frame(root, width=200, height=100, borderwidth=2, relief="sunken")
        frame.place(x=0, y=0)

        self.label_text = StringVar()
        label = Label(root, textvariable=self.label_text, font=("Arial", 24))
        #self.label_text.set("Hello, World!")
        #label.pack(side=LEFT, padx=10, pady=5)
        #label.grid(column=1, row=1)
        '''label2 = Label(root, text="This is a simple Tkinter app.", 
                       font=("Arial", 16), bg="lightblue")
        label2.pack(side=LEFT)'''

        #label["text"] = "New label text"
        #label["bg"] = "red"

        label.configure(text="New label text", bg="red")

        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        #entry.pack(side=LEFT)
        #entry.place(x=100, y=50)
        #entry.grid(column=3, row=1)
        #entry_text.set("Default text")
        #entry_text.get()

        #label["textvariable"] = entry_text

        button = Button(root, text="Click me!", command=self.press_button )
        #button.pack(side=LEFT)
        #button.grid(column=1, row=2, sticky=(S,E,W))
        #button.place(x=0, y=0)
        #button.configure(width=10, height=2, font=("Courier", 40))

        self.list_item_strings = ["Item 1", "Item 2", "Item 3"]
        self.list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(root, listvariable=self.list_items)
        listbox["height"] = 3
        #listbox.pack(side=tk.LEFT, padx=40, pady=20)
        #listbox.grid(column=2, row=2)
        listbox.bind("<<ListboxSelect>>", lambda event: self.select_item(listbox.curselection()))
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
MyApp(root)
root.mainloop()