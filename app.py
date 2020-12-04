from tkinter import *
import tkinter.messagebox
from tkinter import filedialog


class Merge:
    def __init__(self,root):
        self.root=root
        self.root.title("Merge Text files")
        self.root.geometry("400x450")
        self.root.iconbitmap("logo3.ico")
        self.root.resizable(0,0)


        save=StringVar()
        path1=StringVar()
        path2=StringVar()




        def on_enter1(e):
            but_merge['background']="black"
            but_merge['foreground']="cyan"
            
            

        def on_leave1(e):
            but_merge['background']="SystemButtonFace"
            but_merge['foreground']="SystemButtonText"


        def on_enter2(e):
            but_browse1['background']="black"
            but_browse1['foreground']="cyan"
            
            

        def on_leave2(e):
            but_browse1['background']="SystemButtonFace"
            but_browse1['foreground']="SystemButtonText"


        def on_enter3(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
            
            

        def on_leave3(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"



        def on_leave4(e):
            but_browse2['background']="SystemButtonFace"
            but_browse2['foreground']="SystemButtonText"


        def on_enter4(e):
            but_browse2['background']="black"
            but_browse2['foreground']="cyan"

        
        def clear():
            path1.set("")
            save.set("")
            path2.set("")

        
        def browse():
            global filename
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("Text FILES","*.txt"),("all files","*.*"))) 
            path1.set(file_path)


        def browse1():
            global filename
            file_path = filedialog.askopenfilename(title = "Select file",filetypes = (("Text FILES","*.txt"),("all files","*.*"))) 
            path2.set(file_path)



        def merge():
            if len(path1.get())!=0:
                if len(path2.get())!=0:
                    if save.get()!=0:
                        with open(path1.get(),'r') as p1:
                            r1=p1.read()
                        with open(path2.get(),'r') as p2:
                            r2=p2.read()

                        with open('{}.txt'.format(save.get()),'w') as w:
                            w.write(r1+"\n"+r2)
                    else:
                        tkinter.messagebox.showerror("Error","Please Enter name for saving files")
                    
                    

                else:
                    tkinter.messagebox.showerror("Error","Please Select the txt path")
            else:
                tkinter.messagebox.showerror("Error","Please Select the txt path")


       
                    

             


#=====================frame======================================================#

        mainframe=Frame(self.root,width=400,height=450,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=394,height=400,relief="ridge",bd=3,bg="#48adf9")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=394,height=43,relief="ridge",bd=3,bg="#008c8c")
        secondframe.place(x=0,y=400)

#========================firstframe----------------------------------------------------------$
        but_browse1=Button(firstframe,text="Browse TEXT 1",width=16,font=('times new roman',12),cursor="hand2",command=browse)
        but_browse1.place(x=110,y=20)
        but_browse1.bind("<Enter>",on_enter2)
        but_browse1.bind("<Leave>",on_leave2)

        lab_path1=Label(firstframe,text="Path 1",font=('times new roman',12),bg="#48adf9",fg="white")
        lab_path1.place(x=170,y=70)

        ent_path1=Entry(firstframe,width=43,relief="ridge",bd=3,font=('times new roman',12),textvariable=path1)
        ent_path1.place(x=20,y=100)



        but_browse2=Button(firstframe,text="Browse TEXT 2",width=16,font=('times new roman',12),cursor="hand2",command=browse1)
        but_browse2.place(x=110,y=150)
        but_browse2.bind("<Enter>",on_enter4)
        but_browse2.bind("<Leave>",on_leave4)

        lab_path2=Label(firstframe,text="Path 2",font=('times new roman',12),bg="#48adf9",fg="white")
        lab_path2.place(x=170,y=190)

        ent_path2=Entry(firstframe,width=43,relief="ridge",bd=3,font=('times new roman',12),textvariable=path2)
        ent_path2.place(x=20,y=230)


        lab_save=Label(firstframe,text="Save as Name",font=('times new roman',12),bg="#48adf9",fg="white")
        lab_save.place(x=10,y=310)


        ent_save=Entry(firstframe,width=20,relief="ridge",bd=3,font=('times new roman',12),textvariable=save)
        ent_save.place(x=130,y=310)
        

#=======================secondframe===========================================================#
        
        but_merge=Button(secondframe,text="Merge",width=16,font=('times new roman',12),cursor="hand2",command=merge)
        but_merge.place(x=20,y=1)
        but_merge.bind("<Enter>",on_enter1)
        but_merge.bind("<Leave>",on_leave1)


        but_clear=Button(secondframe,text="Clear",width=16,font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=210,y=1)
        but_clear.bind("<Enter>",on_enter3)
        but_clear.bind("<Leave>",on_leave3)







if __name__ == "__main__":
    root=Tk()
    app=Merge(root)
    root.mainloop()





