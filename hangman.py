from tkinter import *
from tkinter import messagebox
import random as r

def hangman():
    global run
    global used_words
    run = 0

    window = Tk()
    window.title("HangMan")

    word_list = []
    f = open("words.txt", "r")
    for i in f:
        word_list.append(i.strip())
    f.close()

    photos = [PhotoImage(file="h1.png"), PhotoImage(file="h2.png"), PhotoImage(file="h3.png"),
              PhotoImage(file="h4.png"),
              PhotoImage(file="h5.png"), PhotoImage(file="h6.png"), PhotoImage(file="h7.png")]

    def newGame():

        global the_word_withSpaces, numberOfGuesses, the_word, used_words
        numberOfGuesses = 0
        imgLabel.config(image=photos[0])
        the_word = r.choice(word_list).upper()
        the_word_withSpaces = " ".join(the_word)
        lblWord.set(" ".join("_" * len(the_word)))
        used_words=set()

    def guess(letter):
        if letter in used_words:
            messagebox.showwarning("HangMan", "You already try this letter!")
        else:
            global numberOfGuesses, run
            used_words.add(letter)
            used.config(text='You used these words: {}'.format(used_words))
            if 0 <= numberOfGuesses < 7:
                txt = list(the_word_withSpaces)
                guessed = list(lblWord.get())
                if the_word_withSpaces.count(letter) > 0:
                    for c in range(len(txt)):
                        if txt[c] == letter:
                            guessed[c] = letter
                        lblWord.set("".join(guessed))
                        if lblWord.get() == the_word_withSpaces:
                            messagebox.showinfo("HangMan", "You guessed it!")
                            run = 1
                            window.destroy()

                else:
                    numberOfGuesses += 1
                    imgLabel.config(image=photos[numberOfGuesses])
                    liveslabel.config(text='Lifes = {}'.format(6 - numberOfGuesses))
                    if numberOfGuesses == 6:
                        messagebox.showwarning("HangMan", f"You lose! Next time... The word was {the_word}")
                        window.destroy()

    liveslabel = Label(window, text="Lifes = 6", font="Helvetica 18", fg="red")
    liveslabel.grid(row=1, column=1,sticky="S")

    used=Label(window, text="You used these words: ", font="Helvetica 16")
    used.grid(row=3, column=1)

    imgLabel = Label(window)
    imgLabel.grid(row=0, column=0, columnspan=3, padx=10, pady=40)
    imgLabel.config(image=photos[0])

    lblWord = StringVar()
    Label(window, textvariable=lblWord, font=("Consolas 24 bold")).grid(row=0, column=4, columnspan=6, padx=10)

    colors=["red", "green", "blue", "cyan", "yellow", "magenta"]
    n = 0
    for c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
        Button(window, text=c, command=lambda c=c: guess(c), fg=str(r.choice(colors)) , bg="#D9D8D7", font=("Helvetica 18"), width=4).grid(row=1 + n // 9,column=3 + n % 9)
        n += 1

    Button(window, text="Pass the\nGame", command=lambda: window.destroy(), font=("Helvetica 10 bold")).grid(row=3,column=11,sticky="NSEW")

    newGame()
    window.mainloop()

    if run==1:
        return True
    else:
        return False