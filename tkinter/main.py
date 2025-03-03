# import tkinter 

# window = tkinter.Tk()

from tkinter import *
window = Tk()
window.title("My First GUI with Tkinter")
window.minsize(width=1000, height=800)

my_label = Label(text="My Label", font=("Arial", 24, "bold"))
my_label.pack()

my_button = Button(text="Click Me")
my_button.pack()

window.mainloop()