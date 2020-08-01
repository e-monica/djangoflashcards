from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.title("Hello World!")
root.geometry("400x400")
root.iconbitmap('c:/guis/brain.ico')

#Create clicked function
def clicked():
	global my_label
	input = e.get()
	my_label = Label(root, text="Hello " + input)
	my_label.pack()

#Hide Function
def hide():
	my_label.pack_forget()

#Show Function
def show():
	my_label.pack()


img = ImageTk.PhotoImage(Image.open("brain.ico"), size = 8)
img_label = Label(image=img)
img_label.pack()

#Label learning notes:
#state may be disabled, normal groove for different button effects upon click
#height may be width for possible grids, not applicable here
#pack and grid may be used together but not necessary here
#pady in pack may center or push text down towards center

my_label = Label(root, text="Enter your name:")
my_label.pack()


def hide():
	my_label.pack_forget()

def show():
	my_label.pack()

#fg="white", bg="black", font=("Helvetica", 32), 
#row=0, column=0, rowspan=2

#my_label2 = Label(root, text="Second thing!!", relief="raised")
#my_label2.grid(row=0, column=1, sticky=W)

#my_label3 = Label(root, text="Third thing!!")
#my_label3.grid(row=2, column=1)

e = Entry(root, font=("Helvetica", 18))
e.pack(pady=20)

my_button = Button(root, text="Click Me!", relief="raised", command=clicked)
my_button.pack(pady=20)

hide_button = Button(root, text="Hide", relief="raised", command=hide)
hide_button.pack(pady=20)

show_button = Button(root, text="Show", relief="raised", command=show)
show_button.pack(pady=20)


root.mainloop()
