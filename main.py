from tkinter import * 
import tkinter as tk

class MyApp:
    def __init__(self, root):
        root.title("My app")
        root.geometry("800x600")
        root.maxsize(1000, 800)

        self.label_text = StringVar()
        label = Label(root, textvariable=self.label_text, font=("Arial", 24))
        self.label_text.set("Hello, World!")
        label.pack(side=TOP)
        label2 = Label(root, text="This is a simple Tkinter app.", 
                       font=("Arial", 16), bg="lightblue")
        label2.pack()

        #label["text"] = "New label text"
        #label["bg"] = "red"

        label.configure(text="New label text", bg="red")

        self.entry_text = StringVar()
        entry = Entry(root, textvariable=self.entry_text)
        entry.pack()


        #entry_text.set("Default text")
        #entry_text.get()

        #label["textvariable"] = entry_text

        button = Button(root, text="Click me!", command=self.press_button )
        button.pack()

        self.list_item_strings = ["Item 1", "Item 2", "Item 3"]
        self.list_items = StringVar(value=self.list_item_strings)
        listbox = Listbox(root, listvariable=self.list_items)
        listbox["height"] = 3
        listbox.pack()
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