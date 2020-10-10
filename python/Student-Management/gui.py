from tkinter import *
from tkinter import StringVar , Label , ttk , scrolledtext , filedialog,simpledialog , messagebox
from main_module import *
import csv

# TO verify New Student entries
def verifier():
    a=b=c=d=e=f=g=h=i=j=0
    txt.delete(1.0,END)
    if not aa.get() or aa.get() == "SELECT":
        txt.insert(INSERT," \n\n------------------------------>>\n\nSelect Section Properly \n")
        a=1
    if not bb.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not cc.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd.get() or dd.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee.get() or ee.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff.get() or ff.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    if not gg.get() :
        txt.insert(INSERT,"Type Father Name \n")
        g=1
    if not hh.get() :
        txt.insert(INSERT,"Type Mother Name \n")
        h=1
    if not ii.get() or ii.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 :
        return 1
    else:
        return 0

# TO verify Update Student entries
def verifier1():
    a=b=c=d=e=f=g=h=i=j=k=0
    txt.delete(1.0,END)
    if not roll_roll1.get():
        txt.insert(INSERT,"Type Roll Number \n")
        k=1
    if not aa1.get() or aa1.get() == "SELECT":
        txt.insert(INSERT," \n\n------------------------------>>\n\nSelect Section Properly \n")
        a=1
    if not bb1.get():
        txt.insert(INSERT,"Type First Name \n")
        b=1
    if not cc1.get():
        txt.insert(INSERT,"Type Last Name\n")
        c=1
    if not dd1.get() or dd1.get() == "SELECT":
        txt.insert(INSERT,"Select Class Properly \n")
        d=1
    if not ee1.get() or ee1.get() == "SELECT":
        txt.insert(INSERT,"Select Section Properly \n")
        e=1
    if not ff1.get() or ff1.get() == "SELECT":
        txt.insert(INSERT,"Select Gender Properly \n")
        f=1
    if not gg1.get() :
        txt.insert(INSERT,"Type Father Name \n")
        g=1
    if not hh1.get() :
        txt.insert(INSERT,"Type Mother Name \n")
        h=1
    if not ii1.get() or ii1.get() == "SELECT":
        txt.insert(INSERT,"Type Mobile Number\n")
        i=1
    if not jj1.get():
        txt.insert(INSERT,"Type Address\n")
        j=1
        
    if a==1 or b==1 or c==1 or d==1 or e==1 or f==1 or g==1 or h==1 or i==1 or j==1 :
        return 1
    else:
        return 0

