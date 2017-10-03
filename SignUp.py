import sqlite3
from Tkinter import *
def signup():
    rootA = Tk()  # This now makes a new window.
    rootA.geometry("200x250")
    rootA.title('Sign up for new User')  # This makes the window title 'login'

    rootA.configure(background="grey")
    instruction = Label(rootA, text='Please Provide Details\n', font=('arial', 20, 'bold')) # More labels to tell us what theydo
    instruction.configure(background="grey")
    instruction.pack() # Blahdy Blah

    nameL = Label(rootA, text='New Username: ')  # More labels
    pwordL = Label(rootA, text='New Password: ')  # ^
    pword2 = Label(rootA, text='Confirm Password: ')

    nameEL = Entry(rootA)  # The entry input
    pwordEL = Entry(rootA, show='*')
    pwordE2 = Entry(rootA, show='*')
    nameL.pack()
    nameEL.pack(padx=5)
    pwordL.pack()
    pwordEL.pack(padx=5)
    pword2.pack()
    pwordE2.pack(padx=5)

    loginB = Button(rootA, text='Sign Up', relief='groove')
# This makes the login button, which will go to the CheckLogin def.

    loginB.pack(ipadx=5,pady=5)

    rootA.mainloop()