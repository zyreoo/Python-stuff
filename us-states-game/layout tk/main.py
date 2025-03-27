import tkinter


window = tkinter.Tk()
window.title("My first gui program")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="i am  a label ")
my_label.config(text="new text")

my_label.grid(column=1, row=1)

button = tkinter.Button(text="click me")

button.grid(column=2, row= 2)

input = tkinter.Entry(width=10)
input.grid(column=4, row=3)

new_button = tkinter.Button(text="new text")
new_button.grid(column=3, row=1)




window.mainloop()