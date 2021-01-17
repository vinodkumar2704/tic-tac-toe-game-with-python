from tkinter import *
from tkinter import messagebox
from tkinter import ttk

root=Tk()
root.geometry('528x375')

button1=ttk.Button(root, text=' ', command=lambda:buttonclicked(1))
button1.grid(row=0,column=0,ipadx=50,ipady=50)

button2=ttk.Button(root, text=' ', command=lambda:buttonclicked(2))
button2.grid(row=0,column=1,ipadx=50,ipady=50)

button3=ttk.Button(root, text=' ', command=lambda:buttonclicked(3))
button3.grid(row=0,column=2,ipadx=50,ipady=50)

button4=ttk.Button(root,text=' ',command=lambda:buttonclicked(4))
button4.grid(row=1,column=0,ipadx=50,ipady=50)

button5=ttk.Button(root,text=' ',command=lambda:buttonclicked(5))
button5.grid(row=1,column=1,ipadx=50,ipady=50)

button6=ttk.Button(root,text=' ',command=lambda:buttonclicked(6))
button6.grid(row=1,column=2,ipadx=50,ipady=50)

button7=ttk.Button(root, text =' ',command=lambda:buttonclicked(7))
button7.grid(row=2,column=0,ipadx=50,ipady=50)

button8=ttk.Button(root, text =' ',command=lambda:buttonclicked(8))
button8.grid(row=2,column=1,ipadx=50,ipady=50)

button9=ttk.Button(root,text=' ',command=lambda:buttonclicked(9))
button9.grid(row=2,column=2,ipadx=50,ipady=50)


def checkwinner():
    i = 0

    if (button1['text']=='O' and button2['text']=='O' and button3['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    elif (button4['text']=='O' and button5['text']=='O' and button6['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    elif (button7['text']=='O' and button8['text']=='O' and button9['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    if (button1['text']=='O' and button4['text']=='O' and button7['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    elif (button2['text']=='O' and button5['text']=='O' and button8['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    elif (button3['text']=='O' and button6['text']=='O' and button9['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    elif (button1['text']=='O' and button5['text']=='O' and button9['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1

    elif (button3['text']=='O' and button5['text']=='O' and button7['text']=='O'):
        messagebox._show("congratulations","winner is player 2")
        i = 1






    elif (button1['text']=='X' and button2['text']=='X' and button3['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button4['text']=='X' and button5['text']=='X' and button6['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button7['text']=='X' and button8['text']=='X' and button9['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button1['text']=='X' and button4['text']=='X' and button7['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button2['text']=='X' and button5['text']=='X' and button8['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button3['text']=='X' and button6['text']=='X' and button9['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button1['text']=='X' and button5['text']=='X' and button9['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1

    elif (button7['text']=='X' and button5['text']=='X' and button9['text']=='X'):
        messagebox._show("congratulations","winner is player 1")
        i = 1


    elif (button1['text']!=" " and button2['text']!=" " and button3['text']!=" " and button4['text']!=" " and button5['text']!=" " and button6['text']!=" " and button7['text']!=" " and button8['text']!=" " and button9['text']!=" "  ):
        messagebox._show("oops!","its a tie!")
        i = 1


    if i == 1:
        button1.config(text = " ")
        button2.config(text = " ")
        button3.config(text = " ")
        button4.config(text = " ")
        button5.config(text = " ")
        button6.config(text = " ")
        button7.config(text = " ")
        button8.config(text = " ")
        button9.config(text = " ")
        player = 1



player=1
def buttonclicked(buttonnumber):
    global player

    if (buttonnumber==1 and player==1 and button1['text'] == " "):
        button1.config(text="X")
        player=2
    elif(buttonnumber==1 and player==2 and button1['text'] == " "):
        button1.config(text="O")
        player=1



    if (buttonnumber==2 and player==1 and button2['text'] == " "):
        button2.config(text="X")
        player=2
    elif(buttonnumber==2 and player==2 and button2['text'] == " "):
        button2.config(text="O")
        player=1


    if (buttonnumber==3 and player==1 and button3['text'] == " "):
        button3.config(text="X")
        player=2
    elif(buttonnumber==3 and player==2 and button3['text'] == " "):
        button3.config(text="O")
        player=1

    if (buttonnumber==4 and player==1 and button4['text'] == " "):
        button4.config(text="X")
        player=2
    elif(buttonnumber==4 and player==2 and button4['text'] == " "):
        button4.config(text="O")
        player=1

    if (buttonnumber==5 and player==1 and button5['text'] == " "):
        button5.config(text="X")
        player=2
    elif(buttonnumber==5 and player==2 and button5['text'] == " "):
        button5.config(text="O")
        player=1

    if (buttonnumber==6 and player==1 and button6['text'] == " "):
        button6.config(text="X")
        player=2
    elif(buttonnumber==6 and player==2 and button6['text'] == " "):
        button6.config(text="O")
        player=1

    if (buttonnumber==7 and player==1 and button7['text'] == " "):
        button7.config(text="X")
        player=2
    elif(buttonnumber==7 and player==2 and button7['text'] == " "):
        button7.config(text="O")
        player=1

    if (buttonnumber==8 and player==1 and button8['text'] == " "):
        button8.config(text="X")
        player=2
    elif(buttonnumber==8 and player==2 and button8['text'] == " "):
        button8.config(text="O")
        player=1

    if (buttonnumber==9 and player==1 and button9['text'] == " "):
        button9.config(text="X")
        player=2
    elif(buttonnumber==9 and player==2 and button9['text'] == " "):
        button9.config(text="O")
        player=1

    checkwinner()





root.mainloop()