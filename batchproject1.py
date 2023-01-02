# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:37:17 2023

@author: Swastik
"""

import csv
p=open("Batch.csv","w",newline='') 
data=csv.writer(p)
data.writerow(["BatchID","BatchName","DepartmentName","ListofCourse","ListofStudent"])
for i in range (3):
    BatchID=input("EnterBatchID")
    BatchName=input("EnterBatchName")
    DepartmentName=input("EnterDepartmentName")
    ListofCourse=input("EnterListofCourse")
    ListofStudent=input("EnterListofStudent")
    info=[BatchID,BatchName,DepartmentName,ListofCourse,ListofStudent]
    data.writerow(info)
import csv
import matplotlib.pyplot as plt

def display_students():
    with open("batch.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==3:
                print(i)

def display_courses():
    with open("batch.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==4:
                print(i[0])

def pie_chart():
    name=[]
    marks=[]
    with open("batch.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==3:
                name.append(i[0])
                marks.append(i[2])
    plt.pie(marks,labels=name)
    plt.title("% MARKS DISTRIBUTION")
    plt.show()