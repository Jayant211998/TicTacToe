from tkinter import *
from tkinter import messagebox
import random
#import time
# from goto import goto,label

def Property(x):
    prop = []
    for i in x:
        u = []
        if (i // 3 == i % 3):
            u.append(1)
        if (i // 3 + i % 3 == 2):
            u.append(2)
        if (i // 3 == 0):
            u.append(30)
        if (i // 3 == 1):
            u.append(31)
        if (i // 3 == 2):
            u.append(32)
        if (i % 3 == 0):
            u.append(40)
        if (i % 3 == 1):
            u.append(41)
        if (i % 3 == 2):
            u.append(42)
        prop.append(u)
    return prop


def attackordefend(l, x, prop):
    for i in l:
        if l.count(i) == 2:
            for j in prop:
                for k in j:
                    if i == k and prop.index(j) in x:
                        return prop.index(j)
    return (-1)


def isodd(x, l, u1, prop):
    if len(u1) == 2:
        if (len(prop[u1[0]]) == 3 and len(prop[u1[1]]) == 2):
            return True
        if (len(prop[u1[0]]) == 2 and len(prop[u1[1]]) == 3):
            return True
    return False


def iseven(x, l, u1, prop):
    if len(u1) == 2:
        if (len(prop[u1[0]]) == 3 and len(prop[u1[1]]) == 3):
            return True
    return False


def isnone(x, l, u1, prop):
    if len(u1) == 2:
        if u1[0] % 2 == 1 and u1[1] % 2 == 1:
            return True
    return False


def whichodd(x, l, u1, prop):
    if len(prop[u1[0]]) > len(prop[u1[1]]):
        a, b = u1[0], u1[1]
    else:
        b, a = u1[0], u1[1]
    if (a == 2 and b == 7) or (a == 6 and b == 5):
        return 8
    elif (a == 2 and b == 3) or (a == 6 and b == 1):
        return 0
    elif (a == 0 and b == 7) or (a == 8 and b == 3):
        return 6
    elif (a == 0 and b == 5) or (a == 8 and b == 1):
        return 2


def whicheven(x, l, u1, prop):
    if u1[0] % 2 == 0 and u1[1] % 2 == 0 and u1[0] != 4 and u1[1] != 4:
        return (random.choice([1,3,5,7]))


def whichnone(x, l, u1, prop):
    if (u1[0] + u1[1] - 4) != 4:
        return (u1[0] + u1[1] - 4)
    else:
        return (0)


def gameover(user, comp):
    global u
    for i in comp:
        if comp.count(i) == 3:
            #   print("You Lose")
            lb1 = Label(window, text="YOU LOSE", font=("Times New Roman", "10"))
            lb1.grid(row=4, column=2, rowspan=3)
            btn.clear()
            return 0
    for i in user:
        if user.count(i) == 3:
            lb1 = Label(window, text="YOU WIN", font=("Times New Roman", "10"))
            lb1.grid(row=4, column=2, rowspan=3)
            btn.clear()
            btn12 = Button(window, text=" Next Level", bg="lightgreen", width=8, height=1,
                           font=("Times New Roman", "10"),
                           command=click12)
            btn12.grid(column=0, row=7)
            return 0
    if turn >= 9:
        # print("Game Over")
        lb1 = Label(window, text="GAME OVER", font=("Times New Roman", "10"))
        lb1.grid(row=4, column=2, rowspan=3)
        btn.clear()
        return 0
    return 1


def compturn(comp, user, prop, x, u1, c1, l):
    global level
    global turn
    if level == 1:
        if gameover(user, comp) == 1:
            a = random.choice(x)
            turn += 2
            try:
                if btn[a]["text"] == " ":
                    btn[a]["text"] = "O"
                comp.extend(prop[a])
                x.remove(a)
            except:
                lb1 = Label(window, text="GAME OVER", font=("Times New Roman", "10"))
                lb1.grid(row=4, column=2, rowspan=3)
    elif level == 2:
        if gameover(user, comp) == 1:
            if (attackordefend(comp, x, prop) >= 0):
                a = attackordefend(comp, x, prop)
                # print("attack")
            elif (attackordefend(user, x, prop) >= 0):
                a = attackordefend(user, x, prop)
                # print("defend")
            else:
                try:
                    a = random.choice(x)
                except:
                    lb1 = Label(window, text="GAME OVER", font=("Times New Roman", "10"))
                    lb1.grid(row=4, column=2, rowspan=3)
            turn += 2
            try:
                if btn[a]["text"] == " ":
                    btn[a]["text"] = "O"
                comp.extend(prop[a])
                x.remove(a)
            except:
                lb1 = Label(window, text="GAME OVER", font=("Times New Roman", "10"))
                lb1.grid(row=4, column=2, rowspan=3)
    else:
        if gameover(user, comp) == 1:
            if (attackordefend(comp, x, prop) >= 0):
                a = attackordefend(comp, x, prop)
                # print("attack")
            elif (attackordefend(user, x, prop) >= 0):
                a = attackordefend(user, x, prop)
                # print("defend")
            elif (attackordefend(user, x, prop) == -1 and isodd(x, l, u1, prop)):
                a = whichodd(x, l, u1, prop)
            elif (attackordefend(user, x, prop) == -1 and iseven(x, l, u1, prop)):
                a = whicheven(x, l, u1, prop)
            elif (attackordefend(user, x, prop) == -1 and isnone(x, l, u1, prop)):
                a = whichnone(x, l, u1, prop)
            else:
                try:
                    a = x[len(x) - 1]
                except:
                    lb1 = Label(window, text="GAME OVER", font=("Times New Roman", "10"))
                    lb1.grid(row=4, column=2, rowspan=3)
            turn += 2
            try:
                if btn[a]["text"] == " ":
                    btn[a]["text"] = "O"
                comp.extend(prop[a])
                x.remove(a)
            except:
                lb1 = Label(window, text="GAME OVER", font=("Times New Roman", "10"))
                lb1.grid(row=4, column=2, rowspan=3)


def firstmove(u):
    global turn
    turn += 2
    if u != 4:
        btn[4]["text"] = "O"
        comp.extend(prop[4])
        x.remove(4)
        turn = 2
        c1.append(4)
    else:
        r=random.choice([0,2,6,8])
        btn[r]["text"] = "O"
        comp.extend(prop[r])
        x.remove(r)
        turn = 2
        c1.append(r)


def change(u):
    global x
    global user
    user.extend(prop[u])
    x.remove(u)
    u1.append(u)


def click1():
    #    label .SB
    try:
        if btn[0]["text"] == " ":
            btn[0]["text"] = "X"
            u = 0
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        print("Error")


def click2():
    try:
        if btn[1]["text"] == " ":
            btn[1]["text"] = "X"
            u = 1
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        print("Error")


def click3():
    try:
        if btn[2]["text"] == " ":
            btn[2]["text"] = "X"
            u = 2
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click4():
    try:
        if btn[3]["text"] == " ":
            btn[3]["text"] = "X"
            u = 3
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click5():
    try:
        if btn[4]["text"] == " ":
            btn[4]["text"] = "X"
            u = 4
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click6():
    try:
        if btn[5]["text"] == " ":
            btn[5]["text"] = "X"
            u = 5
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click7():
    try:
        if btn[6]["text"] == " ":
            btn[6]["text"] = "X"
            u = 6
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click8():
    try:
        if btn[7]["text"] == " ":
            btn[7]["text"] = "X"
            u = 7
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click9():
    try:
        if btn[8]["text"] == " ":
            btn[8]["text"] = "X"
            u = 8
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        pass


def click10():
    exit(0)


btn = []
l = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
prop = []
prop = Property(x)
user = []
comp = []
window = 0
turn = 0
n = 0
level = 1
u1 = []
c1 = []


def click11():
    # pop=pop-1
    global level
    global n
    global window
    global u1
    global c1
    if n > 0:
        window.destroy()
        u1.clear()
    n += 1
    window = Tk()
    window.title("Tic-Tac-Toe")
    window.geometry("400x300")
    global turn
    global prop
    global user
    global comp
    global l
    global x
    global btn
    # if a==True:
    #     level+=1
    btn = []
    l = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
    x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
    prop = []
    prop = Property(x)
    user = []
    comp = []
    #    window = 0
    turn = 0
    lb1 = Label(window, text="Level-" + str(level) + "         ", font=("Times New Roman", "20"))
    lb1.grid(row=0, column=0)
    lb1 = Label(window, text="Player: X", font=("Times New Roman", "10"))
    lb1.grid(row=1, column=0)
    lb1 = Label(window, text="Computer: O", font=("Times New Roman", "10"))
    lb1.grid(row=2, column=0)
    btn1 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click1)
    btn1.grid(column=1, row=1)
    btn.append(btn1)
    btn2 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click2)
    btn2.grid(column=2, row=1)
    btn.append(btn2)
    btn3 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click3)
    btn3.grid(column=3, row=1)
    btn.append(btn3)
    btn4 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click4)
    btn4.grid(column=1, row=2)
    btn.append(btn4)
    btn5 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click5)
    btn5.grid(column=2, row=2)
    btn.append(btn5)
    btn6 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click6)
    btn6.grid(column=3, row=2)
    btn.append(btn6)
    btn7 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click7)
    btn7.grid(column=1, row=3)
    btn.append(btn7)
    btn8 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click8)
    btn8.grid(column=2, row=3)
    btn.append(btn8)
    btn9 = Button(window, text=" ", bg="yellow", fg="red", width=3, height=1, font=("Times New Roman", "20"),
                  command=click9)
    btn9.grid(column=3, row=3)
    btn.append(btn9)
    #btn10 = Button(window, text="Close ", bg="red", width=8, height=1, font=("Times New Roman", "10"),
    #               command=click10)
    #btn10.grid(column=0, row=5)
    btn11 = Button(window, text=" Play Again", bg="lightgreen", width=8, height=1, font=("Times New Roman", "10"),
                   command=click11)
    btn11.grid(column=0, row=6)
    window.mainloop()


def click12():
    global level
    level += 1
    click11()


click11()
