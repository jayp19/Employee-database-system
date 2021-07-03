from tkinter import *
from tkinter import messagebox
import mysql.connector
window=Tk()

def takedata():
    id1 = id.get()
    nam = Name.get()
    pos = Post.get()
    g = gender.get()
    if (id1 == "" or nam == "" or pos == "" or g == ""):
        messagebox.showerror("Enter","All filds are required!!!")
    else:
        mydb = mysql.connector.connect(host="localhost", user="Jay", passwd="4321", db="Emp")
        mycursor = mydb.cursor()
        mycursor.execute("INSERT INTO Emps(id,name,post,gender) VALUES(%s,%s,%s,%s)",
                         (id1,nam,pos,g))
        id.delete(0,END)
        Name.delete(0, END)
        Post.delete(0, END)
        gender.delete(0, END)
        mydb.commit()
        mydb.close()
        refresh()

def delete():
    id1=id.get()
    if(id1==""):
        messagebox.showerror("Delete", "ID is required!!!")
    else:
        mydb = mysql.connector.connect(host="localhost", user="Jay", passwd="4321", db="Emp")
        mycursor = mydb.cursor()
        mycursor.execute("DELETE FROM emps WHERE id='"+id.get()+"'")
        id.delete(0, END)
        Name.delete(0, END)
        Post.delete(0, END)
        gender.delete(0, END)
        mydb.commit()
        mydb.close()
        refresh()

def update():
    id1=id.get()
    n=Name.get()
    p=Post.get()
    g=gender.get()
    mydb = mysql.connector.connect(host="localhost", user="Jay", passwd="4321", db="Emp")
    mycursor = mydb.cursor()
    if (id1 == "" or n == "" or p == "" or g == ""):
        messagebox.showerror("update","All filds are required!!!")
    else:
        mydb = mysql.connector.connect(host="localhost", user="Jay", passwd="4321", db="Emp")
        mycursor = mydb.cursor()
        mycursor.execute("UPDATE emps SET name='" + n + "',post='"+p+"',gender='"+g+"' WHERE id='"+id1+"'")
        id.delete(0, END)
        Name.delete(0, END)
        Post.delete(0, END)
        gender.delete(0, END)
        mydb.commit()
        mydb.close()
        refresh()

def search():
    id1 = id.get()
    if (id1 == ""):
        messagebox.showerror("Search", "ID is required!!!")
    else:
        mydb = mysql.connector.connect(host="localhost", user="Jay", passwd="4321", db="Emp")
        mycursor = mydb.cursor()
        mycursor.execute("SELECT * FROM emps WHERE id='"+id.get()+"'")
        rows=mycursor.fetchall()
        #if(int(id1) > len(rows) or int(id1)<0):
         #   messagebox.showerror("Search", " ID not found!!!")
        #else:
        for row in rows:
            Name.insert(0, row[1])
            Post.insert(0, row[2])
            gender.insert(0, row[3])
        mydb.close()
        refresh()

def clear():
    id.delete(0, END)
    Name.delete(0, END)
    Post.delete(0, END)
    gender.delete(0, END)

def refresh():
    list.delete(0,END)
    mydb = mysql.connector.connect(host="localhost", user="Jay", passwd="4321", db="Emp")
    mycursor = mydb.cursor()
    mycursor.execute("SELECT * FROM emps")
    rows = mycursor.fetchall()
    for row in rows:
        insertData=str(row[0])+'     '+row[1]+'     '+row[2]+'     '+row[3]
        list.insert(list.size()+1,insertData)

window.title("Project")
window.geometry("550x300")
window.configure(bg="black")
lb=Label(window,text="Employee Database Management",bg="red",font=("arial",12,"bold")).place(x=100)
label1=Label(window,text="ID:",bg="black",fg="White",font=("arial",12,"bold"))
label1.place(x=8,y=25)
label2=Label(window,text="Name:",bg="black",fg="White",font=("arial",12,"bold"))
label2.place(x=75,y=25)
label3=Label(window,text="Post:",bg="black",fg="White",font=("arial",12,"bold"))
label3.place(x=145,y=25)
label4=Label(window,text="Gender:",bg="black",fg="White",font=("arial",12,"bold"))
label4.place(x=215,y=25)

id=Entry(window,width=10)
id.place(x=10,y=50)
Name=Entry(window,width=10)
Name.place(x=80,y=50)
Post=Entry(window,width=10)
Post.place(x=150,y=50)
gender=Entry(window,width=10)
gender.place(x=220,y=50)

button1=Button(window,text="Enter",fg="white",bg="blue",font=("arial",12,"bold"),command=takedata)
button1.place(x=10,y=100)
button2=Button(window,text="Delete",fg="white",bg="blue",font=("arial",12,"bold"),command=delete)
button2.place(x=100,y=100)
button3=Button(window,text="Update by ID",fg="white",bg="blue",font=("arial",12,"bold"),command=update)
button3.place(x=200,y=100)
button4=Button(window,text="Exit",fg="white",bg="blue",font=("arial",12,"bold"),command=window.destroy)
button4.place(x=235,y=150)
button5=Button(window,text="Search by ID",fg="white",bg="blue",font=("arial",12,"bold"),command=search)
button5.place(x=30,y=150)
button6=Button(window,text="Clear All",fg="white",bg="blue",font=("arial",12,"bold"),command=clear)
button6.place(x=150,y=150)

list=Listbox(window,width=25)
list.place(x=380,y=20)
refresh()

window.mainloop()