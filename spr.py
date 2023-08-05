from tkinter import *
from PIL import Image, ImageTk
import random
from tkinter import messagebox
import time

def spr():
    global run

    run = True

    top = Toplevel()
    top.title("Rock Scissor Paper")

    rock_img = ImageTk.PhotoImage(Image.open("rock-user.png"))
    paper_img = ImageTk.PhotoImage(Image.open("paper-user.png"))
    scissor_img = ImageTk.PhotoImage(Image.open("scissors-user.png"))
    rock_img_comp = ImageTk.PhotoImage(Image.open("rock.png"))
    paper_img_comp = ImageTk.PhotoImage(Image.open("paper.png"))
    scissor_img_comp = ImageTk.PhotoImage(Image.open("scissors.png"))

    user_label = Label(top, image=scissor_img, bg="#d2b48c")
    comp_label = Label(top, image=scissor_img_comp, bg="#d2b48c")
    comp_label.grid(row=1, column=0)
    user_label.grid(row=1, column=4)

    playerScore = Label(top, text=0, font=100, bg="#d2b48c", fg="black")
    computerScore = Label(top, text=0, font=100, bg="#d2b48c", fg="black")
    computerScore.grid(row=1, column=1)
    playerScore.grid(row=1, column=3)

    user_indicator = Label(top, font=50, text="USER", bg="#d2b48c", fg="black")
    comp_indicator = Label(top, font=50, text="COMPUTER",
                           bg="#d2b48c", fg="black")
    user_indicator.grid(row=0, column=3)
    comp_indicator.grid(row=0, column=1)

    msg = Label(top, font=50, bg="#d2b48c", fg="black")
    msg.grid(row=3, column=2)

    def updateMessage(x):
        msg['text'] = x

    def updateUserScore():
        global score_1, run
        score_1 = int(playerScore["text"])
        score_1 += 1
        playerScore["text"] = str(score_1)
        if playerScore["text"] == 3:
            time.sleep(3)
            exit()

        if score_1 == 3:
            messagebox.showinfo("Rock Scissor Paper", "You won! YEEY!")
            run = True
            top.destroy()

    def updateCompScore():
        global score_2, run
        score_2 = int(computerScore["text"])
        score_2 += 1
        computerScore["text"] = str(score_2)
        if computerScore["text"] == 3:
            time.sleep(3)
            exit()

        if score_2 == 3:
            messagebox.showwarning("Rock Scissor Paper", "You Lose! Next time :(")
            run = False
            top.destroy()

    def checkWin(player, computer):

        score_1 = int(playerScore["text"])
        playerScore["text"] = str(score_1)
        score_2 = int(computerScore["text"])
        computerScore["text"] = str(score_2)

        if player == computer:
            updateMessage("Its a tie!!")
        elif player == "rock":
            if computer == "paper":
                updateMessage("You lose")
                updateCompScore()
            else:
                updateMessage("You Win")
                updateUserScore()
        elif player == "paper":
            if computer == "scissor":
                updateMessage("You lose")
                updateCompScore()
            else:
                updateMessage("You Win")
                updateUserScore()
        elif player == "scissor":
            if computer == "rock":
                updateMessage("You lose")
                updateCompScore()
            else:
                updateMessage("You Win")
                updateUserScore()

        else:
            pass

    choices = ["rock", "paper", "scissor"]

    def updateChoice(x):

        compChoice = choices[random.randint(0, 2)]
        if compChoice == "rock":
            comp_label.configure(image=rock_img_comp)
        elif compChoice == "paper":
            comp_label.configure(image=paper_img_comp)
        else:
            comp_label.configure(image=scissor_img_comp)

        if x == "rock":
            user_label.configure(image=rock_img)
        elif x == "paper":
            user_label.configure(image=paper_img)
        else:
            user_label.configure(image=scissor_img)

        checkWin(x, compChoice)

    rock = Button(top, width=20, height=2, text="ROCK",
                  bg="#FF3E4D", fg="black", command=lambda: updateChoice("rock")).grid(row=2, column=1)
    paper = Button(top, width=20, height=2, text="PAPER",
                   bg="#FAD02E", fg="black", command=lambda: updateChoice("paper")).grid(row=2, column=2)
    scissor = Button(top, width=20, height=2, text="SCISSOR",
                     bg="#0ABDE3", fg="black", command=lambda: updateChoice("scissor")).grid(row=2, column=3)

    top.mainloop()

    return run