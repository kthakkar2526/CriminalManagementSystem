from tkinter import*
from  tkinter import ttk
from PIL import Image,ImageTk


class Criminal:
    def __init__(self,root):
        self.root = root
        self.root.geometry('1530x790+0+0')
        self.root.title('CRIMINAL MANAGEMENT SYSTEM')

        lbl_title = Label(self.root, text='CRIMINAL MANAGEMENT SYSTEM SOFTWARE',font=('times new roman',40,'bold'),bg='black',fg='gold')
        lbl_title.place(x=0,y=0,width=1530,height=70)

        # ncr logo
        img_logo = Image.open('Mumbai_Police_logo.png')
        img_logo = img_logo.resize((60,60),Image.ANTIALIAS)
        self.photo_logo = ImageTk.PhotoImage(img_logo)

        self.logo = Label(self.root,image=self.photo_logo)
        self.logo.place(x=80,y=5,width=60,height=60)

        #img frame
        """ 
        img_frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        img_frame.place(x=0,y=70,width=1530,height=130)

        img1 = Image.open('Mumbai_Police_logo.png')
        img1 = img1.resize((540, 160), Image.ANTIALIAS)
        self.photo1 = ImageTk.PhotoImage(img1)

        self.img1 = Label(self.root, image=self.photo1)
        self.img1.place(x=0, y=70, width=540, height=160)

        img2 = Image.open('Mumbai_Police_logo.png')
        img2 = img2.resize((540, 160), Image.ANTIALIAS)
        self.photo2 = ImageTk.PhotoImage(img2)

        self.img2 = Label(self.root, image=self.photo2)
        self.img2.place(x=540, y=70, width=540, height=160)

        img3 = Image.open('Mumbai_Police_logo.png')
        img3 = img3.resize((540, 160), Image.ANTIALIAS)
        self.photo3 = ImageTk.PhotoImage(img3)

        self.img3 = Label(self.root, image=self.photo3)
        self.img3.place(x=1080, y=70, width=540, height=160)
        """

        #Main Frame
        Main_Frame = Frame(self.root,bd=2,relief=RIDGE,bg='white')
        Main_Frame.place(x=10,y=200,width=1500,height=560)

        #Upper Frame
        upper_Frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, text='Criminal Information',font=('times new roman',11,'bold'),fg='red',bg='white')
        upper_Frame.place(x=10, y=10, width=1480, height=270)

        #Labels Entry

        #case id
        caseid = Label(upper_Frame,text='Case ID:',font=('times new roman', 11, 'bold'), fg='red', bg='white')



        #Down Frame
        down_Frame = LabelFrame(Main_Frame, bd=2, relief=RIDGE, text='Criminal Information Table',
                                 font=('times new roman', 11, 'bold'), fg='red', bg='white')
        down_Frame.place(x=10, y=280, width=1480, height=270)

        search_Frame = LabelFrame(down_Frame, bd=2, relief=RIDGE, text='Search Criminal Record',
                                font=('times new roman', 11, 'bold'), fg='red', bg='white')
        search_Frame.place(x=0, y=0, width=1470, height=60)

        #buttons
        button_frame = Frame(upper_Frame, bd = 2,relief=RIDGE, bg='white')
        button_frame.place(x=5,y=200,width=640,height=45)

        #add button
        btn_add = Button(button_frame,text='Record Save',font=("arial",13,"bold"),width=14, bg='blue', fg='white')
        btn_add.grid(row=0, column=0, padx=3, pady=5)
if __name__=="__main__":
    root=Tk()
    obj = Criminal(root)
    root.mainloop()