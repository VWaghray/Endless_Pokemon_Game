from PIL import ImageTk
import PIL.Image
import random
from tkinter import *

root = Tk()
root.title("Endless Pokemon Game")
root.geometry("600x400")
root.configure(bg = "#4B0082")

Pic = ImageTk.PhotoImage(PIL.Image.open("button.jpg"))
Abra = ImageTk.PhotoImage(PIL.Image.open("abra.jpg"))
Bulbasour = ImageTk.PhotoImage(PIL.Image.open("bulbasour.jpg"))
Button = ImageTk.PhotoImage(PIL.Image.open("button.jpg"))
Charmender = ImageTk.PhotoImage(PIL.Image.open("charmender.jpg"))
Iyvasour = ImageTk.PhotoImage(PIL.Image.open("Iyvasour.jpg"))
Jigglypuff = ImageTk.PhotoImage(PIL.Image.open("jigglypuff.jpg"))
Kadabra = ImageTk.PhotoImage(PIL.Image.open("Kadabra.jpg"))
Meowth = ImageTk.PhotoImage(PIL.Image.open("meowth.jpg"))
Nidoking = ImageTk.PhotoImage(PIL.Image.open("nidoking.jpg"))
Paras = ImageTk.PhotoImage(PIL.Image.open("paras.jpg"))
Persion = ImageTk.PhotoImage(PIL.Image.open("persion.jpg"))
Pikachu = ImageTk.PhotoImage(PIL.Image.open("pikachu.jpg"))
Ratata = ImageTk.PhotoImage(PIL.Image.open("ratata.jpg"))
Squirtle = ImageTk.PhotoImage(PIL.Image.open("squirtle.jpg"))

pokemon_names = [Abra,Bulbasour,Charmender,Iyvasour,Jigglypuff,Kadabra,Meowth,Nidoking,Paras,Persion,Pikachu,Ratata,Squirtle]
power_list = [30,60,50,100,70,70,60,90,40,70,200,40,50]

p1=Label(root, text="Player 1", bg="#4B0082", fg="#FFFFFF", font = ("Comic Sans MS",13,"bold"))
p1.place(relx=0.1, rely=0.3, anchor=CENTER)
p2=Label(root, text="Player 2", bg="#4B0082", fg="#FFFFFF", font = ("Comic Sans MS",13,"bold"))
p2.place(relx=0.9, rely=0.3, anchor=CENTER)

p1_score=Label(root, bg="#4B0082", fg="#FFFFFF", font = ("Comic Sans MS",13,"bold"))
p1_score.place(relx=0.1, rely=0.4, anchor=CENTER)
p2_score=Label(root, bg="#4B0082", fg="#FFFFFF", font = ("Comic Sans MS",13,"bold"))
p2_score.place(relx=0.9, rely=0.4, anchor=CENTER)



random_label=Label(root, bg="#4B0082", fg="#FFFFFF", font = ("Georgia",15,"bold"))
random_label.place(relx=0.5, rely=0.5, anchor=CENTER)

p1score = 0

def Player1():
    global p1score
    r1 = random.randint(0,12)
    random_pokemon=pokemon_names[r1]
    random_label["image"] = random_pokemon
    random_power=power_list[r1]
    p1score = p1score + random_power
    p1_score["text"] = str(p1score)
    
p2score = 0

def Player2():
    global p2score
    r2 = random.randint(0,12)
    random_pokemon2=pokemon_names[r2]
    random_label["image"] = random_pokemon2
    random_power2=power_list[r2]
    p2score = p2score + random_power2
    p2_score["text"] = str(p2score)
    
btn1 = Button(root, image = Pic, command = Player1)
btn1.place(relx = 0.1, rely = 0.6, anchor=CENTER)
btn2 = Button(root, image = Pic, command = Player2)
btn2.place(relx = 0.9, rely = 0.6, anchor=CENTER)

root.mainloop()