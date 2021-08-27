import tkinter as tk
from tkinter import *
import random
import string
import os
from pathlib import Path
#XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
state = 0
state_Lower  = 0
state_Numbers = 0
state_Symbols = 0
lengt = 0
OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / Path("./images")

def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


class PassV2:
    def __init__(self):
        self.app = tk.Tk()
        self.app.geometry('533x727')
        self.app.configure(bg='#0A0E31')
        self.app.title('PassV2')
        self.app.overrideredirect(True)
        self.app.bind("<ButtonPress-1>", self.StartMove)
        self.app.bind("<B1-Motion>", self.OnMotion)
        self.pass_filed= ''
        self.image_off = tk.PhotoImage(file = relative_to_assets('off.png'))
        self.image_on = tk.PhotoImage(file = relative_to_assets('on.png'))
        self.window = Canvas(
            self.app,
            bg = '#0A0E31',
            height = 727,
            width = 533,
            bd = 0,
            highlightthickness = 0,
            relief = 'ridge'
        )
        self.window.place(x = 0, y = 0)
        self.current_value = tk.DoubleVar()
        self.creat_backroundd = self.creat_backround()
        self.textes = self.Creat_Text()
        self.creat_buttons = self.creat_button()
        self.creat_check_btns = self.creat_check_btn()
        self.creat_label = self.creat_labels()
        self.length_optin = self.length_optins()
        self.passwordd = self.Password()

    def StartMove(self, event):
        self.x = event.x
        self.y = event.y

    def OnMotion(self, event):
        deltax = event.x - self.x
        deltay = event.y - self.y
        x = self.app.winfo_x() + deltax
        y = self.app.winfo_y() + deltay
        self.app.geometry("+%s+%s" % (x, y))
        print(self.app.geometry())

    def creat_backround(self):
        backround_upper = tk.PhotoImage(file = relative_to_assets('entry1.png'))
        backround_upper_place = self.window.create_image(
            260,
            350,
            image = backround_upper
        )
        backround_lower = tk.PhotoImage(file = relative_to_assets('entry1.png'))
        backround_lower_place = self.window.create_image(
            260,
            420,
            image = backround_lower
        )
        backround_number = tk.PhotoImage(file = relative_to_assets('entry1.png'))
        backround_number_place = self.window.create_image(
            260,
            490,
            image = backround_number
        )
        backround_symbols = tk.PhotoImage(file = relative_to_assets('entry1.png'))
        backround_symbols_place = self.window.create_image(
            260,
            560,
            image = backround_symbols
        )
        backround_pass = tk.PhotoImage(file = relative_to_assets('entry_1.png'))
        backround_pass_place = self.window.create_image(
            260,
            150,
            image = backround_pass
        )
        backround_length = tk.PhotoImage(file = relative_to_assets('entry1.png'))
        backround_pass_place = self.window.create_image(
            260,
            260,
            image = backround_length
        )
        return backround_upper, backround_lower, backround_number, backround_symbols,backround_length,backround_pass

    def Creat_Text(self):
        self.window.create_text(19,31,anchor="nw",text="Password Generator",fill="#FFFFFF",font=("Montserrat",  40 * -1, "bold"))
        self.window.create_text(75,335,anchor="nw",text="Include Uppercase",fill="#FFFFFF",font=("Roboto",  25 * -1))
        self.window.create_text(75,405,anchor="nw",text="Include Lowercase",fill="#FFFFFF",font=("Roboto",  25 * -1))
        self.window.create_text(75,475,anchor="nw",text="Include Numbers",fill="#FFFFFF",font=("Roboto",  25 * -1))
        self.window.create_text(75,545,anchor="nw",text="Include Symbols",fill="#FFFFFF",font=("Roboto",  25 * -1))
        self.window.create_text(46, 210,anchor="nw",text="LENGTH:",fill="#797B8E",font=("Roboto",  15 * -1))
        self.window.create_text(46, 300,anchor="nw",text="SETTING",fill="#797B8E",font=("Roboto",  15 * -1))

    def creat_button(self):
        button_image_1 = tk.PhotoImage(
            file = relative_to_assets('Button.png')
        )
        button_1 = tk.Button(
            image=button_image_1,
            borderwidth=0,
            highlightthickness=0,
            command=self.Password,
            relief='flat',
            bg='red',
            cursor="hand2"
        )
        button_1.place(
            x=46.0,
            y=630.0,
            width=441.0,
            height=63.0
        )
        return button_image_1

    def update_up(self, *args):
        global lengt
        lengt += 4
        self.length_num.config(text=lengt)

    def update_down(self, *args):
        global lengt
        lengt -= 4
        self.length_num.config(text=lengt)

    def length_optins(self):
        self.length_num = Label(self.window, text = '', font=("Roboto",  17 * -1, 'bold'), height=1, width=2, bg='#0A0E31', fg='white')
        self.length_num.place(x= 113,y= 206)

        self.length_upper = Label(self.window, text = '32', font=("Roboto",  22 * -1, 'bold'), height=1, width=2, bg='#1D2141', fg='white', cursor='hand2')
        self.length_upper.bind('<Button-1>', self.update_up)
        self.length_upper.place(x= 435, y= 245)


        self.length_lower = Label(self.window, text = '4', font=("Roboto",  22 * -1, 'bold'), height=1, width=2, bg='#1D2141', fg='white', cursor='hand2')
        self.length_lower.bind('<Button-1>', self.update_down)
        self.length_lower.place(x=50, y=245)

    def creat_check_btn(self):
        self.copy = Label(self.window, text = 'Click to copy', font=("Roboto",  15 * -1), height=1, width=9, bg='#1D2141', fg='#797B8E', cursor='hand2')
        self.copy.bind('<Button-1>', self.addToClipBoard)
        self.copy.place(x=390, y=161)

        self.winbtntest_Upper = Label(self.app, image=self.image_off, bg='#1D2141', height=45, cursor="hand2")
        self.winbtntest_Upper.bind('<Button-1>', self.Upper)
        self.winbtntest_Upper.place(x= 392, y = 327)

        self.winbtntest_Lower = Label(self.app, image=self.image_off, bg='#1D2141', height=45, cursor="hand2")
        self.winbtntest_Lower.bind('<Button-1>', self.Lower)
        self.winbtntest_Lower.place(x= 392, y = 397)

        self.winbtntest_Numbers = Label(self.app, image=self.image_on, bg='#1D2141', height=45, cursor="no")
        #self.winbtntest_Numbers.bind('<Button-1>', self.Numbers)
        self.winbtntest_Numbers.place(x= 392, y = 467)

        self.winbtntest_Symbols = Label(self.app, image=self.image_off, bg='#1D2141', height=45, cursor="hand2")
        self.winbtntest_Symbols.bind('<Button-1>', self.Symbols)
        self.winbtntest_Symbols.place(x= 392, y = 537)

    def Upper(self, event):
        global state
        if state == 1:
            print('upper off')
            self.winbtntest_Upper.config(image=self.image_off)
            state = 0
        else:
            print('upper on')
            self.winbtntest_Upper.config(image=self.image_on)
            state = 1
    def Lower(self, event):
        global state_Lower
        if state_Lower == 1:
            print('lower off')
            self.winbtntest_Lower.config(image=self.image_off)
            state_Lower = 0
        else:
            print('lower on')
            self.winbtntest_Lower.config(image=self.image_on)
            state_Lower = 1
    def Numbers(self, event):
        global state_Numbers
        if state_Numbers == 1:
            print('number off')
            self.winbtntest_Numbers.config(image=self.image_off)
            state_Numbers = 0
        else:
            print('number on')
            self.winbtntest_Numbers.config(image=self.image_on)
            state_Numbers = 1
    def Symbols(self, event):
        global state_Symbols
        if state_Symbols == 1:
            print('symbols off')
            self.winbtntest_Symbols.config(image=self.image_off)
            state_Symbols = 0
        else:
            print('symbols on')
            self.winbtntest_Symbols.config(image=self.image_on)
            state_Symbols = 1

    def creat_labels(self):
        self.pass_filed = Label(self.app, text=self.pass_filed, bg='#1D2141', fg='white', font=('Montserrat', 20 * -1))
        self.pass_filed.place(x=60,y=135)
        return self.pass_filed

    def Password(self):
        global state
        global state_Lower
        global state_Numbers
        global state_Symbols
        self.length = self.length_num.cget('text')
        self.Uppercase = string.ascii_uppercase
        self.Lowercase = string.ascii_lowercase
        self.RandomNumber = str(random.randrange(1, 99999))
        self.RandomCodes = '!@#$%^&*()_-+={}[]'
        if state == 1:
            RandomWord_Upper = (''.join(random.choice(self.Uppercase) for i in range(30)) )
            resualte_upper = RandomWord_Upper+self.RandomNumber
            resualte_Upper = (''.join(random.choice(resualte_upper) for i in range(self.length)))
            self.pass_filed.config(text = resualte_Upper)

        if state_Lower == 1:
            RandomWord_Lower = (''.join(random.choice(self.Lowercase) for i in range(30)) )
            resualte_lower = RandomWord_Lower+self.RandomNumber
            resualte_Lower = (''.join(random.choice(resualte_lower) for i in range(self.length)))
            self.pass_filed.config(text = resualte_Lower)

        if state == 1 and state_Lower == 1:
            RandomWord_Upperx = (''.join(random.choice(self.Uppercase) for i in range(30)) )
            RandomWord_Lowerx = (''.join(random.choice(self.Lowercase) for i in range(30)) )
            resualte_upper_lower = RandomWord_Upperx+RandomWord_Lowerx+self.RandomNumber
            resualte_Upper_Lower = (''.join(random.choice(resualte_upper_lower) for i in range(self.length)))
            self.pass_filed.config(text = resualte_Upper_Lower)

        if state_Symbols == 1:
            RandomSymbols = (''.join(random.choice(self.RandomCodes) for i in range(30)) )
            resualte_symbols = RandomSymbols+self.RandomNumber
            resualte_Symbols = (''.join(random.choice(resualte_symbols) for i in range(self.length)))
            self.pass_filed.config(text = resualte_Symbols)
        
        if state == 1 and state_Symbols == 1:
            RandomWord_Upper_s = (''.join(random.choice(self.Uppercase) for i in range(30)) )
            RandomSymbols_s = (''.join(random.choice(self.RandomCodes) for i in range(30)) )
            resualte_symbols_upper = RandomWord_Upper_s+RandomSymbols_s+self.RandomNumber
            resualte_Symbols_Upper = (''.join(random.choice(resualte_symbols_upper) for i in range(self.length)))
            self.pass_filed.config(text = resualte_Symbols_Upper)

        if state_Lower == 1 and state_Symbols == 1:
            RandomSymbols_l = (''.join(random.choice(self.RandomCodes) for i in range(30)) )
            RandomWord_Lower_l = (''.join(random.choice(self.Lowercase) for i in range(30)) )
            resualte_symbols_lower = RandomSymbols_l+RandomWord_Lower_l+self.RandomNumber
            resualte_Symbols_Lower = (''.join(random.choice(resualte_symbols_lower) for i in range(self.length)))
            self.pass_filed.config(text = resualte_Symbols_Lower)

        if state == 1 and state_Lower == 1 and state_Symbols == 1:
            RandomSymbols_A = (''.join(random.choice(self.RandomCodes) for i in range(30)) )
            RandomWord_Lower_A = (''.join(random.choice(self.Lowercase) for i in range(30)) )
            RandomWord_Upper_A = (''.join(random.choice(self.Uppercase) for i in range(30)) )
            resualte_a = RandomSymbols_A+RandomWord_Lower_A+RandomWord_Upper_A+self.RandomNumber
            resualte_A = (''.join(random.choice(resualte_a) for i in range(self.length)))
            self.pass_filed.config(text = resualte_A)

    def addToClipBoard(self, *args):
        text = self.pass_filed.cget('text')
        command = 'echo ' + text.strip() + '| clip'
        os.system(command)

    def run(self):
        self.app.mainloop()

if __name__ == "__main__":
    calc = PassV2()
    calc.run()