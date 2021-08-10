from tkinter import*
from PIL import ImageTk
from tkinter import messagebox
class Email:
    def __init__(self,root):
        self.root=root
        self.root.title("Automatic Email App")
        self.root.geometry("1000x550+200+50")  # defined size and default area of opening
        self.root.resizable(False,False)    #resize frame locked
        self.root.config(bg="white")   #background color

          #.......icon..........
        self.email_icon=ImageTk.PhotoImage(file="logo.png")
        self.setting_icon=ImageTk.PhotoImage(file="set.png")
       #......title......
        title=Label(self.root,text="The Inseparable Mailer",image=self.email_icon,padx=40,compound='left',font=("Goudy Old Style",48,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1) 
        btn_setting=Button(self.root,image=self.setting_icon,bd=0,activebackground="#222A35",bg="#222A35",cursor="hand2",command=self.setting_window).place(x=850,y=5)
        desc=Label(self.root,text="Please use Excel file ",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=100,relwidth=1) 
        #..................Button
        self.var_choice=StringVar()
        single=Radiobutton(self.root,text="Single",value="single",variable=self.var_choice,command=self.check_single_or_bulk,activebackground="white",font=("times new roman",30,"bold"),bg="white",fg="#262627").place(x=50,y=150)
        single=Radiobutton(self.root,text="Bulk",value="bulk",variable=self.var_choice,activebackground="white",font=("times new roman",30,"bold"),bg="white",fg="#262627",command=self.check_single_or_bulk).place(x=300,y=150)
        self.var_choice.set("single")
        self.btn_browse=Button(self.root,text="BROWSE",font=("times new roman",15,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white",state=DISABLED)
        self.btn_browse.place(x=750,y=240,width=120,height=30)


        #.................sender main
        to=Label(self.root,text="To (Email Address)",bg="white",font=("times new roman",18,"bold")).place(x=50,y=240)
        subj=Label(self.root,text="Subject",bg="white",font=("times new roman",18,"bold")).place(x=50,y=280) 
        msg=Label(self.root,text="Message",bg="white",font=("times new roman",18,"bold")).place(x=50,y=320)
        #........entry field......
        self.txt_to=Entry(self.root,font=("time new roman",14),bg="lightyellow")
        self.txt_to.place(x=350,y=240,width=350,height=30)        
        
        self.txt_subj=Entry(self.root,font=("time new roman",14),bg="lightyellow")
        self.txt_subj.place(x=350,y=280,width=450,height=30)
        
        self.txt_msg=Text(self.root,font=("time new roman",12),bg="lightyellow")
        self.txt_msg.place(x=350,y=320,width=600,height=100)
        
        btn_send=Button(self.root,command=self.send_email,text="SEND",font=("times new roman",18,"bold"),bg="#00B0F0",fg="white",cursor="hand2",activebackground="#00B0F0",activeforeground="white")
        btn_send.place(x=850,y=450,width=120,height=30)
             
        btn_clear=Button(self.root,text="CLEAR",command=self.clear1,font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=700,y=450,width=120,height=30)
    
    
    
    def check_single_or_bulk(self):
        if self.var_choice.get()=="single":
          #messagebox.showinfo("Success","Single",parent=self.root)
          self.btn_browse.config(state=DISABLED)
        if self.var_choice.get()=="bulk":
          #messagebox.showinfo("Success","bulk",parent=self.root)
          self.btn_browse.config(state=NORMAL)    
    
    def clear1(self):
      self.txt_to.delete(0,END)
      self.txt_subj.delete(0,END)
      self.txt_msg.delete('1.0',END)
      self.var_choice.set("single")
      self.btn_browse.config(state=NORMAL)
         
    

    def send_email(self):          
        x=self.txt_msg.get('1.0',END)
        print(x)
        if self.txt_to.get()=="" or self.txt_subj.get()=="" or x==1:
          messagebox.showerror("error","ALL FIELD ARE REQUIRED",parent=self.root)
        else:
          messagebox.showinfo("Success","Email Has been Sent",parent=self.root)
    
    
    def setting_window(self):
        self.root2=Toplevel()
        self.root2.title("setting")
        self.root2.geometry("700x400+350+90")
        self.root2.focus_force()
        self.root2.grab_set()
        self.root2.config(bg="white")
        title2=Label(self.root2,text="Credential Setting",image=self.setting_icon,padx=40,compound='left',font=("Goudy Old Style",48,"bold"),bg="#222A35",fg="white",anchor="w").place(x=0,y=0,relwidth=1)
        desc2=Label(self.root2,text="Enter Sender Email Id and Password ",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=100,relwidth=1) 
        from_=Label(self.root2,text="Email Address",bg="white",font=("times new roman",18,"bold")).place(x=50,y=140)
        password=Label(self.root2,text="PASSWORD",bg="white",font=("times new roman",18,"bold")).place(x=50,y=180)
        self.txt_from=Entry(self.root2,font=("time new roman",14),bg="lightyellow").place(x=250,y=140,width=350,height=30)        
        self.txt_password=Entry(self.root2,font=("time new roman",14),bg="lightyellow").place(x=250,y=180,width=250,height=30)
      
        btn_save=Button(self.root2,text="SAVE",font=("times new roman",18,"bold"),bg="#00B0F0",fg="white",cursor="hand2",activebackground="#00B0F0",activeforeground="white").place(x=450,y=250,width=120,height=30)
        btn_clear2=Button(self.root2,text="CLEAR",font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=400,y=250,width=120,height=30)
      


           
        


root=Tk()
obj=Email(root)
root.mainloop()
