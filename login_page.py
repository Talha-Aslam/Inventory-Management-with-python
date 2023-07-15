from tkinter import *
import tkinter.messagebox as tmsg
from tkinter.ttk import Labelframe, Treeview
import sqlite3
import ast
import os

def click(event):
    username = value.get()
    password = passw.get()
    if username == "":
        tmsg.showerror("Missing Information" , "Please enter the username!")
        user_name_E.delete(0,END)
        user_pass_E.delete(0,END)
    if password == "":
        tmsg.showerror("Missing Information" , "Please enter the password!")
        user_name_E.delete(0,END)
        user_pass_E.delete(0,END)
    if username.lower() == "admin" and password == "55555":
        user_name_E.delete(0,END)
        user_pass_E.delete(0,END)
        def inventry(event):
            hide_all_frame()
            valdisp_f.place(x = 95 , y = 60)
            show_hed_inv = Label(valdisp_f,text = "Showing Items in inventry:" , bg = "grey" , fg = "white" , font = ("times new roman" , 30 , "bold"))
            show_hed_inv.place(x= 50 , y =5)
            #Search Bar for treeview
            def filterTreeView(*args):
                itemsOnTreeView = lbx.get_children()
                search = search_ent_var.get().lower()
                for eachitem in itemsOnTreeView:
                    if search in lbx.item(eachitem)['values'][0]:
                        search_var = lbx.item(eachitem)['values']
                        lbx.delete(eachitem)
                        lbx.insert("",0,values=search_var)
            search_ent_var = StringVar()
            search_label  =Label(valdisp_f , text = "Search By Name:" , font=("times new roman" , 20 , "bold") , bg = "grey" , fg = "white")
            search_label.place(x= 830 , y = 50)
            search_entry = Entry(valdisp_f ,textvariable=search_ent_var,font = ("Times new roman",20),borderwidth=5)
            search_entry.place(x= 830 , y = 100)
            search_ent_var.trace('w' ,filterTreeView)
            #Working with DATABASE
            conn = sqlite3.connect('tree_crm.db')
            c = conn.cursor()
            c.execute("""CREATE TABLE if not exists customers(
            name text,
            quantity integer,
            price integer
            )""")
            c.execute("SELECT rowid,* FROM customers")
            record = c.fetchall()
            #Making Treeview
            lbx = Treeview(valdisp_f, height=25,yscrollcommand=scrollbar.set)
            #defining Columns
            lbx['columns'] = ("Product" , "Quantity" , "Price" )
            #formating columns
            lbx.column("#0" , anchor=W, width=100)
            lbx.column("Product" ,anchor=W, width=250)
            lbx.column("Quantity" ,anchor=CENTER , width=200)
            lbx.column("Price" ,anchor=CENTER , width=200)
            #making headings
            lbx.heading("#0" , text = 'ID' ,anchor=W)
            lbx.heading("Product" , text = 'Product' ,anchor=W)
            lbx.heading("Quantity" , text = 'Quantity' ,anchor=W)
            lbx.heading("Price" , text = 'Price' ,anchor=W)
            
            count =1   
            for records in record:
                lbx.insert(parent='' , index='end' , iid = count , text = count , values=(records[1] , records[2] , records[3]))
                count+=1
            
            conn.commit()
            conn.close()
            lbx.place(x= 50 ,y = 70)
            scrollbar.config(command=lbx.yview)

        def edit(event):
            hide_all_frame()
            editing_frame.place(x = 95 , y = 60)
            show_hed_inv = Label(editing_frame,text = "Editing Items:" , bg = "grey" , fg = "white" , font = ("times new roman" , 20 , "bold"))
            show_hed_inv.place(x= 40 , y =10)
            #search Bar for treeview
            def filterTreeView(*args):
                itemsOnTreeView = lbx.get_children()
                search = search_ent_var.get().lower()
                for eachitem in itemsOnTreeView:
                    if search in lbx.item(eachitem)['values'][0]:
                        search_var = lbx.item(eachitem)['values']
                        lbx.delete(eachitem)
                        lbx.insert("",0,values=search_var)
            search_ent_var = StringVar()
            search_label  =Label(editing_frame , text = "Search By Name:" , font=("times new roman" , 20 , "bold") , bg = "grey" , fg = "white")
            search_label.place(x= 830 , y = 50)
            search_entry = Entry(editing_frame ,textvariable=search_ent_var,font = ("Times new roman",20),borderwidth=5)
            search_entry.place(x= 830 , y = 100)
            search_ent_var.trace('w' ,filterTreeView)
            #Making database for treeview
            conn = sqlite3.connect('tree_crm.db')
            c = conn.cursor()
            c.execute("""CREATE TABLE if not exists customers(
            name text,
            quantity integer,
            price integer
            )""")
            c.execute("SELECT rowid,* FROM customers")
            record = c.fetchall()
            #Making Treeview
            lbx = Treeview(editing_frame, height=20,yscrollcommand=scrollbar.set)
            #defining Columns
            lbx['columns'] = ("Product" , "Quantity" , "Price" )
            #formating columns
            lbx.column("#0" , anchor=W, width=100)
            lbx.column("Product" ,anchor=W, width=250)
            lbx.column("Quantity" ,anchor=CENTER , width=200)
            lbx.column("Price" ,anchor=CENTER , width=200)
            #making headings
            lbx.heading("#0" , text = 'ID' ,anchor=W)
            lbx.heading("Product" , text = 'Product' ,anchor=W)
            lbx.heading("Quantity" , text = 'Quantity' ,anchor=W)
            lbx.heading("Price" , text = 'Price' ,anchor=W)
            
            count = 1
            for records in record:
                lbx.insert(parent='' , index='end' , iid = count , text = count , values=(records[1] , records[2] , records[3]))
                count+=1
                
            #database closing    
            conn.commit()
            conn.close()
            lbx.place(x= 35 ,y = 50)
            scrollbar.config(command=lbx.yview)

            def add_record():
                lbx.insert(parent='' ,index ='end',values=(product_tree_entry.get(),quantity_tree_entry.get(),price_tree_entry.get())) 
                conn = sqlite3.connect('tree_crm.db')
                c = conn.cursor()
                c.execute("""CREATE TABLE if not exists customers(
                    name text,
                    quantity integer,
                    price integer
                    )""")
                c.execute("INSERT INTO customers VALUES(?,?,?)",(product_tree_entry.get(),quantity_tree_entry.get(),price_tree_entry.get()))
                #clearing the entry box
                product_tree_entry.delete(0,END)
                quantity_tree_entry.delete(0,END)
                price_tree_entry.delete(0,END)
                conn.commit()
                conn.close()
                
            def removeall():
                response = tmsg.askyesno("Warning" , "All the data will be deleted\nAre you sure?")
                if response == 1:
                    for record in lbx.get_children():
                        lbx.delete(record)
                    conn = sqlite3.connect('tree_crm.db')
                    c = conn.cursor()
                    c.execute("DROP TABLE customers")
                    conn.commit()
                    conn.close()
                    product_tree_entry.delete(0,END)
                    quantity_tree_entry.delete(0,END)
                    price_tree_entry.delete(0,END)
            
            def remove_selected():
                x = lbx.selection()[0]
                lbx.delete(x)
                conn = sqlite3.connect('tree_crm.db')
                c = conn.cursor()
                #deleting selected record by using there id
                c.execute("DELETE FROM customers WHERE name = (?)",(product_tree_entry.get(),))
                conn.commit()
                conn.close()
                product_tree_entry.delete(0,END)
                quantity_tree_entry.delete(0,END)
                price_tree_entry.delete(0,END)

            def selectbutton():
                product_tree_entry.delete(0,END)
                quantity_tree_entry.delete(0,END)
                price_tree_entry.delete(0,END)
                #grabing the record numbers
                selected = lbx.focus()
                #grabing record values from treeview
                values = lbx.item(selected , 'values')
                product_tree_entry.insert(0,values[0])
                quantity_tree_entry.insert(0,values[1])
                price_tree_entry.insert(0,values[2])
                #this is for update fun
                global temp
                temp = product_tree_entry.get()

            def updaterecord():
                selected = lbx.focus()
                values = lbx.item(selected , text='' ,values = (product_tree_entry.get(),quantity_tree_entry.get(),price_tree_entry.get()))
                conn = sqlite3.connect('tree_crm.db')
                c = conn.cursor()
                c.execute("""UPDATE customers SET
                name = :first_name, 
                quantity = :first_quantity,
                price = :first_price
                WHERE name = :temp_var""",
                {
                    'first_name':product_tree_entry.get(),
                    'first_quantity':quantity_tree_entry.get(),
                    'first_price':price_tree_entry.get(),
                    'temp_var':temp,
                }
                )
                product_tree_entry.delete(0,END)
                quantity_tree_entry.delete(0,END)
                price_tree_entry.delete(0,END)
                conn.commit()
                conn.close()
                
            def showinfo():
                global info_W
                info_W = Toplevel(root2)
                info_W.geometry("950x600")
                info_W.title("How To Use Edit Function")
                info_W.config(bg="#fff")
                text_is = """>Add :: To Add the items,Enter the item details then select <Add>.\n\n>Remove Selected :: Choose the product then click <Select> and then click <Remove Selected>.\n\n>Remove All :: Just click <Remove All> to remove entire data.\n\n>Update :: To Update choose the product then click <Select> and change the details you want and then click <Update>.\n\n>Search bar :: In search bar you can search the Product by name only."""
                info_text = Text(info_W,font=("lucida",13,"bold"))
                info_text.pack(fill=BOTH,expand=1)
                info_text.insert(END,text_is)
                info_W.mainloop()

            Enter_item = Label(editing_frame ,text = "Enter Item" , font = ("Time new roman" ,15) , bg = "grey" , fg = "white")
            Enter_item.place(x= 50 , y = 500)
            Label(editing_frame , text="Name" , bg = "grey", fg = "#fff").place(x=50 , y = 530)
            product_tree_entry = Entry(editing_frame,font = ("times new roman" ,15))
            product_tree_entry.place(x= 50 , y =550)
            #Label(editing_frame , text="ID" , bg = "grey", fg = "#fff").place(x=257 , y = 530)
            #ID_tree_entry = Entry(editing_frame,width=15,font = ("times new roman" ,15))
            #ID_tree_entry.place(x=257, y =550)
            Label(editing_frame , text="Quantity" , bg = "grey", fg = "#fff").place(x=257, y = 530)
            quantity_tree_entry = Entry(editing_frame,width=15,font = ("times new roman" ,15))
            quantity_tree_entry.place(x=257 , y =550)
            Label(editing_frame , text="Price per piece" , bg = "grey", fg = "#fff").place(x=415, y = 530)
            price_tree_entry = Entry(editing_frame,width=15,font = ("times new roman" ,15))
            price_tree_entry.place(x=415, y =550)
            
            Edit_B_Frame = Frame(editing_frame , bg  = "white" , borderwidth=5 , relief=RIDGE , width=1150,height=80)
            Edit_B_Frame.place(x=5 , y = 640)
            add_val_B = Button(Edit_B_Frame,text="Add",bg = "grey" ,fg = "white",font=("time new roman",15,"bold"),padx=15,pady=5,command = add_record).place(x=5,y=10)
            Remv_sec_val_B = Button(Edit_B_Frame,text="Remove Selected",bg = "grey" ,fg = "white",font=("time new roman",15,"bold"),padx=5,pady=5,command=remove_selected).place(x=100,y=10)
            Remv_all_val_B = Button(Edit_B_Frame,text="Remove All",bg = "grey" ,fg = "white",font=("time new roman",15,"bold"),padx=10,pady=5,command=removeall).place(x=300,y=10)
            select_B = Button(Edit_B_Frame,text="Select",bg = "grey" ,fg = "white",font=("time new roman",15,"bold"),padx=15,pady=5,command=selectbutton).place(x=453,y=10)
            update_selected_B = Button(Edit_B_Frame,text="Update",bg = "grey" ,fg = "white",font=("time new roman",15,"bold"),padx=15,pady=5,command=updaterecord).place(x=570,y=10)
            Showinfo_B = Button(Edit_B_Frame,text="How to use?",bg = "grey" ,fg = "orange",font=("time new roman",15,"bold"),padx=15,pady=5,command=showinfo).place(x=695,y=10)

        def notepad(event):
            hide_all_frame()
            NOTEPAD_frame.place(x = 95 , y = 60)
            text_area.place(x=5,y=5)
            def open_text():
                text_file = open("notes.txt" , 'r')
                Stuff =text_file.read()
                text_area.insert(END,Stuff)
                text_file.close()
            def save_text():
                text_file = open("notes.txt" , "w")
                text_file.write(text_area.get(1.0 , END))
                text_area.delete("1.0","end")
            Open_Button = Button(NOTEPAD_frame,text="Open Text" ,command=open_text,padx=7,pady=7)
            Open_Button.place(x=950 ,y=720)
            SAVE_Button = Button(NOTEPAD_frame,text="Save" ,command=save_text,padx=10,pady=7)
            SAVE_Button.place(x=1050 ,y=720)
            scrollbar.config(command=text_area.yview)
                    
        def Update(event):
            hide_all_frame()
            Update_frame.place(x = 95 , y = 60)
            update_label = Labelframe(Update_frame ,width=200,height=200,text = "Updates:" ,borderwidth=5,relief=RIDGE )
            update_label.place(x=20,y=20)
            update_ver = "1.0"
            text_1 = Text(update_label,font = ("lucida",13),width=70,height=7)
            text_1.pack(fill = BOTH , expand=1)
            text = f"This is informed you that this is the latest version.Version ({update_ver}) .Download and install\nthe latest updates if there are to get better performance.\n\n\t\t\t---Contact the Developer---"
            text_1.insert(END ,text)
            #check_up_B = Button()  

        def hide_all_frame():
            text_area.place_forget()
            valdisp_f.place_forget()
            editing_frame.place_forget()
            NOTEPAD_frame.place_forget()
            Update_frame.place_forget()

        #*******MAIN WINDOW2*******
        root2 = Toplevel(root)
        root2.title("Market Store")
        root2.geometry("1280x830")
        #Frames used in func
        valdisp_f = Frame(root2 , width=1170 , height=768 , bg = "grey" , borderwidth=5 , relief=SUNKEN)
        editing_frame = Frame(root2 , width=1170 , height=768, bg = "grey" , borderwidth=5 , relief=SUNKEN)
        NOTEPAD_frame = Frame(root2 , width=1170 , height=768 , bg = "grey" , borderwidth=5 , relief=SUNKEN)
        text_area = Text(NOTEPAD_frame,width=125,height=37, font = ("lucida",13),border=1)
        Update_frame = Frame(root2 , width=1170 , height=768 , bg = "grey" , borderwidth=5 , relief=SUNKEN)
        #***************
        heading_f  = Frame(root2 , relief=RIDGE , borderwidth=10 , bg = "grey")
        heading_f.pack(side = TOP , fill = X)
        heading_l = Label(heading_f , text = "Welcome to Lateef Electronic" , bg = "grey" , fg = "cyan" , font = ("Times New Roman" , 25 ,"bold"))
        heading_l.pack()
        heading_l_2 = Label(heading_f ,border=0, text = "Software By Talha Aslam" , bg = "grey" , fg = "black" , font = ("Arial Black" , 11 ,"bold"))
        heading_l_2.place(x=1040,y=17)
        #***************************
        scrollbar = Scrollbar(root2)
        scrollbar.pack(side=RIGHT , fill = Y)
        #**************************
        menu_hed_f = Frame(root2 , relief = RIDGE , borderwidth=3 , bg = "grey" ) 
        menu_hed_f.pack(side = LEFT , fill = Y)
        menu_L = Label(menu_hed_f , text = "MENU" , bg  = "grey" , fg = "black" , font = ("Times new roman" , 20 , "bold") )
        menu_L.pack()

        inv_button = Button(menu_hed_f , text="Inventry" , bg  = "grey" , fg = "black" , border=1 ,font=("times new roman" , 15 , "bold") , pady=10)
        inv_button.place(x = 0 , y = 70 )
        inv_button.bind('<Button-1>' , inventry)

        edit_button = Button(menu_hed_f , text="Edit" , bg  = "grey" , fg = "black" , border=1 ,font=("times new roman" , 15 , "bold") ,padx=20, pady=10)
        edit_button.place(x = 0 , y = 170 )
        edit_button.bind('<Button-1>' , edit)

        notes_button = Button(menu_hed_f , text="Notes" , bg  = "grey" , fg = "black" , border=1 ,font=("times new roman" , 15 , "bold") ,padx=13, pady=10)
        notes_button.place(x = 0 , y = 270 )
        notes_button.bind('<Button-1>' , notepad)

        Update_button = Button(menu_hed_f , text="Update" , bg  = "grey" , fg = "black" , border=1 ,font=("times new roman" , 15 , "bold") ,padx=7, pady=10)
        Update_button.place(x = 0 , y = 370 )
        Update_button.bind('<Button-1>' , Update)
        #********************
        root2.resizable(FALSE ,FALSE)
        root2.mainloop()
        


    if username.lower() != "admin" or password != "55555":
        if username.lower() == "" and password == "":
            pass
        else:
            tmsg.showerror("Login Alert" ,"Email or Password does not match!")
            user_name_E.delete(0,END)
            user_pass_E.delete(0,END)

