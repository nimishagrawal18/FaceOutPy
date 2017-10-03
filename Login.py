
from Tkinter import *
import webcam
def signup():
    rootA = Tk()  # This now makes a new window.
    rootA.geometry("200x250")
    rootA.title('Sign up for new User')  # This makes the window title 'login'

    rootA.configure(background="grey")
    instruction = Label(rootA, text='Please Provide Details\n',
                        font=('arial', 20, 'bold'))  # More labels to tell us what theydo
    instruction.configure(background="grey")
    instruction.pack()  # Blahdy Blah

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

    loginB.pack(ipadx=5, pady=5)

    rootA.mainloop()


def sign():
    global rootA
    rootA.destroy()
    signup()


rootA = Tk()  # This now makes a new window.
rootA.geometry("200x250")
rootA.title('Login')  # This makes the window title 'login'

# C = Canvas(rootA, bg="blue", height=250, width=300)
# bgim=PhotoImage(file="fashion-store.jpg")
# app = Label(rootA,image=bgim)
# app.place(x=0,y=0,relwidth=1,relheight=1)

rootA.configure(background="grey")
intruction = Label(rootA, text='Please Login\n', font=('arial', 20, 'bold'))  # More labels to tell us what they do
intruction.configure(background="grey")
intruction.pack()  # Blahdy Blah

nameL = Label(rootA, text='Username: ')  # More labels
pwordL = Label(rootA, text='Password: ')  # ^

nameEL = Entry(rootA)  # The entry input
pwordEL = Entry(rootA, show='*')
nameL.pack()
nameEL.pack(padx=5)
pwordL.pack()
pwordEL.pack(padx=5)

loginB = Button(rootA, text='Login', relief='groove', command=webcam)
# This makes the login button, which will go to the CheckLogin def.
loginB.pack(ipadx=5, pady=5)

rmuser = Button(rootA, text='New User', fg='blue', relief='groove', command=sign)
# This makes the deluser button. blah go to the deluser def.

rmuser.pack()
rootA.mainloop()
