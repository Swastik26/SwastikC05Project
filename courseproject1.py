# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:18:48 2023

@author: Swastik
"""

import csv
p=open("Courseproj.csv","w",newline='')
data=csv.writer(p)
data.writerow(["CourseID","CourseName","Marksobtained"])
for i in range (2):
    CourseID=input("EnterCourseID")
    CourseName=input("EnterCourseName")
    Marksobtained=input("Enter MarksOtained")
    info=[CourseID,CourseName,Marksobtained]
    data.writerow(info)
p.close()
import csv
import matplotlib.pyplot as plt

def display_courses():
    with open("course.csv", "r") as obj:
        obj.seek(0)
        robj=csv.reader(obj)
        for i in robj:
            print(i)

def histogram():
    l=[]
    with open("course.csv","r") as obj:
        robj=csv.reader(obj)
        for i in robj:
            if len(i)==3:
                l.append(int(i[2]))
        print(l)
    k=[0,10,20,30,40,50,60,70,80,90,100]
    plt.hist(l,bins=k,rwidth=0.8)
    plt.xlabel("GRADES")
    plt.ylabel("NUMBER OF STUDENTS")
    plt.title("COURSE STATISTICS")
    plt.xticks(k)
    plt.show()


