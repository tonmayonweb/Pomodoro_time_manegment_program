from tkinter import *
import math

# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
rep = 0
timer = None


# ---------------------------- TIMER RESET ------------------------------- #
def Reset():
    window.after_cancel(timer)
    check_mark.config(text="")
    title_label.config(text="Timer")
    canvas.itemconfig(timer_text, text="00:00")
    global rep
    rep = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #
def start_timer():
    global rep
    rep += 1
    work_sec = WORK_MIN * 60
    short_break = SHORT_BREAK_MIN * 60
    long_break = LONG_BREAK_MIN * 60

    if rep % 2 == 0:
        count_down(short_break)
        title_label.config(text="Short Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=PINK)
    elif rep % 8 == 0:
        count_down(long_break)
        title_label.config(text="Long Break", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=RED)
    else:
        count_down(work_sec)
        title_label.config(text="Work", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(count):
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec < 10:
        count_sec = f"0{count_sec}"
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        mark = ""
        work_segment = math.floor(rep / 2)
        for _ in range(work_segment):
            mark += "✔"
        check_mark.config(text=mark)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

start_btn = Button(text="Start", font=FONT_NAME, command=start_timer)
start_btn.grid(row=3, column=1)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(row=2, column=2)

title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), bg=YELLOW, fg=GREEN)
title_label.grid(row=1, column=2)

reset_btn = Button(text="Reset", font=FONT_NAME, command=Reset)
reset_btn.grid(row=3, column=3)

check_mark = Label(text="", bg=YELLOW, fg=GREEN)
check_mark.grid(row=4, column=2)

window.mainloop()
