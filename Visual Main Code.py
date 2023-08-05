from tkinter import*
import random
from hangman import hangman
from tictactoe import tictactoe
from spr import spr

Categories=["scıence","history","cografya","art","spor","cinema"]
Question_numbers=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
                  [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15]]


user_jokers=[0,0,0]
question_no=1
score=[]
fails=[]
joker_1=1
joker_2=1
joker_3=1

Category_gain=False
Hint_gain=False
Half_gain=False

a=hangman()
if(a==True):
    user_jokers[0]=joker_1
    Category_gain=True

root=Tk()
root.title("Quiz Game")
root["bg"]="dark cyan"
count=0
label_quizname=Label(root,text="Welcome to the our Quiz Game",font=("Arial",30))
label_quizname.place(x=450,y=30)
label_name=Label(root,text="Username =",font=("Arial",25),bg="dark cyan")
label_name.place(x=450,y=245)
entry_name=Entry(root,font=("Arial",20))
entry_name.place(x=650,y=250)

Hint_used=False
Category_used=False

def specialq():
    global question_no, Hint_gain, Half_gain, user_jokers

    if (question_no == 6):
        a = spr()
        if a == True:
            user_jokers[1] = joker_2
            Hint_gain = True

    if (question_no == 11):
        c = tictactoe()
        if (c == True):
            user_jokers[2] = joker_3
            Half_gain = True


def question():
    global user_jokers

    categ=random.choice(Categories)
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    
    global data
    data=file.readlines()
    
    label_quizname.destroy()
    label_name.destroy()
    entry_name.destroy()
    button0.destroy()
    
    global label_categ
    global label_0
    global label_1
    global label_2
    global label_3
    global label_4
    
    label_categ=Label(root,text="Category : "+categ,font=("Arial",20))
    label_categ.place(x=1300,y=90)
      
            
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)
    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)
    
    if(user_jokers!=[0,0,0]):
        
        global button_yes1
        global button_no1
        global label_yesno1
        
        label_yesno1=Label(root,text="Do you want to use a Joker? Press YES or NO",font=("Arial",20))
        label_yesno1.place(x=30,y=625)

        button_no1=Button(root,text="NO",font=("Arial",20),command=PressNo1)
        button_no1.place(x=350,y=675)
        
        button_yes1=Button(root,text="YES",font=("Arial",20),command=PressYes1)
        button_yes1.place(x=170,y=675)
        
    else:
        
        label_yesno1=Label(root,text="Do you want to use a Joker? Press YES or NO",font=("Arial",20))
        label_yesno1.place(x=30,y=625)
        
        button_no1=Button(root,text="NO",font=("Arial",20),command=PressNo1)
        button_no1.place(x=350,y=675)
        
        button_yes1=Button(root,text="YES",font=("Arial",20),command=PressYes1)
        button_yes1.place(x=170,y=675)
        
        PressNo1()
        

def PressYes1():
    
    
    button_yes1.destroy()
    button_no1.destroy()
    label_yesno1.destroy()
    
    global indicator1
    indicator1=Label(root,text=" OWNED JOKERS "+"\n"+"____________________",font=("Arial",20))
    indicator1.place(x=1070,y=230)
    
    for i in user_jokers:
        if(i!=0):
            if(i=="CATEGORY"):
                global category_button
                category_button=Button(root,text="< CATEGORY JOKER >",font=("Arial",18),command=Category)
                category_button.place(x=1085,y=330)
            elif(i=="HINT"):
                global hint_button
                hint_button=Button(root,text="< HINT JOKER >",font=("Arial",18),command=Hint)
                hint_button.place(x=1116,y=450)
            elif(i=="HALF_AND_HALF"):
                global half_button
                half_button=Button(root,text="< HALF AND HALF JOKER >",font=("Arial",18),command=Half_and_Half)
                half_button.place(x=1059,y=570)
    
                
