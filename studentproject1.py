# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:08:34 2023

@author: Swastik
"""
import csv
p=open("Student.csv","a",newline='')
data=csv.writer(p)
data.writerow(["StudentID","Name","ClassRollNumber","BatchID"])
for i in range (4):
    StudentID=input("EnterStudentID")
    Name=input("EnterName")
    ClassRollNumber=int(input("EnterClassRollNumber"))
    BatchID=input("EnterBatchID")
    info=[StudentID,Name,ClassRollNumber,BatchID]
    data.writerow(info)


def student_display():
    with open("student.csv", "a") as obj:
        obj.seek(0)
        robj=csv.reader(obj)
        for i in robj:
            print(i)

def student_update():
    with open("student.csv", "a") as obj:
        robj=csv.reader(obj)    
        L=[]
        found=False
        fid = input("Enter Student ID to edit data ")
        for i in robj:
            if i[0]==fid:
                found=True
                nid=input("Enter new Student ID ")
                name=input("Enter new Name ")
                roll=input("Enter new Class Roll Number ")
                batch=input("Enter new Batch Name ")
                i[0]=nid
                i[1]=name
                i[2]=roll
                i[3]=batch
            else:
                print("Student not found")
            L.append(i)

    if found==False:
        print("Student cannot be found")
    else:
        with open("student.csv", "w+", newline="") as obj:
            wobj=csv.writer(obj)
            wobj.writerows(L)
            obj.seek(0)
            robj=csv.reader(obj)
            for i in robj:
                print(i)

def student_delete():
    with open("student.csv", "a") as obj:
        robj=csv.reader(obj)
        L=[]
        found=False
        fid = input("Enter Student ID to delete data ")
        for i in robj:
            if i[0]==fid:
                found=True
            else:
                print("Student not found")
                L.append(i)
                



    if found==False:
        print("Student cannot be found")
    else:
        with open("student.csv", "w+", newline="") as obj:
            wobj = csv.writer(obj)
            wobj.writerows(L)
            obj.seek(0)
            robj = csv.reader(obj)
            for i in robj:
                print(i)

def report_card():
     name=input("Enter the name of the student ")
     a="report_card_"+ name
     with open(a+".txt","w") as obj:
        num=int(input("enter number of subjects "))
        for i in range(num):
            sub=input("enter subject ")
            marks=int(input("enter marks out of 100 "))
            if marks>=90:
                grade="A"
            elif marks>=80:
                grade="B"
            elif marks>=70:
                grade="C"
            elif marks>=60:
                grade="D"
            elif marks>=50:
                grade="E"
            else:
                grade="F"
            if grade == "F":
                result = "FAIL"
            else:
                result = "PASS"
            k=[sub," ",str(marks)," ",str(grade)," ",result,"\n"]
            obj.writelines(k)

student_display()
#student_update()
#student_delete()   
report_card()     