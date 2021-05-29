from kivy.app import App
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.properties import ListProperty
from kivy.core.window import Window
from kivy.uix.popup import Popup


import random

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
def valcorner(x):
    if 0 in x:
        return 0
    elif 2 in x:
        return 2
    elif 8 in x:
        return 8
    elif 6 in x:
        return 6


def gameover(user, comp):
    global u
    for i in comp:
        if comp.count(i) == 3:
            decision = GridLayout(cols=1, padding=10)
            closeButton = Button(text="You Lose")
            decision.add_widget(closeButton)
            popup = Popup(title='Demo Popup',
                          content=decision)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)
            btn.clear()
            return 0
    for i in user:
        if user.count(i) == 3:
            decision = GridLayout(cols=1, padding=10)
            closeButton = Button(text="You Win")
            decision.add_widget(closeButton)
            popup = Popup(title='Demo Popup',
                          content=decision)
            popup.open()
            closeButton.bind(on_press=popup.dismiss)
            btn.clear()
            nlb = Button(text='Next Level', size=(170, 100), pos=(500, 50))
            nlb.bind(on_press=TicTacToeApp().click12)
            nll = Label(text='')
            nll.add_widget(nlb)
            layout.add_widget(nll)
            return 0
    if turn >= 9:
        decision = GridLayout(cols=1, padding=10)
        closeButton = Button(text="Game Over")
        decision.add_widget(closeButton)
        popup = Popup(title='Demo Popup',
                      content=decision)
        popup.open()
        closeButton.bind(on_press=popup.dismiss)
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
                if btn[a].text == " ":
                    btn[a].text = "O"
                comp.extend(prop[a])
                x.remove(a)
            except:
                decision = GridLayout(cols=1, padding=10)
                closeButton = Button(text="Game Over")
                decision.add_widget(closeButton)
                popup = Popup(title='Demo Popup',
                              content=decision)
                popup.open()
                closeButton.bind(on_press=popup.dismiss)
    elif level == 2:
        if gameover(user, comp) == 1:
            if (attackordefend(comp, x, prop) >= 0):
                a = attackordefend(comp, x, prop)
            elif (attackordefend(user, x, prop) >= 0):
                a = attackordefend(user, x, prop)
            else:
                try:
                    a = random.choice(x)
                except:
                    decision = GridLayout(cols=1, padding=10)
                    closeButton = Button(text="Game Over")
                    decision.add_widget(closeButton)
                    popup = Popup(title='Demo Popup',
                                  content=decision)
                    popup.open()
                    closeButton.bind(on_press=popup.dismiss)
            turn += 2
            try:
                if btn[a].text == " ":
                    btn[a].text = "O"
                comp.extend(prop[a])
                x.remove(a)
            except:
                decision = GridLayout(cols=1, padding=10)
                closeButton = Button(text="Game Over")
                decision.add_widget(closeButton)
                popup = Popup(title='Demo Popup',
                              content=decision)
                popup.open()
                closeButton.bind(on_press=popup.dismiss)
    else:
        if gameover(user, comp) == 1:
            if (attackordefend(comp, x, prop) >= 0):
                a = attackordefend(comp, x, prop)
            elif (attackordefend(user, x, prop) >= 0):
                a = attackordefend(user, x, prop)
            elif (attackordefend(user, x, prop) == -1 and isodd(x, l, u1, prop)):
                a = whichodd(x, l, u1, prop)
            elif (attackordefend(user, x, prop) == -1 and iseven(x, l, u1, prop)):
                a = whicheven(x, l, u1, prop)
            elif (attackordefend(user, x, prop) == -1 and isnone(x, l, u1, prop)):
                a = whichnone(x, l, u1, prop)
            elif (0 in x) or (2 in x) or (6 in x) or (8 in x):
                a=valcorner(x)
            else:
                try:
                    a = x[len(x) - 1]
                except:
                    decision = GridLayout(cols=1, padding=10)
                    closeButton = Button(text="Game Over")
                    decision.add_widget(closeButton)
                    popup = Popup(title='Demo Popup',
                                  content=decision)
                    popup.open()
                    closeButton.bind(on_press=popup.dismiss)
            turn += 2
            try:
                if btn[a].text == " ":
                    btn[a].text = "O"
                comp.extend(prop[a])
                x.remove(a)
            except:
                decision = GridLayout(cols=1, padding=10)
                closeButton = Button(text="Game Over")
                decision.add_widget(closeButton)
                popup = Popup(title='Demo Popup',
                              content=decision)
                popup.open()
                closeButton.bind(on_press=popup.dismiss)