def Category():

    global Category_used
    Category_used=True

    if(Category_gain==True):
        category_button.destroy()
        
    if(Hint_gain==True):
        hint_button.destroy()
        
    if(Half_gain==True):
        half_button.destroy()
        
    indicator1.destroy()

    label_categ.destroy()
    label_0.destroy()
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()

    
    user_jokers[0]=0
    
    global indicator2
    indicator2=Label(root,text="~ CATEGORIES ~"+"\n"+"___________________________",font=("Arial",20))
    indicator2.place(x=900,y=200)
    
    global science_button
    science_button=Button(root,text="1) SCIENCE",font=("Helvetica",18,'bold'),bg="#32cd32",command=science)
    science_button.place(x=900,y=350)
    
    global history_button
    history_button=Button(root,text="2) HISTORY",font=("Arial",18,'bold'),bg="#daa520",command=history)
    history_button.place(x=1150,y=350)
    
    global geography_button
    geography_button=Button(root,text="3) GEOGRAPHY",font=("Arial",18,'bold'),bg="#6495ed",command=geography)
    geography_button.place(x=900,y=450)
    
    global art_button
    art_button=Button(root,text="4) ART",font=("Arial",18,'bold'),bg="#ff0000",command=art)
    art_button.place(x=1175,y=450)
    
    global sport_button
    sport_button=Button(root,text="5) SPORT",font=("Arial",18,'bold'),bg="#ff4500",command=sport)
    sport_button.place(x=900,y=550)
    
    global cinema_button
    cinema_button=Button(root,text="6) CINEMA",font=("Arial",18,'bold'),bg="#f08080",command=cinema)
    cinema_button.place(x=1150,y=550)

    

def science():
    
    global indicator2
    indicator2.destroy()
        
    categ="science"
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    global data
    data=file.readlines()
    
    global label_categ
    label_categ=Label(root,text=" Chosen Category : "+categ,font=("Arial",20))
    label_categ.place(x=1200,y=90)

    global label_0
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    global label_1
    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    global label_2
    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    global label_3
    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)

    global label_4    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)

    science_button.destroy()
    history_button.destroy()
    geography_button.destroy()
    art_button.destroy()
    sport_button.destroy()
    cinema_button.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
    

def history():
    
    global indicator2
    indicator2.destroy()
    
    categ="history"
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    global data
    data=file.readlines()
    
    global label_categ
    label_categ=Label(root,text=" Chosen Category : "+categ,font=("Arial",20))
    label_categ.place(x=1200,y=90)

    global label_0
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    global label_1
    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    global label_2
    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    global label_3
    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)

    global label_4    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)

    science_button.destroy()
    history_button.destroy()
    geography_button.destroy()
    art_button.destroy()
    sport_button.destroy()
    cinema_button.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
        

def geography():
    
    global indicator2
    indicator2.destroy()
        
    categ="geography"
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    global data
    data=file.readlines()
    
    global label_categ
    label_categ=Label(root,text=" Chosen Category : "+categ,font=("Arial",20))
    label_categ.place(x=1200,y=90)

    global label_0
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    global label_1
    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    global label_2
    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    global label_3
    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)

    global label_4    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)

    science_button.destroy()
    history_button.destroy()
    geography_button.destroy()
    art_button.destroy()
    sport_button.destroy()
    cinema_button.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
        
    
def art():
    
    global indicator2
    indicator2.destroy()

    categ="art"
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    
    global data
    data=file.readlines()
  
    global label_categ
    label_categ=Label(root,text=" Chosen Category : "+categ,font=("Arial",20))
    label_categ.place(x=1200,y=90)

    global label_0
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    global label_1
    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    global label_2
    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    global label_3
    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)

    global label_4    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)

    science_button.destroy()
    history_button.destroy()
    geography_button.destroy()
    art_button.destroy()
    sport_button.destroy()
    cinema_button.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
        
    
def sport():
    global indicator2
    indicator2.destroy()
        
    categ="spor"
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    global data
    data=file.readlines()
   
    global label_categ
    label_categ=Label(root,text=" Chosen Category : "+categ,font=("Arial",20))
    label_categ.place(x=1200,y=90)

    global label_0
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    global label_1
    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    global label_2
    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    global label_3
    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)

    global label_4    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)

    science_button.destroy()
    history_button.destroy()
    geography_button.destroy()
    art_button.destroy()
    sport_button.destroy()
    cinema_button.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
        
    
def cinema():
    
    global indicator2
    indicator2.destroy()
        
    categ="cinema"
    number=random.choice(Question_numbers[Categories.index(categ)])
    Question_numbers[Categories.index(categ)].remove(number)
    file=open(categ+str(number)+".txt","r")
    global data
    data=file.readlines()
    
    global label_categ
    label_categ=Label(root,text=" Chosen Category : "+categ,font=("Arial",20))
    label_categ.place(x=1200,y=90)

    global label_0
    label_0=Label(root,text="Question "+str(question_no)+") "+data[0].rstrip(),font=("Arial",18))
    label_0.place(x=30,y=10)

    global label_1
    label_1=Label(root,text=data[1].rstrip(),font=("Arial",20))
    label_1.place(x=50,y=150)

    global label_2
    label_2=Label(root,text=data[2].rstrip(),font=("Arial",20))
    label_2.place(x=50,y=250)

    global label_3
    label_3=Label(root,text=data[3].rstrip(),font=("Arial",20))
    label_3.place(x=50,y=350)

    global label_4    
    label_4=Label(root,text=data[4].rstrip(),font=("Arial",20))
    label_4.place(x=50,y=450)

     
    science_button.destroy()
    history_button.destroy()
    geography_button.destroy()
    art_button.destroy()
    sport_button.destroy()
    cinema_button.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
    

