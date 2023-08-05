import tkinter
from tkinter import *
from tkinter import messagebox
import random as r
from PIL import Image, ImageTk
def tictactoe():
    global run
    run = 2

    window = tkinter.Tk()

    window.title("Tic Tac Toe")

    window.resizable(0, 0)

    b1 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b1))
    b1.grid(row=1, column=1)
    b2 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b2))
    b2.grid(row=1, column=2)
    b3 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b3))
    b3.grid(row=1, column=3)
    b4 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b4))
    b4.grid(row=2, column=1)
    b5 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b5))
    b5.grid(row=2, column=2)
    b6 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b6))
    b6.grid(row=2, column=3)
    b7 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b7))
    b7.grid(row=3, column=1)
    b8 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b8))
    b8.grid(row=3, column=2)
    b9 = tkinter.Button(window, text=" ", font='Helvetica 19 bold', bg='white', height=4, width=8,command=lambda: btn_click(b9))
    b9.grid(row=3, column=3)

    buttons = [b1, b2, b3, b4, b5, b6, b7, b8, b9]

    def btn_click(btn_clicked):
        btn_clicked['text'] = "X"
        btn_clicked['state'] = 'disabled'
        btn_clicked['bg'] = 'rosybrown'
        btn_clicked["font"] = "Helvetica 19 bold"
        btn_clicked["fg"] = "white"
        def checkforwinner():
            global run
            if b1['text'] == 'X' and b2['text'] == 'X' and b3['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b4['text'] == 'X' and b5['text'] == 'X' and b6['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b7['text'] == 'X' and b8['text'] == 'X' and b9['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b1['text'] == 'X' and b4['text'] == 'X' and b7['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b2['text'] == 'X' and b5['text'] == 'X' and b8['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b3['text'] == 'X' and b6['text'] == 'X' and b9['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b1['text'] == 'X' and b5['text'] == 'X' and b9['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            elif b3['text'] == 'X' and b5['text'] == 'X' and b7['text'] == 'X':
                for btn in buttons:
                    btn['state'] = 'disabled'
                run = 0
                messagebox.showinfo("Tic Tac Toe", "You won!")
                window.destroy()

            else:

                emptybuttons = []

                if b1['text'] == " ":
                    emptybuttons.append(b1)

                if b2['text'] == " ":
                    emptybuttons.append(b2)

                if b3['text'] == " ":
                    emptybuttons.append(b3)

                if b4['text'] == " ":
                    emptybuttons.append(b4)

                if b5["text"] == " ":
                    emptybuttons.append(b5)

                if b6['text'] == " ":
                    emptybuttons.append(b6)

                if b7['text'] == " ":
                    emptybuttons.append(b7)

                if b8['text'] == " ":
                    emptybuttons.append(b8)

                if b9['text'] == " ":
                    emptybuttons.append(b9)

                if emptybuttons == []:
                    messagebox.showinfo("Tic Tac Toe", "This is a tie! The game will be restart.")
                    window.destroy()

                else:
                    random_button = r.choice(emptybuttons)
                    random_button.config(text="O", state=DISABLED, bg="gold", font="Helvetica 19 bold", fg="white")
                    emptybuttons.clear()

                    if b1['text'] == 'O' and b2['text'] == 'O' and b3['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()
                    elif b4['text'] == 'O' and b5['text'] == 'O' and b6['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()

                    elif b7['text'] == 'O' and b8['text'] == 'O' and b9['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()

                    elif b1['text'] == 'O' and b4['text'] == 'O' and b7['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()

                    elif b2['text'] == 'O' and b5['text'] == 'O' and b8['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()

                    elif b3['text'] == 'O' and b6['text'] == 'O' and b9['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()

                    elif b1['text'] == 'O' and b5['text'] == 'O' and b9['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()

                    elif b3['text'] == 'O' and b5['text'] == 'O' and b7['text'] == 'O':
                        for btn in buttons:
                            btn['state'] = 'disabled'
                        run = 1
                        messagebox.showinfo("Tic Tac Toe", "You Lose!")
                        window.destroy()
        checkforwinner()

    window.mainloop()

    if run == 0:
        return True
    elif run == 1:
        return False
    else:
        return tictactoe()