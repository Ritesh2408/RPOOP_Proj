
from tkinter import*
import tkinter.messagebox as tkMessageBox
import tkinter.ttk as ttk
import csv
import os

import qrcode
import image
import csv

root = Tk()
root.configure(bg="black")
root.title("Metro Station Service")
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
width = 1400
height = 800
x = (screen_width/2) - (width/2)
y = (screen_height/2) - (height/2)
root.geometry('%dx%d+%d+%d' % (width, height, x, y))
root.resizable(0, 0)

def additem():
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get() 
    e5=entry5.get()
    e6=entry6.get()
    e7=entry7.get()
    if entry1.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="" and entry7.get()=="":

        print("Error")
        tkMessageBox.showerror("error","there is issue with some information")

    else:
        result=tkMessageBox.askquestion("Submit","You are about to enter following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 +"\n" + e6 + "\n" + e7)
        entry1.delete(0, END)
        entry2.delete(0, END)
        entry3.delete(0, END)
        entry4.delete(0, END)
        entry5.delete(0, END)
        entry6.delete(0, END)
        entry7.delete(0, END)
        if(result =="yes"):
            print("here")
            with open("data.csv", 'a') as csvfile:
                csvfile.write('{0}, {1}, {2}, {3},{4},{5}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6))
                
               
            csvfile.close()
        else:
            entry1.set("")
            entry2.set("")
            entry3.set("")
            entry4.set("")
            entry5.set("")
            entry6.set("")
            entry7.set("")
def deleteitem():
##    tree.delete(*tree.get_children())
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()
    e7 = entry7.get()
    if entry1.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="" and entry7.get()=="":
        print("Error")
        tkMessageBox.showerror("error","there is issue with some information")
    else:
        result=tkMessageBox.askquestion("Submit","You are about to enter following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)

        if(result =="yes"):
            print("here")
            with open("data.csv", 'r') as f, open("data1.csv",  "w") as w1:
                for line in f:
                    if e1 not in line:
                        w1.write(line)
            os.remove("data.csv")
            os.rename("data1.csv", "data.csv")
            f.close()
            w1.close()
    
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            entry7.delete(0, END)
def updateitem():
    
    e1=entry1.get()
    e2=entry2.get()
    e3=entry3.get()
    e4=entry4.get()
    e5=entry5.get()
    e6=entry6.get()
    e7=entry7.get()
    if entry1.get()=="" and entry2.get()=="" and entry3.get()=="" and entry4.get()=="" and entry5.get()=="" and entry6.get()=="" and entry7.get()=="":

        print("Error")
        tkMessageBox.showerror("error","there is issue with some information")
    else:
        result=tkMessageBox.askquestion("Submit","You are about to update following details\n" + e1 + "\n" + e2 + "\n" + e3 + "\n" + e4 + "\n" + e5 + "\n" + e6)

        if(result =="yes"):
            print("here")
            with open("data.csv","r") as f1 ,open("data1.csv", "w") as working:
                for line in f1:
                    if str(e1) not in line:
                        working.write(line)
                    else:
                        working.write('{0}, {1}, {2}, {3},{4} ,{5}\n'.format(str(e1),e2,e3,str(e4),str(e5),e6))
            os.remove("data.csv")
            os.rename("data1.csv", "data.csv")
            entry1.delete(0, END)
            entry2.delete(0, END)
            entry3.delete(0, END)
            entry4.delete(0, END)
            entry5.delete(0, END)
            entry6.delete(0, END)
            entry7.delete(0, END)
                                      
                                      

def viewitem():
    tree.delete(*tree.get_children())
    with open('data.csv',"r") as f:
        reader = csv.DictReader(f, delimiter=',')
        for row in reader:
            MetroNum=row['MetroNum']
            Name =row['Name']
            StartStation =row['Start Station']
            EndStation=row['End Station']
            StartTime=row['Start Time']
            EndTime = row['End Time']
            Total_Price=row['Total_Price']
            tree.insert("", 0, values=(MetroNum, Name, StartStation, EndStation,StartTime,EndTime,Total_Price))
    f.close()
    txt_result.config(text="Successfully read the data from database", fg="black")
            
  

def clearitem():
    entry1.delete(0, END)
    entry2.delete(0, END)
    entry3.delete(0, END)
    entry4.delete(0, END)
    entry5.delete(0, END)
    entry6.delete(0, END)
    entry7.delete(0, END)

def Ticket():
	with open('data.csv') as file_obj:
	   	reader_obj = csv.reader(file_obj)
	   	for row in reader_obj:
	   		    data = f" Metro Number : {row[0]} \n Name : {row[1]} \n Start Station : {row[2]} \n End Station : {row[3]} \n StartTime : {row[4]} \n Total Price : {row[5]}"

            
		
	#add data to qr code
	qr.add_data(data)
	qr.make(fit=True)

#create an image of qr code
	image = qr.make_image(fill_color="black", back_color= "white")

#save it locally 
	image.save("QR.png")
	print("QR code has been generated successfully!")


MetroNum = StringVar()
Name = StringVar()
StartStation = StringVar()
EndStation = StringVar()
StartTime=StringVar()
EndTime = StringVar()
Total_Price = StringVar()

Top = Frame(root, width=900, height=50 ,bd=8, relief="raise")
Top.pack(side=TOP)
Left = Frame(root, width=200, height=500, bd=8, relief="raise")
Left.pack(side=LEFT)
Right = Frame(root, width=600, height=500,bd=8, relief="raise")
Right.pack(side=RIGHT)
Forms = Frame(Left, width=300, height=450)
Forms.pack(side=TOP)
Buttons = Frame(Left, width=300, height=250, bd=8, relief="raise")
Buttons.pack(side=BOTTOM)

txt_title = Label(Top, width=900, font=('arial', 24),fg='red',text = "Metro station services")
txt_title.pack()
label0 = Label(Forms, text="Metro number:", fg='red',font=('arial', 16), bd=15)
label0.grid(row=0, stick="e")
label1 = Label(Forms, text="Name:",fg='red', font=('arial', 16), bd=15)
label1.grid(row=1, stick="e")
label2 = Label(Forms, text="Start Station",fg='red', font=('arial', 16), bd=15)
label2.grid(row=2, stick="e")
label3 = Label(Forms, text="End station",fg='red', font=('arial', 16), bd=15)
label3.grid(row=3, stick="e")
label4 = Label(Forms, text="StartTime",fg='red', font=('arial', 16), bd=15)
label4.grid(row=4, stick="e")
label6 = Label(Forms, text="EndTime",fg='red', font=('arial', 16), bd=15)
label6.grid(row=6, stick="e")
label5 = Label(Forms, text="Total price:",fg='red', font=('arial', 16), bd=15)
label5.grid(row=5, stick="e")
txt_result = Label(Buttons)
txt_result.pack(side=TOP)

entry1 = Entry(Forms, textvariable=MetroNum, width=30)
entry1.grid(row=0, column=1) 
entry2 = Entry(Forms, textvariable=Name, width=30)
entry2.grid(row=1, column=1)
entry3 = Entry(Forms, textvariable=StartStation, width=30)
entry3.grid(row=2, column=1)
entry4 = Entry(Forms, textvariable=EndStation, width=30)
entry4.grid(row=3, column=1)
entry5 = Entry(Forms, textvariable=StartTime, width=30)
entry5.grid(row=4, column=1)
entry6 = Entry(Forms, textvariable=Total_Price, width=30)
entry6.grid(row=5, column=1)
entry7 = Entry(Forms, textvariable=Total_Price, width=30)
entry7.grid(row=6, column=1)


btn_add = Button(Buttons, width=10,text="ADD",fg="red",bg="white",font=('arial', 10), command=additem)
btn_add.pack(side=LEFT)
btn_delete = Button(Buttons, width=10, text="DELETE",fg="red",font=('arial', 10), command=deleteitem)
btn_delete.pack(side=LEFT)
btn_update = Button(Buttons, width=10, text="UPDATE",fg="red",font=('arial', 10), command=updateitem )
btn_update.pack(side=LEFT)
btn_view = Button(Buttons, width=10, text="VIEW",fg="red",font=('arial', 10), command=viewitem)
btn_view.pack(side=LEFT)
btn_clear = Button(Buttons, width=10, text="CLEAR",fg="red",font=('arial', 10), command=clearitem)
btn_clear.pack(side=LEFT)
btn_tick = Button(Buttons, width=10, text="TICKET",fg="red",font=('arial', 10), command=Ticket)
btn_tick.pack(side=LEFT)


scrollbary = Scrollbar(Right, orient=VERTICAL)
scrollbarx = Scrollbar(Right, orient=HORIZONTAL)
tree = ttk.Treeview(Right, columns=( "MetroNum", "Name", "StartStation", "EndStation","StartTime", "Total_Price"),
                    selectmode="extended", height=500, yscrollcommand=scrollbary.set, xscrollcommand=scrollbarx.set)
scrollbary.config(command=tree.yview)
scrollbary.pack(side=RIGHT, fill=Y)
scrollbarx.config(command=tree.xview)
scrollbarx.pack(side=BOTTOM, fill=X)

tree.heading('MetroNum', text="Number", anchor=W)
tree.heading('Name', text="Name", anchor=W)
tree.heading('StartStation', text="Starting station", anchor=W)
tree.heading('EndStation', text="End station", anchor=W)
tree.heading('StartTime', text="StartTime", anchor=W)
tree.heading('EndTime', text="EndTime", anchor=W)
tree.heading('Total_Price', text="Total price", anchor=W)
tree.column('#0', stretch=NO, minwidth=0, width=0)
tree.column('#1', stretch=NO, minwidth=0, width=100)
tree.column('#2', stretch=NO, minwidth=0, width=150)
tree.column('#3', stretch=NO, minwidth=0, width=150)
tree.column('#4', stretch=NO, minwidth=0, width=100)
tree.column('#5', stretch=NO, minwidth=0, width=100)
tree.column('#6', stretch=NO, minwidth=0, width=100)

tree.pack()
qr = qrcode.QRCode(
version =9,
box_size =7,
border=7)




if(1):
    root.mainloop()
