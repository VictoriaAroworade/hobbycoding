from tkinter import *
from random import choice, randint
from typing import Dict, Any
import pandas

BACKGROUND_COLOR = "#B1DDC6"
current_card = {}
to_learn = {}
WORDS_TO_LEARN_PATH = "data/it_words_to_learn.csv"
ORIGINAL_DATA_PATH = "data/italian_words.csv"
LANGUAGE = "Italian"

# read and format initial csv data

try:
    flash_data = pandas.read_csv(WORDS_TO_LEARN_PATH)
except FileNotFoundError:
    original_data = pandas.read_csv(ORIGINAL_DATA_PATH)
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = flash_data.to_dict(orient="records")


# --------------------------------- CREATE FLASHCARD ------------------------------- #
def create_flashcard():
    global current_card, flip_timer

    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    random_lang = current_card[LANGUAGE]
    canvas.itemconfig(word_text, text=f"{random_lang}", fill="black")
    canvas.itemconfig(language_text, text=LANGUAGE, fill="black")
    canvas.itemconfig(card_image, image=card_front_img)
    flip_timer = window.after(3000, flip)


# --------------------------------- FLIP FLASHCARD ------------------------------- #
def flip():
    random_en = current_card["English"]
    canvas.itemconfig(word_text, text=f"{random_en}", fill="white")
    canvas.itemconfig(language_text, text="English", fill= "white")
    canvas.itemconfig(card_image, image=card_back_img)

# --------------------------------- SAVE YOUR PROGRESS ------------------------------- #
def save_progess():
    to_learn.remove(current_card)
    words_to_learn = pandas.DataFrame(to_learn)
    words_to_learn.to_csv(WORDS_TO_LEARN_PATH, index = False)
    create_flashcard()

# ------------------------------------- UI SETUP ------------------------------------ #

# create window
window = Tk()
window.title("Flashy Swiss Linguistics 🇨🇭🧀🐄")
window.config(padx=50, pady=50, bg = BACKGROUND_COLOR)
flip_timer = window.after(3000, flip)

# create canvas
canvas = Canvas(width=800, height=550, highlightthickness=0, bg=BACKGROUND_COLOR)
card_front_img = PhotoImage(file="images/card_front.png")
card_back_img = PhotoImage(file="images/card_back.png")
card_image = canvas.create_image(400,280, image=card_front_img)
language_text = canvas.create_text(400,150, text="", font=("Arial", 40, "italic"), fill="black")
word_text = canvas.create_text(400,263, text="", font=("Arial", 60, "bold"), fill="black")
canvas.grid(row=0, column=0, columnspan=2)

# create buttons

right_img = PhotoImage(file="images/right.png")
wrong_img = PhotoImage(file="images/wrong.png")

right = Button(image=right_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=save_progess)
right.grid(row=1, column=1)
wrong = Button(image=wrong_img, highlightthickness=0, highlightbackground=BACKGROUND_COLOR, command=create_flashcard)
wrong.grid(row=1, column=0)

create_flashcard()
save_progess()


window.mainloop()