root = Tk()
root.geometry("900x600")
root.title("LOGIN PAGE")
root.resizable(False,False)

img = PhotoImage(file="tut.png")
ico = PhotoImage(file = "man.png")
Label(root , image=img ).pack()



frame = Frame(root , width=500 , height=450 , bg= "#fff").place(x=200,y=80)
Label(root , image=ico ).place(x =520 , y = 200)
heading = Label(frame , text = "SIGN IN" , fg = "#57a1f8" , bg = "white" ,font = ("Bauhaus 93",23,"bold"))
heading.place(x =390 , y= 90 )

user_name = Label(frame , text = "Username :" , fg = "#57a1f8" , bg = "white" ,font = ("Bauhaus 93",23,"bold"))
user_name.place(x =230 , y= 170 )

value = StringVar()
passw = StringVar()

value.set("")
user_name_E = Entry(frame ,textvariable=value,bg ="white",fg="black", width = 20 ,border=1 , font=("Times New Roman" , 15))
user_name_E.place(x=260 , y= 220)

user_pass = Label(frame , text = "Password :" , fg = "#57a1f8" , bg = "white" ,font = ("Bauhaus 93",23,"bold"))
user_pass.place(x =230 , y= 250 )
passw.set("")
user_pass_E = Entry(frame ,textvariable=passw,bg ="white",fg="black", width = 20 ,border=1 , font=("Times New Roman" , 15))
user_pass_E.place(x=260 , y= 300)

button = Button(frame ,width = 20 ,text = 'LOGIN' , bg ="#57a1f8" , fg = "white" ,border=0, font = ("Bauhaus 93" ,15 , "bold"))
button.place(x=330 , y = 370)
button.bind("<Button-1>", click)

root.mainloop()