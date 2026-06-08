from tkinter import *
import pandas 
import random
BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}

try:
    data = pandas.read_csv("/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/words_to_learn.csv")
except FileNotFoundError:   
    original_data = pandas.read_csv("/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/igbo_word.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")





  
def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = random.choice(to_learn)
    canvas.itemconfig(card_title, text="Igbo", fill="black")
    canvas.itemconfig(card_question, text="Gini Bu 🤔", fill="black")
    canvas.itemconfig(card_word, text=current_card["Igbo"], fill="black")
    canvas.itemconfig(card_background, image=card_front_img)
    flip_timer = window.after(3000, func=flip_card)

def is_known():
    to_learn.remove(current_card)
    data = pandas.DataFrame(to_learn)
    data.to_csv("/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/words_to_learn.csv", index=False)
    next_card()

def flip_card():
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_question, text="Answer is... 😎", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")
    canvas.itemconfig(card_background, image=card_back_img)
       




window = Tk()
window.title("Flash Card Project")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)


flip_timer = window.after(3000, func=flip_card)

# -------------------GUI Setup-------------------
canvas = Canvas(width=800, height=526)
card_front_img = PhotoImage(file="/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/images/card_front.png")
card_back_img = PhotoImage(file="/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/images/card_back.png")

card_background = canvas.create_image(400, 263, image=card_front_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(column=0, row=0, columnspan=2)

card_title = canvas.create_text(400, 150, text="", font=("Ariel", 40, "italic"), fill="black")
card_question = canvas.create_text(400, 220, text="Gini Bu 🤔", font=("Ariel", 30, "bold"), fill="black")
card_word = canvas.create_text(400, 280, text="", font=("Ariel", 60, "bold"), fill="black")

cross_image = PhotoImage(file="/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/images/wrong.png")
unknown_button = Button(image=cross_image, highlightthickness=0, command=next_card)
unknown_button.grid(column=0, row=1)

check_image = PhotoImage(file="/Users/victoriamadedor/Desktop/Stan's projects/flash-card-project-start/images/right.png")
known_button = Button(image=check_image, highlightthickness=0, command=is_known)
known_button.grid(column=1, row=1)


next_card()



window.mainloop()
