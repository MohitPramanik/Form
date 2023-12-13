import tkinter as tk
import tkinter.messagebox as tmsg
import re
import string
import pymongo

root = tk.Tk()

root.minsize(520, 302)
root.title("Login Form")

def submit():
    with open("registration.txt", 'r') as f:
        client = pymongo.MongoClient("mongodb://localhost:27017") # to connect mongoDB to python
        db = client['my_app_registration']
        collection = db['python']

        data = collection.find_one({'email' : emailval.get(), 'password': passval.get()}, {'_id':0})
        if(data != None):
            print(f'Name   : {data["name"]} \nEmail  : {data["email"]} \nAge    : {data["age"]} \nGender : {data["gender"]}' )
            tmsg.showinfo("Message", "Your data is present and is printed to terminal")
        else:
            tmsg.showinfo("Message", "Data not found.")


frame = tk.Frame(root, bd=2, relief='solid', bg='lightgrey')
frame.pack(pady=40)

# value storage variables
emailval = tk.StringVar()
passval = tk.StringVar()

# items to be displayed
heading=tk.Label(frame, text="Login Form", font="comicsansns 18 bold italic", bg='yellow', fg='blue', width=33, pady=10)
email = tk.Label(frame, text="Email", font='comicsansns 10', width=10, bg="lightgrey")
password = tk.Label(frame, text="Password", font='comicsansc 10', width=10, bg='lightgrey')

heading.grid(row = 0, pady=(0, 20), columnspan=4)
email.grid(row=2, column=0, padx=40, pady=8)
password.grid(row=5, column=0, padx=40, pady=8)

emailEntry = tk.Entry(frame, textvariable=emailval, width=40, bd=1, relief='groove', justify='center', font='comicsansns 10')
passEntry = tk.Entry(frame, textvariable=passval, show='*', width=40, bd=1, relief='groove', justify='center', font='comicsansns 10 bold')

submitBtn = tk.Button(frame, text='Submit', bg='brown', fg='white', font='Helvetica 10 bold', activebackground='green', activeforeground='white', bd=1, relief='sunken', pady=4, padx=30, command=submit)

emailEntry.grid(row=2, column=1,columnspan=3, ipady=3, pady=2, padx=16)
passEntry.grid(row=5, column=1,columnspan=3, ipady=3, pady=2, padx=16)
submitBtn.grid(row = 6, column=0, columnspan=4, pady=20, ipadx=20)

root.eval('tk::PlaceWindow . center')
root.mainloop()