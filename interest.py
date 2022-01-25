from tkinter import *

window = Tk()

window.title('Simple Interest Calculator')
window.geometry("500x500")
window.configure(bg='lightcyan')

def calculate_interest():
    principal = float(principal_entry.get())
    rate = float(rate_entry.get())
    time = float(time_entry.get())
    interest = (principal*rate*time)/100
    interest = round(interest,2)
    name = username.get()
    result_label.destroy()

    output_msg = Label(result_frame,text=name+", your simple interest is Rs. "+str(interest),bg="lightcyan",font=("Calibri",15),width=42)
    output_msg.place(x=20,y=40)
    output_msg.pack()

heading_label= Label(window,text="SIMPLE INTEREST CALCULATOR",fg="black",bg="lightcyan",font=("Calibri",20),bd=5)
heading_label.place(x=50,y=20)

enter_name = Label(window,text="Enter your name",fg="black",bg="lightcyan",font=("Calibri",15))
enter_name.place(x=25, y=92)

username = Entry(window,text="",bd=2,width=22)
username.place(x=250,y=95)

principal_label = Label(window,text="Enter the principal (in Rs.)",fg="black",bg="lightcyan",font=("Calibri",15))
principal_label.place(x=25,y=150)

principal_entry = Entry(window,text="",bd=2,width=22)
principal_entry.place(x=250, y=155)

rate_label = Label(window,text="Enter the rate (in %)",fg="black",bg="lightcyan",font=("Calibri",15))
rate_label.place(x=25, y=200)

rate_entry = Entry(window,text="",bd=2,width=22)
rate_entry.place(x=250, y=205)

time_label = Label(window,text="Enter the time (in years)",fg="black",bg="lightcyan",font=("Calibri",15))
time_label.place(x=25, y=250)

time_entry = Entry(window,text="",bd=2,width=22)
time_entry.place(x=250, y=250)

calculate_button = Button(window,text="Calculate",fg="black",bg="cyan",bd=4,command=calculate_interest)
calculate_button.place(x=20,y=300)

result_frame = LabelFrame(window,text="Result",bg="lightcyan",font=("Calibri",20))
result_frame.pack(padx=20,pady=20)
result_frame.place(x=20,y=350)

result_label = Label(result_frame,text=" Your result will be displayed here ",bg="lightcyan",font=("Calibri",20),width=33)
result_label.place(x=20,y=20)
result_label.pack()

window.mainloop()