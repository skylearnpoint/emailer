from tkinter import*
from PIL import ImageTk
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
        btn_setting=Button(self.root,image=self.setting_icon,bd=0,activebackground="#222A35",bg="#222A35").place(x=850,y=5)
        desc=Label(self.root,text="Please use Excel file ",font=("Calibri (Body)",14),bg="#FFD966",fg="#262626").place(x=0,y=100,relwidth=1) 
        #..................Button
        self.var_choice=StringVar()
        single=Radiobutton(self.root,text="Single",value="single",variable=self.var_choice,activebackground="white",font=("times new roman",30,"bold"),bg="white",fg="#262627").place(x=50,y=150)
        single=Radiobutton(self.root,text="Bulk",value="bulk",variable=self.var_choice,activebackground="white",font=("times new roman",30,"bold"),bg="white",fg="#262627").place(x=300,y=150)
        self.var_choice.set("single")
        btn_browse=Button(self.root,text="BROWSE",font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=750,y=240,width=120,height=30)


        #.................sender main
        to=Label(self.root,text="To (Email Address)",bg="white",font=("times new roman",18,"bold")).place(x=50,y=240)
        subj=Label(self.root,text="Subject",bg="white",font=("times new roman",18,"bold")).place(x=50,y=280) 
        msg=Label(self.root,text="Message",bg="white",font=("times new roman",18,"bold")).place(x=50,y=320)
        self.txt_to=Entry(self.root,font=("time new roman",14),bg="lightyellow").place(x=350,y=240,width=350,height=30)        
        self.txt_subj=Entry(self.root,font=("time new roman",14),bg="lightyellow").place(x=350,y=280,width=450,height=30)
        self.txt_msg=Text(self.root,font=("time new roman",12),bg="lightyellow").place(x=350,y=320,width=600,height=100)
        btn_send=Button(self.root,text="SEND",font=("times new roman",18,"bold"),bg="#00B0F0",fg="white",cursor="hand2",activebackground="#00B0F0",activeforeground="white").place(x=850,y=450,width=120,height=30)
        btn_clear=Button(self.root,text="CLEAR",font=("times new roman",18,"bold"),bg="#262626",fg="white",cursor="hand2",activebackground="#262626",activeforeground="white").place(x=700,y=450,width=120,height=30)


root=Tk()
obj=Email(root)
root.mainloop()