def Hint():

    if(Category_gain==True):    
        category_button.destroy()
    hint_button.destroy()
    half_button.destroy()
    indicator1.destroy()
    
    user_jokers[1]=0
    
    global Hint_used
    Hint_used=True
    
    global hint
    hint=Label(root,text=data[6].rstrip(),font=("Arial",18))
    hint.place(x=30,y=540)

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
        


def Half_and_Half():
    
    if(Category_gain==True):
        category_button.destroy()
    hint_button.destroy()
    half_button.destroy()
    indicator1.destroy()
    
    user_jokers[2]=0
    sample_txt=[data[5].rstrip(),"A","B","C","D"]
    eliminate=0
    elimination=[]

    while(eliminate<2):
        option=random.choice(sample_txt)
        
        if(option!=data[5].rstrip()):
            
            if(option not in elimination):
                elimination.append(option)
                eliminate+=1
                
    for j in elimination:
        if(j=="A"):
            label_1.destroy()
        elif(j=="B"):
            label_2.destroy()
        elif(j=="C"):
            label_3.destroy()
        else:
            label_4.destroy()

    if(user_jokers!=[0,0,0]):
        Another_joker()

    else:
        PressNo1()
        
    
def Another_joker():
    
    global Hint_used
    global Category_used
    
    if(Hint_used==True and Category_used==True):
        hint.destroy()
        Hint_used=0

    global button_yes1
    global button_no1
    global label_yesno1
    
    label_yesno1=Label(root,text="Do you want to use Another Joker? Press YES or NO",font=("Arial",20))
    label_yesno1.place(x=30,y=625)

    button_no1=Button(root,text="NO",font=("Arial",20),command=PressNo1)
    button_no1.place(x=350,y=675)
        
    button_yes1=Button(root,text="YES",font=("Arial",20),command=PressYes1)
    button_yes1.place(x=170,y=675)
    
    
def PressNo1():
    
    global Hint_used
    global Category_used
    
    if(Hint_used==True and Category_used==True):
        hint.destroy()
        Hint_used=0

    button_yes1.destroy()
    button_no1.destroy()
    label_yesno1.destroy()

    global button_1A
    global button_1B
    global button_1C
    global button_1D
    
    button_1A=Button(root,text="Answer : A",font=("Arial",20),command=CheckAnswer_A)
    button_1A.place(x=700,y=150)
    
    button_1B=Button(root,text="Answer : B",font=("Arial",20),command=CheckAnswer_B)
    button_1B.place(x=700,y=250)
    
    button_1C=Button(root,text="Answer : C",font=("Arial",20),command=CheckAnswer_C)
    button_1C.place(x=700,y=350)
    
    button_1D=Button(root,text="Answer : D",font=("Arial",20),command=CheckAnswer_D)
    button_1D.place(x=700,y=450)
    

def CheckAnswer_A():
    
    global Hint_used
    global Category_used
    
    if(Hint_used==True and Category_used==False):
        hint.destroy()
        Hint_used=0
        
    ANSWER="A"

    label_categ.destroy()
    label_0.destroy()
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()
    
    button_1A.destroy()
    button_1B.destroy()
    button_1C.destroy()
    button_1D.destroy()

    global Next
    
    if(ANSWER==data[5].rstrip()):
        
        score.append(1)
        
        global correct
        correct=Label(root,text="CORRECT, THE ANSWER WAS "+ANSWER,font=("Arial",30))
        correct.place(x=420,y=73)

        global correct_indicator1
        correct_indicator1=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator1.place(x=430,y=267)

        global wrong_indicator1
        wrong_indicator1=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator1.place(x=430,y=461)
                               
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand1)
        Next.place(x=680,y=655)
    else:

        fails.append(1)
        
        global wrong
        wrong=Label(root,text="WRONG, THE CORRECT ANSWER WAS "+data[5].rstrip(),font=("Arial",30))
        wrong.place(x=350,y=88)

        global correct_indicator2
        correct_indicator2=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator2.place(x=430,y=282)

        global wrong_indicator2
        wrong_indicator2=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator2.place(x=430,y=476)
        
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand2)
        Next.place(x=680,y=670)
        

