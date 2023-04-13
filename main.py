from tkinter import *
from ranking import Ranking
from words_area import WordsArea

# ---------------------------- CONSTANTS ------------------------------- #
YELLOW = "#f7f5dd"
GREEN = '#9bdeac'
L_PURPLE = "#372948"
H_PURPLE = "#251B37"
FONT_NAME = "Courier"
TIMER_SEC = 60


# ---------------------------- TIMER MECHANISM ------------------------------- #

# START BUTTON CLICKED
def start_timer():
    count_down(TIMER_SEC)
    words_area.words_reset(words, text)
    text.delete('1.0', 'end')


# RESET BUTTON CLICKED
def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="1min")
    words_area.words_reset(words, text)
    text.delete('1.0', 'end')
    text.insert('1.0', "Click start button and type here the words you can see above.")


# UPDATING WORDS FIELD
def config_words_area():
    words['state'] = 'normal'
    words.delete('1.0', '1.1')
    words['state'] = 'disabled'
    words.update()


# COUNTDOWN MECHANISM
def count_down(count):
    count_sec = count
    text_content = text.get('1.0', 'end')
    if " " in text_content:
        typed_words = text_content.split(" ")
        if len(typed_words) > 2:
            config_words_area()

    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_sec}sec")

    if count > 0:
        timer = window.after(1000, count_down, count - 1)

    if count == 0:
        text_content = text.get('1.0', 'end')
        typed_words = ("").join(text_content)
        typed_words_list = typed_words.split()

        correct_list = [_ for _ in typed_words_list if _ in words_area.random_string_words]
        WPM = len(correct_list)
        CPM = sum(len(i) for i in correct_list)
        canvas.itemconfig(timer_text, text="0sec")

        # Ranking
        ranking = Ranking(CPM, WPM, words)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Typing Speed Test")
window.config(pady=50, padx=100, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
timer_text = canvas.create_text(100, 130, text="1min", fill=H_PURPLE, font=(FONT_NAME, 20, "bold"))
canvas.grid(row=1, column=2)

# Text

text = Text(window, width=50, height=5, fg="grey", font=(FONT_NAME, 16))
text.insert('1.0', "Click the start button and type here the words you will see above.")
text.grid(row=2, column=0)

words = Text(window, width=50, height=5, fg=H_PURPLE, bg=GREEN, font=(FONT_NAME, 16))
words.grid(row=1, column=0)
words_area = WordsArea(words)

# Labels

label_timer = Label(text="Typing Speed Test", fg=L_PURPLE, bg=YELLOW, font=(FONT_NAME, 40, "bold"))
label_timer.grid(row=0, column=0, columnspan=2)

label_CMP = Label(text="CMP - Correct Characters Per Minute", fg=L_PURPLE, bg=YELLOW, font=(FONT_NAME, 14))
label_CMP.grid(row=3, column=0, columnspan=2)
label_WPM = Label(text="WMP - Correct Words Per Minute", fg=L_PURPLE, bg=YELLOW, font=(FONT_NAME, 14))
label_WPM.grid(row=4, column=0, columnspan=2)

# Button

start_image = PhotoImage(file="play.png")
button_start = Button(image=start_image, highlightthickness=0, bg=YELLOW, command=start_timer)
button_start.grid(row=2, column=2)

restart_image = PhotoImage(file="restart.png")
button_reset = Button(image=restart_image, highlightthickness=0, bg=YELLOW, command=reset_timer)
button_reset.grid(row=2, column=3)

# Window mainloop

window.mainloop()
