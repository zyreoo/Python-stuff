import tkinter

window = tkinter.Tk()
window.title("My first gui program!")
window.minsize(width=500, height=300)


my_label = tkinter.Label(text="i m a label", font=("Arial", 24, "bold"))
my_label.pack()


def function (*args):
    
    print(sum(args))


function(1,2,2,2,2,2,2,2,2,2)


input_  = tkinter.Entry(width=10)
input_.pack()


def function_label():
    david = input_.get()

    my_label.config(text=david)


button = tkinter.Button(text="click me", command=function_label)
button.pack()



window.ex