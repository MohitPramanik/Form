import tkinter as tk
import tkinter.messagebox as tmsg
import string
import re
import pymongo

root = tk.Tk()

# root.geometry('520x300')
# root.maxsize(520, 260)
root.minsize(520, 302)
root.title("Registration Form")

def check(): 
    # for email address
    if not re.match(r"[^@]+@[^@]+\.[^@]+",emailval.get()):
        tmsg.showerror('Error', "Please use a valid email address")

    # for password
    elif len(passval.get()) < 8:
        tmsg.showwarning('Warning', "The password must contain at least 8 characters") 
    elif not any(char in string.ascii_uppercase for char in passval.get()) or not any(char in string.ascii_lowercase for char in passval.get()) or not any(char in '0123456789' for char in passval.get()) or not any(char in string.punctuation for char in passval.get()):
         tmsg.showwarning('Warning', "The password must contain an uppercase letter, a lowercase letter, a number and a special character in it")
    else:
         return True     


def submit():
    if check():
        client = pymongo.MongoClient("mongodb://localhost:27017") # to connect mongoDB to python
        db = client['my_app_registration']
        collection = db['python']
        insertData = {'name' : nameval.get(), 'email' : emailval.get(), 'gender' : genderval.get(),'age' : ageval.get(),'password' : passval.get()}
        collection.insert_one(insertData)
        tmsg.showinfo("Message", "Your data is successfully submitted")

frame = tk.Frame(root, bd=2, relief='solid', bg='lightgrey')
frame.pack(pady=40)

# value storage variables
nameval = tk.StringVar()
emailval = tk.StringVar()
genderval = tk.StringVar()
genderval.set("none")
ageval = tk.IntVar()
passval = tk.StringVar()
# passval = tk.StringVar()

# items to be displayed
heading=tk.Label(frame, text="Registration Form", font="comicsansns 18 bold italic", bg='yellow', fg='blue', width=33, pady=10)
name = tk.Label(frame, text="Full Name", font='comicsansns 10', width=10, bg="lightgrey")
email = tk.Label(frame, text="Email", font='comicsansns 10', width=10, bg="lightgrey")
gender = tk.Label(frame, text="Gender", font='comicsansns 10', width=10, bg="lightgrey")
age = tk.Label(frame, text="Age", font='comicsansns 10', width=10, bg="lightgrey")
password = tk.Label(frame, text="Password", font='comicsansc 10', width=10, bg='lightgrey')

heading.grid(row = 0, pady=(0, 20), columnspan=4)
name.grid(row=1, column=0, padx=40, pady=8)
email.grid(row=2, column=0, padx=40, pady=8)
gender.grid(row=3, column=0, padx=40, pady=8)
age.grid(row=4, column=0, padx=40, pady=8)
password.grid(row=5, column=0, padx=40, pady=8)

nameEntry = tk.Entry(frame, textvariable=nameval, width=40, bd=1, relief='groove', justify='center', font='comicsansns 10')
emailEntry = tk.Entry(frame, textvariable=emailval, width=40, bd=1, relief='groove', justify='center', font='comicsansns 10')
genderMale = tk.Radiobutton(frame, text="Male", variable=genderval, value = 'male', font='comicsansns 10', bg="lightgrey", activebackground='lightgrey')
genderFemale = tk.Radiobutton(frame, text="Female", variable=genderval, value = 'female', font='comicsansns 10', bg="lightgrey", activebackground='lightgrey')
genderOther = tk.Radiobutton(frame, text="Other", variable=genderval, value = 'other', font='comicsansns 10', bg="lightgrey", activebackground='lightgrey')
ageEntry = tk.Entry(frame, textvariable=ageval, width=40, bd=1, relief='groove', justify='center', font='comicsansns 10')
passEntry = tk.Entry(frame, textvariable=passval, show='*', width=40, bd=1, relief='groove', justify='center', font='comicsansns 10 bold')

submitBtn = tk.Button(frame, text='Submit', bg='brown', fg='white', font='Helvetica 10 bold', activebackground='green', activeforeground='white', bd=1, relief='sunken', pady=4, padx=30, command=submit)

nameEntry.grid(row=1, column=1,columnspan=3, ipady=3, pady=2, padx=16)
emailEntry.grid(row=2, column=1,columnspan=3, ipady=3, pady=2, padx=16)
genderMale.grid(row=3, column=1)
genderFemale.grid(row=3, column=2)
genderOther.grid(row=3, column=3)
ageEntry.grid(row=4, column=1,columnspan=3, ipady=3, pady=2, padx=16)
passEntry.grid(row=5, column=1,columnspan=3, ipady=3, pady=2, padx=16)
submitBtn.grid(row = 6, column=0, columnspan=4, pady=20, ipadx=20)

root.eval('tk::PlaceWindow . center')
root.mainloop()