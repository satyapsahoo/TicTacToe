from tkinter import *
BACKGROUND_COLOR = "#B1DDC6"
PLAYER_1 = "YAY"
PLAYER_2 = "NAY"
VALUE_0_0 = ""
VALUE_0_1 = ""
VALUE_0_2 = ""
VALUE_1_0 = ""
VALUE_1_1 = ""
VALUE_1_2 = ""
VALUE_2_0 = ""
VALUE_2_1 = ""
VALUE_2_2 = ""
COUNT = 0


def check_player():
    if COUNT % 2 == 0:
        ret_text = PLAYER_1
    else:
        ret_text = PLAYER_2
    return ret_text


def check_winner():
    if VALUE_0_0 == VALUE_0_1 == VALUE_0_2 or VALUE_0_0 == VALUE_1_1 == VALUE_2_2 \
            or VALUE_0_0 == VALUE_1_0 == VALUE_2_0:
        if VALUE_0_0 == PLAYER_1:
            canvas_status.itemconfig(status, text="PLAYER 1 WINS!")
            return 1
        elif VALUE_0_0 == PLAYER_2:
            canvas_status.itemconfig(status, text="PLAYER 2 WINS!")
            return 1

    if VALUE_2_2 == VALUE_2_1 == VALUE_2_0 or VALUE_2_2 == VALUE_1_2 == VALUE_0_2:
        if VALUE_2_2 == PLAYER_1:
            canvas_status.itemconfig(status, text="PLAYER 1 WINS!")
            return 1
        elif VALUE_2_2 == PLAYER_2:
            canvas_status.itemconfig(status, text="PLAYER 2 WINS!")
            return 1

    if VALUE_2_0 == VALUE_1_1 == VALUE_0_2:
        if VALUE_2_0 == PLAYER_1:
            canvas_status.itemconfig(status, text="PLAYER 1 WINS!")
            return 1
        elif VALUE_2_0 == PLAYER_2:
            canvas_status.itemconfig(status, text="PLAYER 2 WINS!")
            return 1

    if VALUE_0_1 == VALUE_1_1 == VALUE_2_1:
        if VALUE_0_1 == PLAYER_1:
            canvas_status.itemconfig(status, text="PLAYER 1 WINS!")
            return 1
        elif VALUE_0_1 == PLAYER_2:
            canvas_status.itemconfig(status, text="PLAYER 2 WINS!")
            return 1

    if VALUE_1_0 == VALUE_1_1 == VALUE_1_2:
        if VALUE_1_0 == PLAYER_1:
            canvas_status.itemconfig(status, text="PLAYER 1 WINS!")
            return 1
        elif VALUE_1_0 == PLAYER_2:
            canvas_status.itemconfig(status, text="PLAYER 2 WINS!")
            return 1

    if COUNT == 8:
        canvas_status.itemconfig(status, text="DRAW GAME!")
        return 1

    return 0


def next_player():
    global COUNT
    COUNT = COUNT + 1
    if COUNT % 2 == 0:
        canvas_status.itemconfig(status, text="Player 1 (X) Turn")
    else:
        canvas_status.itemconfig(status, text="Player 2 (X) Turn")


def click_0_0(event):
    global VALUE_0_0
    canvas_0_0.delete(image_0_0)
    canvas_0_0.itemconfig(text_0_0, text=check_player())
    VALUE_0_0 = canvas_0_0.itemcget(text_0_0, 'text')
    if check_winner() == 0:
        next_player()


def click_0_1(event):
    global VALUE_0_1
    canvas_0_1.delete(image_0_1)
    canvas_0_1.itemconfig(text_0_1, text=check_player())
    VALUE_0_1 = canvas_0_1.itemcget(text_0_1, 'text')
    if check_winner() == 0:
        next_player()


def click_0_2(event):
    global VALUE_0_2
    canvas_0_2.delete(image_0_2)
    canvas_0_2.itemconfig(text_0_1, text=check_player())
    VALUE_0_2 = canvas_0_2.itemcget(text_0_2, 'text')
    if check_winner() == 0:
        next_player()


def click_1_0(event):
    global VALUE_1_0
    canvas_1_0.delete(image_1_0)
    canvas_1_0.itemconfig(text_1_0, text=check_player())
    VALUE_1_0 = canvas_1_0.itemcget(text_1_0, 'text')
    if check_winner() == 0:
        next_player()


