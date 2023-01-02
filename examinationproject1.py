# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 19:02:14 2023

@author: Swastik
"""

import csv
p=open("Examination.csv","w",newline='')
data=csv.writer(p)
data.writerow(["CourseName","StudentRollNumber","ExaminationMarks"])
for i in range (6):
    CourseName=input("CourseName")
    StudentRollNumber=input("StudentRollNumber")
    ExaminationMarks=int(input("ExaminationMarks"))
    info=[CourseName,StudentRollNumber,ExaminationMarks]
    data.writerow(info)
p.close()


import csv
import matplotlib.pyplot as plt


def student_performance():
    with open("examination.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==2:
                print(i)

def scatter_plot():
    batch=[]
    marks=[]
    with open("examination.csv","r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            batch.append(i[0])
            marks.append(int(i[3]))

    plt.scatter(marks,batch,color="r")
    plt.title("MARKS OBTAINED IN DIFFERENT COURSES BY VARIOUS BATCHES")
    plt.xlabel("MARKS")
    plt.ylabel("BATCHES")
    plt.show()