def firstmove(u):
    global turn
    turn += 2
    if u != 4:
        btn[4].text = "O"
        comp.extend(prop[4])
        x.remove(4)
        turn = 2
        c1.append(4)
    else:
        r=random.choice([0,2,6,8])
        btn[r].text = "O"
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


def click1(id):
    try:
        if btn[0].text == " ":
            btn[0].text = "X"
            u = 0
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        print("ErrorHandeled")


def click2(id):
    try:
        if btn[1].text == " ":
            btn[1].text = "X"
            u = 1
            change(u)
            global turn
            if turn == 0:
                firstmove(u)
            else:
                compturn(comp, user, prop, x, u1, c1, l)
        gameover(user, comp)
    except:
        print("ErrorHandeled")


def click3(id):
    try:
        if btn[2].text == " ":
            btn[2].text = "X"
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


def click4(id):
    try:
        if btn[3].text== " ":
            btn[3].text = "X"
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


def click5(id):
    try:
        if btn[4].text == " ":
            btn[4].text = "X"
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


def click6(id):
    try:
        if btn[5].text == " ":
            btn[5].text = "X"
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


def click7(id):
    try:
        if btn[6].text == " ":
            btn[6].text = "X"
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


def click8(id):
    try:
        if btn[7].text == " ":
            btn[7].text = "X"
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


def click9(id):
    try:
        if btn[8].text == " ":
            btn[8].text = "X"
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
layout=None
class TicTacToeApp(App):
    def __init__(self):
        App.__init__(self)

    def click11(self,id):
        return self.run()

    def click12(self,id):
        global level
        level+=1
        return self.run()
    def ttt_layout(self):
        global layout
        global level
        global n
        global u1
        global c1
        if n > 0:
            layout.clear_widgets()
            u1.clear()
        n += 1
        global turn
        global prop
        global user
        global comp
        global l
        global x
        global btn
        btn = []
        l = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]
        x = [0, 1, 2, 3, 4, 5, 6, 7, 8]
        prop = []
        prop = Property(x)
        user = []
        comp = []
        turn = 0
        layout = GridLayout(cols=3)
        layout.add_widget(Label(text='LEVEL-' + str(level)))
        layout.add_widget(Label(text=''))
        layout.add_widget(Label(text='You: X \n\nComputer: O'))

        btn1 = Button(text=' ')
        layout.add_widget(btn1)
        btn.append(btn1)
        btn1.bind(on_press=click1)

        btn2 = Button(text=' ')
        layout.add_widget(btn2)
        btn.append(btn2)
        btn2.bind(on_press=click2)

        btn3 = Button(text=' ')
        layout.add_widget(btn3)
        btn.append(btn3)
        btn3.bind(on_press=click3)

        btn4 = Button(text=' ')
        layout.add_widget(btn4)
        btn.append(btn4)
        btn4.bind(on_press=click4)

        btn5 = Button(text=' ')
        layout.add_widget(btn5)
        btn.append(btn5)
        btn5.bind(on_press=click5)

        btn6 = Button(text=' ')
        layout.add_widget(btn6)
        btn.append(btn6)
        btn6.bind(on_press=click6)

        btn7 = Button(text=' ')
        layout.add_widget(btn7)
        btn.append(btn7)
        btn7.bind(on_press=click7)

        btn8 = Button(text=' ')
        layout.add_widget(btn8)
        btn.append(btn8)
        btn8.bind(on_press=click8)

        btn9 = Button(text=' ')
        layout.add_widget(btn9)
        btn.append(btn9)
        btn9.bind(on_press=click9)

        pab = Button(text='Play Again', size=(170, 100), pos=(50, 50))
        pab.bind(on_press=self.click11)
        pal = Label(text='')
        pal.add_widget(pab)
        layout.add_widget(pal)
        return layout

    def build(self):
        Window.size = (360, 640)
        Window.minimum_width, Window.minimum_height = (360, 640)

        return self.ttt_layout()





def start():
    TicTacToeApp().run()

start()