def CheckAnswer_B():

    global Hint_used
    global Category_used
    
    if(Hint_used==True and Category_used==False):
        hint.destroy()
        Hint_used=0
        
    ANSWER="B"

    label_categ.destroy()
    label_0.destroy()
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()
    
    button_1A.destroy()
    button_1B.destroy()
    button_1C.destroy()
    button_1D.destroy()

    global Next
    
    if(ANSWER==data[5].rstrip()):
        
        score.append(1)
        
        global correct
        correct=Label(root,text="CORRECT, THE ANSWER WAS "+ANSWER,font=("Arial",30))
        correct.place(x=420,y=73)

        global correct_indicator1
        correct_indicator1=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator1.place(x=430,y=267)

        global wrong_indicator1
        wrong_indicator1=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator1.place(x=430,y=461)
                               
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand1)
        Next.place(x=680,y=655)
    else:

        fails.append(1)
        
        global wrong
        wrong=Label(root,text="WRONG, THE CORRECT ANSWER WAS "+data[5].rstrip(),font=("Arial",30))
        wrong.place(x=350,y=88)

        global correct_indicator2
        correct_indicator2=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator2.place(x=430,y=282)

        global wrong_indicator2
        wrong_indicator2=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator2.place(x=430,y=476)
        
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand2)
        Next.place(x=680,y=670)
        

def CheckAnswer_C():

    global Hint_used
    global Category_used
    
    if(Hint_used==True and Category_used==False):
        hint.destroy()
        Hint_used=0
        
    ANSWER="C"

    label_categ.destroy()
    label_0.destroy()
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()
    
    button_1A.destroy()
    button_1B.destroy()
    button_1C.destroy()
    button_1D.destroy()

    global Next
    
    if(ANSWER==data[5].rstrip()):
        
        score.append(1)
        
        global correct
        correct=Label(root,text="CORRECT, THE ANSWER WAS "+ANSWER,font=("Arial",30))
        correct.place(x=420,y=73)

        global correct_indicator1
        correct_indicator1=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator1.place(x=430,y=267)

        global wrong_indicator1
        wrong_indicator1=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator1.place(x=430,y=461)
                               
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand1)
        Next.place(x=680,y=655)
    else:

        fails.append(1)
        
        global wrong
        wrong=Label(root,text="WRONG, THE CORRECT ANSWER WAS "+data[5].rstrip(),font=("Arial",30))
        wrong.place(x=350,y=88)

        global correct_indicator2
        correct_indicator2=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator2.place(x=430,y=282)

        global wrong_indicator2
        wrong_indicator2=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator2.place(x=430,y=476)
        
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand2)
        Next.place(x=680,y=670)
        
def CheckAnswer_D():

    global Hint_used
    global Category_used
    
    if(Hint_used==True and Category_used==False):
        hint.destroy()
        Hint_used=0
        
    ANSWER="D"

    label_categ.destroy()
    label_0.destroy()
    label_1.destroy()
    label_2.destroy()
    label_3.destroy()
    label_4.destroy()
    
    button_1A.destroy()
    button_1B.destroy()
    button_1C.destroy()
    button_1D.destroy()

    global Next
    
    if(ANSWER==data[5].rstrip()):
        
        score.append(1)
        
        global correct
        correct=Label(root,text="CORRECT, THE ANSWER WAS "+ANSWER,font=("Arial",30))
        correct.place(x=420,y=73)

        global correct_indicator1
        correct_indicator1=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator1.place(x=430,y=267)

        global wrong_indicator1
        wrong_indicator1=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator1.place(x=430,y=461)
                               
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand1)
        Next.place(x=680,y=655)
    else:

        fails.append(1)
        
        global wrong
        wrong=Label(root,text="WRONG, THE CORRECT ANSWER WAS "+data[5].rstrip(),font=("Arial",30))
        wrong.place(x=350,y=88)

        global correct_indicator2
        correct_indicator2=Label(root,text="Correct Answer : "+str(sum(score)),font=("Arial",30))
        correct_indicator2.place(x=430,y=282)

        global wrong_indicator2
        wrong_indicator2=Label(root,text="Wrong Answer : "+str(sum(fails)),font=("Arial",30))
        wrong_indicator2.place(x=430,y=476)
        
        Next=Button(root,text="NEXT",font=("Arial",30),command=FinalCommand2)
        Next.place(x=680,y=670)
        

def FinalCommand1():
    
    global question_no
    question_no+=1
    correct.destroy()
    correct_indicator1.destroy()
    wrong_indicator1.destroy()
    Next.destroy()
    
    if question_no!=15:
        specialq()
        question()

def FinalCommand2():
    
    global question_no
    question_no+=1
    wrong.destroy()
    correct_indicator2.destroy()
    wrong_indicator2.destroy()
    Next.destroy()
    
    if question_no!=15:
        specialq()
        question()


button0=Button(root,text="SUBMIT",font=("Arial",30),command=question)
button0.place(x=650,y=350)

root.mainloop()