def click_1_1(event):
    global VALUE_1_1
    canvas_1_1.delete(image_1_1)
    canvas_1_1.itemconfig(text_1_1, text=check_player())
    VALUE_1_1 = canvas_1_1.itemcget(text_1_1, 'text')
    if check_winner() == 0:
        next_player()


def click_1_2(event):
    global VALUE_1_2
    canvas_1_2.delete(image_1_2)
    canvas_1_2.itemconfig(text_1_2, text=check_player())
    VALUE_1_2 = canvas_1_2.itemcget(text_1_2, 'text')
    if check_winner() == 0:
        next_player()


def click_2_0(event):
    global VALUE_2_0
    canvas_2_0.delete(image_2_0)
    canvas_2_0.itemconfig(text_2_0, text=check_player())
    VALUE_2_0 = canvas_2_0.itemcget(text_2_0, 'text')
    if check_winner() == 0:
        next_player()


def click_2_1(event):
    global VALUE_2_1
    canvas_2_1.delete(image_2_1)
    canvas_2_1.itemconfig(text_2_1, text=check_player())
    VALUE_2_1 = canvas_2_1.itemcget(text_2_1, 'text')
    if check_winner() == 0:
        next_player()


def click_2_2(event):
    global VALUE_2_2
    canvas_2_2.delete(image_2_2)
    canvas_2_2.itemconfig(text_2_2, text=check_player())
    VALUE_2_2 = canvas_2_2.itemcget(text_2_2, 'text')
    if check_winner() == 0:
        next_player()


# Creating a new window and configurations
window = Tk()
window.title("TicTacToe Game!")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

# Create 9 canvas for a 3X3 matrix
dot = PhotoImage(file='./images/white.png')

canvas_0_0 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_0_0 = canvas_0_0.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_0_0 = canvas_0_0.create_image(100, 100, image=dot)
canvas_0_0.bind('<Button-1>', click_0_0)
canvas_0_0.grid(row=0, column=0)

canvas_0_1 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_0_1 = canvas_0_1.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_0_1 = canvas_0_1.create_image(100, 100, image=dot)
canvas_0_1.bind('<Button-1>', click_0_1)
canvas_0_1.grid(row=0, column=1)

canvas_0_2 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_0_2 = canvas_0_2.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_0_2 = canvas_0_2.create_image(100, 100, image=dot)
canvas_0_2.bind('<Button-1>', click_0_2)
canvas_0_2.grid(row=0, column=2)

canvas_1_0 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_1_0 = canvas_1_0.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_1_0 = canvas_1_0.create_image(100, 100, image=dot)
canvas_1_0.bind('<Button-1>', click_1_0)
canvas_1_0.grid(row=1, column=0)

canvas_1_1 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_1_1 = canvas_1_1.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_1_1 = canvas_1_1.create_image(100, 100, image=dot)
canvas_1_1.bind('<Button-1>', click_1_1)
canvas_1_1.grid(row=1, column=1)

canvas_1_2 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_1_2 = canvas_1_2.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_1_2 = canvas_1_2.create_image(100, 100, image=dot)
canvas_1_2.bind('<Button-1>', click_1_2)
canvas_1_2.grid(row=1, column=2)

canvas_2_0 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_2_0 = canvas_2_0.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_2_0 = canvas_2_0.create_image(100, 100, image=dot)
canvas_2_0.bind('<Button-1>', click_2_0)
canvas_2_0.grid(row=2, column=0)

canvas_2_1 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_2_1 = canvas_2_1.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_2_1 = canvas_2_1.create_image(100, 100, image=dot)
canvas_2_1.bind('<Button-1>', click_2_1)
canvas_2_1.grid(row=2, column=1)

canvas_2_2 = Canvas(width=200, height=200, bg=BACKGROUND_COLOR, highlightthickness=1)
text_2_2 = canvas_2_2.create_text(100, 100, fill="darkblue", font="Times 80 bold", text="")
image_2_2 = canvas_2_2.create_image(100, 100, image=dot)
canvas_2_2.bind('<Button-1>', click_2_2)
canvas_2_2.grid(row=2, column=2)

canvas_status = Canvas(width=600, height=80, bg=BACKGROUND_COLOR, highlightthickness=1)
status = canvas_status.create_text(300, 40, fill="red", font="Times 30 bold", text="Player 1 (X) Turn")
canvas_status.grid(row=3, column=0, columnspan=3)

window.mainloop()