def add_student() :
    if verifier() == 0 :
        student = {"session" : aa.get() , "first_name" : bb.get() , "last_name" : cc.get() , "class" : dd.get() ,  "section" : ee.get() , "gender" : ff.get() , "father" : gg.get() , "mother" : hh.get(),"mobile" : ii.get(),"address" : jj.get()}

        return_data = student_create(student)
        txt.delete(1.0,END)
        for key, value in return_data.items() :
            roll=str(key)
            txt.insert(INSERT,"\n------------------------------>>\n")
            txt.insert(INSERT,"Your Details -->>"+"\n\nRoll No. : "+roll+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+"\nFather : "+return_data[key]["father"]+"\nMother : "+return_data[key]["mother"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")
 
        aa.delete(0,END)
        bb.delete(0,END)
        cc.delete(0,END)
        dd.delete(0,END)
        ee.delete(0,END)
        ff.delete(0,END)
        gg.delete(0,END)
        hh.delete(0,END)
        ii.delete(0,END)
        jj.delete(0,END)
      

def view_student() :
    return_data = student_list()
    txt.delete(1.0,END)
    txt.insert(INSERT,"\n Roll No.,\tStudent Name,\t\t Class ,\t Section,\t Father Name ,\t\t\t Mobile ,\t\t Address \n")
    for key, value in return_data.items() :
        if return_data[key] == "This Record is Deleted from System" :
            continue
        else :
            roll=str(key)
            txt.insert(INSERT,"\n"+roll+",\t"+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+",\t\t"+return_data[key]["class"]+",\t"+return_data[key]["section"]+",\t"+return_data[key]["father"]+",\t\t\t"+return_data[key]["mobile"]+",\t\t"+return_data[key]["address"],"\n")

def update_student() :
    if verifier1() == 0 :
        rollNo = roll_roll1.get()
        student = {"session" : aa1.get() , "first_name" : bb1.get() , "last_name" : cc1.get() , "class" : dd1.get() ,  "section" : ee1.get() , "gender" : ff1.get() , "father" : gg1.get() , "mother" : hh1.get(),"mobile" : ii1.get(),"address" : jj1.get()}
        return_data = student_update(rollNo,student)
        txt.delete(1.0,END)
        for key, value in return_data.items() :
            if key == rollNo :
                rollNo=str(key)
                txt.insert(INSERT,"\n------------------------------>>\n")
                txt.insert(INSERT,"Updated Details -->>"+"\n\nRoll No. : "+rollNo+"\nName : "+return_data[key]["first_name"]+" "+return_data[key]["last_name"]+"\nClass : "+return_data[key]["class"]+"\nFather : "+return_data[key]["father"]+"\nMother : "+return_data[key]["mother"]+"\nMobile : "+return_data[key]["mobile"]+"\nAddress :"+return_data[key]["address"],"\n")

        aa1.delete(0,END)
        bb1.delete(0,END)
        cc1.delete(0,END)
        dd1.delete(0,END)
        ee1.delete(0,END)
        ff1.delete(0,END)
        gg1.delete(0,END)
        hh1.delete(0,END)
        ii1.delete(0,END)
        jj1.delete(0,END)
        
def delete_student() :
    messagebox.showwarning("Warning","Are you sure ?")
    data = student_delete(entry_delete.get())
    txt.delete(1.0,END)
    txt.insert(INSERT,data)

def search_by_class() :
    pass

def clse() :
    sys.exit()


def saveFile():
    f = filedialog.asksaveasfile(mode='w',defaultextension='.csv')
    if f!= None:
        data = txt.get('1.0',END)
    try:
        f.write(data)
        txt.delete(1.0,END)
        txt.insert(INSERT,"Spreadsheet Saved Successfully !")
    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")

def classwise() :
    return_data = student_list()
    txt.delete(1.0,END)
   #txt.insert(INSERT,"\nRoll No.\tFirst Name\tLastName\tClass\tSection\tGender\tFather\tMother\tMobile\tAddress")
    if combo_class.get() in ("LKG","HKG","NURSERY",'1', '2', '3', '4', '5','6','7','8','9','10','11','12') :
        for key, value in return_data.items() :
            if return_data[key] == "This Record is Deleted from System" :
                continue
            else :
                roll=str(key)
                if combo_class.get() == return_data[key]["class"]:
                    txt.insert(INSERT,"\n"+roll+",\t"+return_data[key]["first_name"]+"\t"+return_data[key]["last_name"]+",\t"+return_data[key]["class"]+",\t"+return_data[key]["section"]+",\t"+return_data[key]["gender"]+",\t"+return_data[key]["father"]+",\t"+return_data[key]["mother"]+",\t"+return_data[key]["mobile"]+",\t"+return_data[key]["address"],"\n")
                    
if __name__=="__main__":
    root=Tk()
    w=1000
    h=700
    ws = root.winfo_screenwidth()
    hs = root.winfo_screenheight()
    x = (ws/2) - (w/2)    
    y = (hs/2) - (h/2)
    root.geometry('%dx%d+%d+%d' % (w, h, x, y))
    root.title("Student Management")
    
    # ----------------------
    
    sess = StringVar()
    fn = StringVar()
    ln = StringVar()
    cl = StringVar()
    sect = StringVar()
    gen = StringVar()
    fa_name= StringVar()
    mo_name = StringVar()
    mob = StringVar()
    ad = StringVar()
    
    heading=Label(root,text="New Student",font=("Arial",12),foreground ="#ee9a4d")
    label_a=Label(root,text="Session :",font=("Arial",10),width=10)
    label_b=Label(root,text="First Name :",font=("Arial",10),width=10)
    label_c=Label(root,text="Last Name :",font=("Arial",10),width=10)
    label_d=Label(root,text="Class :",font=("Arial",10),width=10)
    label_e=Label(root,text="Section :",font=("Arial",10),width=10)
    label_f=Label(root,text="Gender :",font=("Arial",10),width=10)
    label_g=Label(root,text="Father Name :",font=("Arial",10),width=10)
    label_h=Label(root,text="Mother Name :",font=("Arial",10),width=10)
    label_i=Label(root,text="Mobile :",font=("Arial",10),width=10)
    label_j=Label(root,text="Address :",font=("Arial",10),width=10)
    
    aa = ttk.Combobox(root,width=10)    # Session entry
    aa['values']= ("SELECT","2015-16","2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
    aa.current(0) #set the selected item
    
    bb=Entry(root,textvariable=fn,width=10)    # first name
    
    cc=Entry(root,textvariable=ln,width=10)    # last name
    
    dd = ttk.Combobox(root,width=10)    # class name
    dd['values']= ("SELECT","LKG","HKG","NURSERY",1, 2, 3, 4, 5,6,7,8,9,10,11,12)
    dd.current(0) #set the selected item
    
    ee = ttk.Combobox(root,width=10)    # section name
    ee['values']= ("A","B","C","D","E")
    ee.current(0) #set the selected item
    
    ff = ttk.Combobox(root,width=10)    # gender
    ff['values']= ("SELECT","Male","Female")
    ff.current(0) #set the selected item
    
    gg=Entry(root,textvariable=fa_name,width=10)    # father name
    
    hh=Entry(root,textvariable=mo_name,width=10)    # mother name
    
    ii=Entry(root,textvariable=mob,width=10)    # mobile
    
    jj=Entry(root,textvariable=ad,width=10)    # address
   
     # ----------------------

    heading1=Label(root,text="Update Student",font=("Arial",12),foreground ="#ee9a4d")
    label_roll=Label(root,text="Roll Number :",font=("Arial",10),width=10)
    label_a1=Label(root,text="Session :",font=("Arial",10),width=10)
    label_b1=Label(root,text="First Name :",font=("Arial",10),width=10)
    label_c1=Label(root,text="Last Name :",font=("Arial",10),width=10)
    label_d1=Label(root,text="Class :",font=("Arial",10),width=10)
    label_e1=Label(root,text="Section :",font=("Arial",10),width=10)
    label_f1=Label(root,text="Gender :",font=("Arial",10),width=10)
    label_g1=Label(root,text="Father Name :",font=("Arial",10),width=10)
    label_h1=Label(root,text="Mother Name :",font=("Arial",10),width=10)
    label_i1=Label(root,text="Mobile :",font=("Arial",10),width=10)
    label_j1=Label(root,text="Address :",font=("Arial",10),width=10)

    roll1 = StringVar()
    sess1 = StringVar()
    fn1 = StringVar()
    ln1 = StringVar()
    cl1 = StringVar()
    sect1 = StringVar()
    gen1 = StringVar()
    fa_name1= StringVar()
    mo_name1 = StringVar()
    mob1 = StringVar()
    ad1 = StringVar()

    roll_roll1=Entry(root,textvariable=roll1,width=10)    # Roll Number

    aa1 = ttk.Combobox(root,width=10)    # Session entry
    aa1['values']= ("SELECT","2015-16","2016-17","2017-18","2018-19","2019-20","2020-21","2021-22","2022-23","2023-24","2024-25","2025-26")
    aa1.current(0) #set the selected item
    
    bb1=Entry(root,textvariable=fn,width=10)    # first name
    
    cc1=Entry(root,textvariable=ln,width=10)    # last name
    
    dd1 = ttk.Combobox(root,width=10)    # class name
    dd1['values']= ("SELECT","LKG","HKG","NURSERY",1, 2, 3, 4, 5,6,7,8,9,10,11,12)
    dd1.current(0) #set the selected item
    
    ee1 = ttk.Combobox(root,width=10)    # section name
    ee1['values']= ("A","B","C","D","E")
    ee1.current(0) #set the selected item
    
    ff1 = ttk.Combobox(root,width=10)    # gender
    ff1['values']= ("SELECT","Male","Female")
    ff1.current(0) #set the selected item
    
    gg1=Entry(root,textvariable=fa_name,width=10)    # father name
    
    hh1=Entry(root,textvariable=mo_name,width=10)    # mother name
    
    ii1=Entry(root,textvariable=mob,width=10)    # mobile
    
    jj1=Entry(root,textvariable=ad,width=10)    # address

    # ----------------------
    roll_delete = StringVar()
    heading2=Label(root,text="Delete Student",font=("Arial",12),foreground ="#ee9a4d")
    label_del=Label(root,text="Record",font=("Arial",12),width=10)
    label_delete=Label(root,text="Roll Number :",font=("Arial",12),width=10)
    entry_delete=Entry(root,textvariable=roll_delete,font=("Arial",12),width=10)
    
    def addnew():
        
        heading.grid(row=8 , column=1,columnspan=2)
        
        label_a.grid(row=9 , column=1)
        label_b.grid(row=10 , column=1)
        label_c.grid(row=11 , column=1)
        label_d.grid(row=12 , column=1)
        label_e.grid(row=13 , column=1)
        label_f.grid(row=14 , column=1)
        label_g.grid(row=15 , column=1)
        label_h.grid(row=16 , column=1)
        label_i.grid(row=17 , column=1)
        label_j.grid(row=18 , column=1)
  
        aa.grid(row=9 , column=2)   
        bb.grid(row=10 , column=2)
        cc.grid(row=11 , column=2)
        dd.grid(row=12 , column=2)
        ee.grid(row=13 , column=2)
        ff.grid(row=14 , column=2)
        gg.grid(row=15 , column=2)
        hh.grid(row=16 , column=2)
        ii.grid(row=17 , column=2)
        jj.grid(row=18 , column=2)

        b1=Button(root,text="ADD",command=lambda: add_student(),width=40,background = '#4E8975', foreground ="white",font=("Arial",11))
        b1.grid(row=21 , column=1, columnspan=2)    
   
    def update() :
        
        heading1.grid(row=8 , column=3,columnspan=2)
        
        label_roll.grid(row=9 , column=3)
        label_a1.grid(row=10 , column=3)
        label_b1.grid(row=11 , column=3)
        label_c1.grid(row=12 , column=3)
        label_d1.grid(row=13 , column=3)
        label_e1.grid(row=14 , column=3)
        label_f1.grid(row=15 , column=3)
        label_g1.grid(row=16 , column=3)
        label_h1.grid(row=17 , column=3)
        label_i1.grid(row=18 , column=3)
        label_j1.grid(row=19 , column=3)
  
        roll_roll1.grid(row=9 , column=4)
        aa1.grid(row=10 , column=4)   
        bb1.grid(row=11 , column=4)
        cc1.grid(row=12 , column=4)
        dd1.grid(row=13 , column=4)
        ee1.grid(row=14 , column=4)
        ff1.grid(row=15 , column=4)
        gg1.grid(row=16 , column=4)
        hh1.grid(row=17 , column=4)
        ii1.grid(row=18 , column=4)
        jj1.grid(row=19 , column=4)

        b2=Button(root,text="UPDATE",command=lambda: update_student(),width=40,background = '#4E8975', foreground ="white",font=("Arial",11))
        b2.grid(row=21 , column=3, columnspan=2)
    # ----------------------
    
    def delete() :

        heading2.grid(row=8 , column=5,columnspan=1)
        
     #   label_del.grid(row=9 , column=5 )
        label_delete.grid(row=14 , column=5 )
        entry_delete.grid(row=15 , column=5)

        b3=Button(root,text="DELETE",command=lambda: delete_student(),width=25,background = '#4E8975', foreground ="white",font=("Arial",11))
        b3.grid(row=21 , column=5, columnspan=1)
        
    # ----------------------

    dashboard=Label(root,text=" Dashboard ",font=("Arial",16),foreground="#ee9a4d")
    dashboard.grid(row=0,column=0)

    view=Button(root,text="VIEW ALL",background = '#4E8975', foreground ="white",command=lambda: view_student(),width=10,font=("Arial",11))
    view.grid(row=0,column=1)

    add=Button(root,text="NEW",command=addnew,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    add.grid(row=0,column=2)

    update=Button(root,text="UPDATE",command=update,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    update.grid(row=0,column=3)

    delete=Button(root,text="DELETE",command=delete,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    delete.grid(row=0 , column=4)


    txt = scrolledtext.ScrolledText(root,width=120,height=10,background = '#fff8dc', foreground ="#4E8975",font=("Arial",11))
    txt.grid(row=1,column=0,rowspan=5 , columnspan=7)

    save=Button(root,text="Save As Spreadsheet",command=saveFile,width=18,background = '#4E8975', foreground ="white",font=("Arial",11))
    save.grid(row=5,column=2,columnspan=3)

    combo_class = ttk.Combobox(root,width=15)    # Filter Searches
    combo_class['values']= ("CLASS","LKG","HKG","NURSERY",1, 2, 3, 4, 5,6,7,8,9,10,11,12)
    combo_class.current(0) #set the selected item
    combo_class.grid(row=0,column=5)

    combo_class_button=Button(root,text="SEARCH",command=classwise,width=10,background = '#4E8975', foreground ="white",font=("Arial",11))
    combo_class_button.grid(row=0,column=6)

    classroom=Button(root,text="Go to Classroom",command=lambda: classroom(),width=40,background = '#4E8975', foreground ="white",font=("Arial",11))
    classroom.grid(row=22 , column=3, columnspan=2)
     
    root.mainloop()
    
