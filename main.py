[09:44, 4/20/2023] Pragati Patil: from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Face_Recognition_System:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\face-recognition-attendance-system.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=130)

        #second image
        img1=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\images (1).jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=130)

        #third image
        img2=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\images.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=130)

        #fourth image
        img3=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\face-768x512.jpg")
        img3=img3.resize((1530,660),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=130,width=1530,height=660)

        title_lbl=Label(bg_img,text="FACE RECOGNITION ATTENDANCE SYSTEM",font=("times new roman",35,"bold"),bg="white",fg="red")
        title_lbl.place(x=0,y=0,width=1400,height=40)

        #student button
        img4=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\face-recognition-attendance-system.png")
        img4=img4.resize((1530,660),Image.ANTIALIAS)
        self.photoimg4=ImageTk.PhotoImage(img4)

        b1_1=Button(bg_img,text="Student Detail",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_1.place(x=200,y=120,width=220,height=180)

        b1_2=Button(bg_img,text="Detect Face",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_2.place(x=500,y=120,width=220,height=180)

        b1_3=Button(bg_img,text="Attendance",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_3.place(x=800,y=120,width=220,height=180)

        b1_4=Button(bg_img,text="Help Desk",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_4.place(x=1100,y=120,width=220,height=180)

        b1_5=Button(bg_img,text="Train Data",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_5.place(x=200,y=350,width=220,height=180)

        b1_6=Button(bg_img,text="Photos",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_6.place(x=500,y=350,width=220,height=180)

        b1_7=Button(bg_img,text="Developer",cursor="hand2",font=("times new roman",14,"bold"),bg="red",fg="white")
        b1_7.place(x=800,y=350,width=220,height=180)



if _name_ == "_main_":
    root = Tk()
    obj = Face_Recognition_System(root)
    root.mainloop()
[09:45, 4/20/2023] Pragati Patil: home page
[09:45, 4/20/2023] Pragati Patil: from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk


class Student:
    def _init_(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        #first image
        img=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\face-recognition-attendance-system.jpg")
        img=img.resize((500,130),Image.ANTIALIAS)
        self.photoimg=ImageTk.PhotoImage(img)

        f_lbl=Label(self.root,image=self.photoimg)
        f_lbl.place(x=0,y=0,width=500,height=100)

        #second image
        img1=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\images (1).jpg")
        img1=img1.resize((500,130),Image.ANTIALIAS)
        self.photoimg1=ImageTk.PhotoImage(img1)

        f_lbl=Label(self.root,image=self.photoimg1)
        f_lbl.place(x=500,y=0,width=500,height=100)

        #third image
        img2=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\images.jpg")
        img2=img2.resize((500,130),Image.ANTIALIAS)
        self.photoimg2=ImageTk.PhotoImage(img2)

        f_lbl=Label(self.root,image=self.photoimg2)
        f_lbl.place(x=1000,y=0,width=500,height=100)

        #fourth image
        img3=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\face-768x512.jpg")
        img3=img3.resize((1530,600),Image.ANTIALIAS)
        self.photoimg3=ImageTk.PhotoImage(img3)

        bg_img=Label(self.root,image=self.photoimg3)
        bg_img.place(x=0,y=110,width=1530,height=600)

        title_lbl=Label(bg_img,text="STUDENT MANAGEMENT SYSTEM",font=("times new roman",30,"bold"),bg="white",fg="green")
        title_lbl.place(x=0,y=0,width=1400,height=30)

        main_frame=Frame(bg_img,bd=2)
        main_frame.place(x=0,y=35,width=1500,height=680)

        #left side label frame
        left_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Details",font=("times new roman",12,"bold"))
        left_frame.place(x=10,y=10,width=730,height=670)

        img_left=Image.open(r"C:\Users\ADMIN\Desktop\face recognition system\college_image\close-up-of-studying-student-hands-writing-in-book-during-lecture-education-students-college-of-university-reading-learning-and-exam-education-conc-2G7GFYP.jpg")
        img_left=img_left.resize((720,130),Image.ANTIALIAS)
        self.photoimg_left=ImageTk.PhotoImage(img_left)

        f_lbl=Label(left_frame,image=self.photoimg_left)
        f_lbl.place(x=50,y=0,width=650,height=110)

        #current course
        current_course_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Current Course",font=("times new roman",12,"bold"))
        current_course_frame.place(x=15,y=110,width=730,height=110)

        #department
        dep_label=Label(current_course_frame,text="Department",font=("times new roman",12,"bold"),bg="white")
        dep_label.grid(row=0,column=0,padx=10)

        dep_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only")
        dep_combo["values"]=("Select Depertment","Computer","IT","Civil","Mechanical")
        dep_combo.current(0)
        dep_combo.grid(row=0,column=1,padx=2,pady=10,sticky=W)

        #course
        course_label=Label(current_course_frame,text="course",font=("times new roman",12,"bold"),bg="white")
        course_label.grid(row=0,column=2,padx=10,sticky=W)

        course_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only")
        course_combo["values"]=("Select Course","FE","SE","TE","BE")
        course_combo.current(0)
        course_combo.grid(row=0,column=3,padx=2,pady=10,sticky=W)

        #year
        year_label=Label(current_course_frame,text="Year",font=("times new roman",12,"bold"),bg="white")
        year_label.grid(row=1,column=0,padx=10,sticky=W)

        year_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only")
        year_combo["values"]=("Select Year","2020-21","2021-22","2022-23","2023-24")
        year_combo.current(0)
        year_combo.grid(row=1,column=1,padx=2,pady=10,sticky=W)

        #semester
        semester_label=Label(current_course_frame,text="Semester",font=("times new roman",12,"bold"),bg="white")
        semester_label.grid(row=1,column=2,padx=10,sticky=W)

        semester_combo=ttk.Combobox(current_course_frame,font=("times new roman",12,"bold"),state="read only")
        semester_combo["values"]=("Select semester","sem-I","sem-II","sem-III","sem-IV","sem-V","sem-VI","sem-VII","sem-VIII")
        semester_combo.current(0)
        semester_combo.grid(row=1,column=3,padx=2,pady=10,sticky=W)

        #class student information
        class_student_frame=LabelFrame(left_frame,bd=2,bg="white",relief=RIDGE,text="Class student information",font=("times new roman",12,"bold"))
        class_student_frame.place(x=15,y=220,width=720,height=330)

        #student ID
        studentID_label=Label(class_student_frame,text="Student ID:",font=("times new roman",12,"bold"),bg="white")
        studentID_label.grid(row=0,column=0,padx=10,pady=5,sticky=W)

        studentID_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentID_entry.grid(row=0,column=1,padx=10,pady=5,sticky=W)

        #student name
        studentname_label=Label(class_student_frame,text="Student Name:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=0,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=0,column=3,padx=10,pady=5,sticky=W)

        #class division
        studentdiv_label=Label(class_student_frame,text="Student Division:",font=("times new roman",12,"bold"),bg="white")
        studentdiv_label.grid(row=1,column=0,padx=10,pady=5,sticky=W)

        studentdiv_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentdiv_entry.grid(row=1,column=1,padx=10,pady=5,sticky=W)

        #roll no
        studentname_label=Label(class_student_frame,text="Roll No:",font=("times new roman",12,"bold"),bg="white")
        studentname_label.grid(row=1,column=2,padx=10,pady=5,sticky=W)

        studentname_entry=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        studentname_entry.grid(row=1,column=3,padx=10,pady=5,sticky=W)

        #gender
        gender_label=Label(class_student_frame,text="Gender:",font=("times new roman",12,"bold"),bg="white")
        gender_label.grid(row=2,column=0,padx=10,pady=5,sticky=W)

        gender_label=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        gender_label.grid(row=2,column=1,padx=10,pady=5,sticky=W)

        #DOB
        dob_label=Label(class_student_frame,text="DOB:",font=("times new roman",12,"bold"),bg="white")
        dob_label.grid(row=2,column=2,padx=10,pady=5,sticky=W)

        dob_label=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        dob_label.grid(row=2,column=3,padx=10,pady=5,sticky=W)

        #email
        email_label=Label(class_student_frame,text="Email:",font=("times new roman",12,"bold"),bg="white")
        email_label.grid(row=3,column=0,padx=10,pady=5,sticky=W)

        email_label=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        email_label.grid(row=3,column=1,padx=10,pady=5,sticky=W)

        #phone no
        phone_label=Label(class_student_frame,text="Phone No:",font=("times new roman",12,"bold"),bg="white")
        phone_label.grid(row=3,column=2,padx=10,pady=5,sticky=W)

        phone_label=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        phone_label.grid(row=3,column=3,padx=10,pady=5,sticky=W)

        #Address
        addr_label=Label(class_student_frame,text="Address:",font=("times new roman",12,"bold"),bg="white")
        addr_label.grid(row=4,column=0,padx=10,pady=5,sticky=W)

        addr_label=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        addr_label.grid(row=4,column=1,padx=10,pady=5,sticky=W)

        #teacher name
        teachername_label=Label(class_student_frame,text="Gender",font=("times new roman",12,"bold"),bg="white")
        teachername_label.grid(row=4,column=2,padx=10,pady=5,sticky=W)

        teachername_label=ttk.Entry(class_student_frame,width=20,font=("times new roman",13,"bold"))
        teachername_label.grid(row=4,column=3,padx=10,pady=5,sticky=W)

        #radio button
        radiobutton1=ttk.Radiobutton(class_student_frame,text="Take photo sample",value="yes")
        radiobutton1.grid(row=6,column=0)

        radiobutton2=ttk.Radiobutton(class_student_frame,text="No photo sample",value="yes")
        radiobutton2.grid(row=6,column=1)

        #bbuttons frame
        btn_frame=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame.place(x=0,y=200,width=725,height=35)

        save_btn=Button(btn_frame,text="Save",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        save_btn.grid(row=0,column=0)

        update_btn=Button(btn_frame,text="Update",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_btn.grid(row=0,column=1)

        delete_btn=Button(btn_frame,text="Delete",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        delete_btn.grid(row=0,column=3)

        reset_btn=Button(btn_frame,text="Reset",width=17,font=("times new roman",13,"bold"),bg="blue",fg="white")
        reset_btn.grid(row=0,column=4)


        btn_frame1=Frame(class_student_frame,bd=2,relief=RIDGE)
        btn_frame1.place(x=0,y=235,width=725,height=35)

        take_photo_btn=Button(btn_frame1,text="Take photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        take_photo_btn.grid(row=0,column=0)

        update_photo_btn=Button(btn_frame1,text="Update photo sample",width=35,font=("times new roman",13,"bold"),bg="blue",fg="white")
        update_photo_btn.grid(row=0,column=1)

        #right side label frame
        right_frame=LabelFrame(main_frame,bd=2,bg="white",relief=RIDGE,text="Student Detail",font=("times new roman",12,"bold"))
        right_frame.place(x=750,y=10,width=720,height=580)










if _name_ == "_main_":
    root = Tk()
    obj = Student(root)
    root.mainloop()
