from tkinter import *


# class Buttons:
#
#     def __init__(self, master):
#         frame = Frame(master)
#         frame.pack()
#
#         self.printButton = Button(frame, text = "Print message", command = self.printMessage)
#         self.printButton.pack(side = LEFT)
#
#         self.quitButton = Button(frame, text = "Quit", command = frame.quit)
#         self.quitButton.pack(side = LEFT)
#
#     def printMessage(self):
#         print("wow, worked")

#Various functions

# Function is called when LOGIN Button is pressed
def login():
    label_correct_password.pack_forget()
    label_incorrect_password.pack_forget()
    all_passcode_entries = typed.get() # Type conversion to an array
    if all_passcode_entries == "12345":
        label_correct_password.pack()
    else:
        label_incorrect_password.pack()
    print(all_passcode_entries)


# Global variable to store the passcode entries while logging in
all_passcode_entries = []


# This is to create a blank window which inculdes title bar buttons (close, minimise and restore button)
root = Tk()
root.geometry('600x600+700+300')
root.config(bg = "white")


# Local string variable to store the entered passcode
typed = StringVar()

# Frame 1 consists of the name XYZ 
frame1 = Frame(root)
label1 = Label(frame1, text = "XYZ",bg = "white", fg = "black", font=("XYZ", 40))
frame1.config(bg = "white")
frame1.pack(fill = BOTH)
label1.pack(fill = BOTH)

# Frame 2 consists of text "Passcode" and entry box
frame2 = Frame(root)
frame2.pack(side=TOP, expand = 1)
frame2.config(bg = "white")
label2 = Label(frame2, text = "Passcode", bg = "white")
entry2 = Entry(frame2, textvariable = typed)
label2.pack(fill = BOTH)
entry2.pack(fill = BOTH)
check = Checkbutton(frame2, text = "Keep me logged in", fg = "black", bg = "white")
check.pack()

# Frame 3 consists of all the buttons from 0 to 9, * and #
frame3 = Frame(root)
frame3.pack(side=TOP, expand = 1)
frame3.config(bg = "white")
button1 = Button(frame3, text = "1", fg = "white", bg = "black")
button2 = Button(frame3, text = "2", fg = "white", bg = "black")
button3 = Button(frame3, text = "3", fg = "white", bg = "black")
button4 = Button(frame3, text = "4", fg = "white", bg = "black")
button5 = Button(frame3, text = "5", fg = "white", bg = "black")
button6 = Button(frame3, text = "6", fg = "white", bg = "black")
button7 = Button(frame3, text = "7", fg = "white", bg = "black")
button8 = Button(frame3, text = "8", fg = "white", bg = "black")
button9 = Button(frame3, text = "9", fg = "white", bg = "black")
button0 = Button(frame3, text = "0", fg = "white", bg = "black")
button11 = Button(frame3, text = "*", fg = "white", bg = "black")
button12 = Button(frame3, text = "C", fg = "white", bg = "black")
button1.grid(row = 2, column = 0)
button2.grid(row = 2, column = 1)
button3.grid(row = 2, column = 2)
button4.grid(row = 3, column = 0)
button5.grid(row = 3, column = 1)
button6.grid(row = 3, column = 2)
button7.grid(row = 4, column = 0)
button8.grid(row = 4, column = 1)
button9.grid(row = 4, column = 2)
button11.grid(row = 5, column = 0)
button0.grid(row = 5, column = 1)
button12.grid(row = 5, column = 2)

# Frame 4 consists of enter button
frame4 = Frame(root)
frame4.pack(side=RIGHT)
label_correct_password = Label(frame2, text = "Passcode correct", fg = "green", bg = "white")
label_incorrect_password = Label(frame2, text = "Passcode Incorrect", fg = "red", bg = "white")
button_enter = Button(frame4, text = "LOGIN", fg = "white", bg = "blue", command = login)
button_enter.pack(fill = BOTH)





# frame1 = Frame(root, bg = "white")
# frame1.pack(side=TOP, fill = X, expand = 2)
#
# frame2 = Frame(root, bg = "white")
# frame2.pack(side=TOP, fill = X, expand = 2)
#
# frame3 = Frame(root, bg = "white")
# frame3.pack(side = TOP, fill = X, expand = 2)
#
# frame4 = Frame(root, bg = "white")
# frame4.pack(side = TOP, fill = X, expand = 2)
#
# operatore_mode_button = Button(frame1, text = "MODE 1",fg = "white", bg = "blue")
# maintenance_mode_button = Button(frame2, text = "MODE 2",fg = "white", bg = "orange")
# engineer_mode_button = Button(frame3, text = "MODE 3",fg = "white", bg = "green")
# exit_button = Button(frame4, text = "EXIT",fg = "black", bg = "red")
#
# operatore_mode_button.pack()
# maintenance_mode_button.pack()
# engineer_mode_button.pack()
# exit_button.pack(side = RIGHT)






# one = Label(root, text = "One", bg = "red", fg = "white")
# one.pack(fill = X)
# two = Label(root, text = "two", bg = "green", fg = "black")
# two.pack(fill = X)
# three = Label(root, text = "three", bg = "blue", fg = "white")
# three.pack(side = LEFT, fill = Y)


# to put the above program in continuous loop
root.mainloop()
