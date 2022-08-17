from PIL import Image, ImageTk

from tkinter import *

root = Tk()
root.title("Endless Dice Game")
root.geometry("600x400")
root.configure(bg = "#4B0082")

p1=Label(root, text="Player 1", bg="#4B0082", fg="#FFFFFF")
p1.place(relx=0.1, rely=0.3, anchor=CENTER)
p2=Label(root, text="Player 2", bg="#4B0082", fg="#FFFFFF")
p2.place(relx=0.9, rely=0.3, anchor=CENTER)

p1_score=Label(root, bg="#4B0082", fg="#FFFFFF")
p1_score.place(relx=0.1, rely=0.4, anchor=CENTER)
p2_score=Label(root, bg="#4B0082", fg="#FFFFFF")
p2_score.place(relx=0.9, rely=0.4, anchor=CENTER)



random_label=Label(root, bg="#4B0082", fg="#FFFFFF")
random_label.place(relx=0.5, rely=0.5, anchor=CENTER)

root.mainloop()