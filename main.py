BACKGROUND_COLOR = "#B1DDC6"
from tkinter import *
import pandas
import random
import time
try:
    df = pandas.read_csv("data/word_to_learn.csv")
except:
    df = pandas.read_csv("data/french_words.csv")
dic = df.to_dict(orient="records")
text = ""




window = Tk()
def button1():
    global a
    global b
    a=random1(dic)
    b = french(a)
def is_known():
    global dic
    dic.remove(a)
    data=pandas.DataFrame(dic)
    data.to_csv("data/word_to_learn.csv",index=False)
    print(len(dic))
    button1()

window.title("Flashy")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)
my_image3 = PhotoImage(file="images/card_front.png")
my_image4 = PhotoImage(file="images/card_back.png")
canvas = Canvas(width=800, height=526)
my_image5=canvas.create_image(400, 263, image=my_image3)
canvas.grid(row=0, column=0, columnspan=2)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
title=canvas.create_text(400, 150, text="title", font=("Ariel", 40, "italic"))
word=canvas.create_text(400, 263, text="word", font=("Ariel", 60, "bold"))


my_image1 = PhotoImage(file="images/right.png")
button = Button(image=my_image1, highlightthickness=0, command=is_known)
button.grid(row=1, column=0)


my_image2 = PhotoImage(file="images/wrong.png")
button = Button(image=my_image2, highlightthickness=0, command=button1)
button.grid(row=1, column=1)

def random1(dic):
    global canvas
    print("rand")
    global text
    a = random.randint(0,len(dic))
    b = dic[a]
    print(b)
    return b
a= random1(dic)




def timer1():
    print("english")
    global text
    global a
    global word
    b = a["English"]
    text = "English"
    canvas.itemconfig(my_image5,image=my_image4)
    canvas.itemconfig(title,text=text,fill="white")
    canvas.itemconfig(word, text=b,fill="white")


def french(a):
    global canvas,flip_timer
    window.after_cancel(flip_timer)
    canvas.itemconfig(my_image5, image=my_image3)
    print("french")
    global text
    text = "French"
    b=a["French"]
    canvas.itemconfig(title, text=text,fill="black")
    canvas.itemconfig(word, text=b,fill="black")
    flip_timer=window.after(3000,timer1)

flip_timer = window.after(3000,timer1)



window.mainloop()
