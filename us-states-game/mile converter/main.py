from tkinter import *

window = Tk()
window.title("yes!")
window.minsize(width=500, height=300)


miles = Label(text="Miles", font=("Arial", 24, "bold"))
miles.grid(column=3, row=1)

entry = Entry(width=10)
entry.grid(column=2,row=1)

km = Label(text="km",font=("Arial", 24, "bold"))
km.grid(column=3, row=2)

is_eg = Label(text="is equal to", font=("Arial", 24, "bold"))
is_eg.grid(column=1, row=2)

results = Label(text="0",font=("Arial", 24, "bold") )
results.grid(column=2, row=2)



def function_button():
    miles_value = entry.get()
    result = float(miles_value) * 1.6
    results.config(text=f"{result}") 

button = Button(text="calculate", command=function_button)
button.grid(column=2, row=3)


window.mainloop()



