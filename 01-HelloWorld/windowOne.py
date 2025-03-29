import sys
from tkinter import *

def welcome():
    print('How Are You?')

def terminated():
    print('Exiting from Program')

rootwindow = Tk()
rootwindow.title('Hemant Ganesh Kshirsagar')

bOne = Button(rootwindow)
bOne.configure(text = 'Welcome', command = welcome)
bOne.grid(row = 1, column = 1, sticky = E)

bTwo = Button(rootwindow)
bTwo.configure(text = 'Exit', command = terminated)
bTwo.grid(row = 2, column = 1, sticky = E)

rootwindow.mainloop()


