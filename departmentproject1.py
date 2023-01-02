# -*- coding: utf-8 -*-
"""
Created on Sun Jan  1 18:54:44 2023

@author: Swastik
"""

import csv
p=open("Department.csv","w",newline='')
data=csv.writer(p)
data.writerow(["DepartmentID","DepartmentName","ListofBatches"])
for i in range (2):
    DepartmentID=input("Enter Department ID")
    DepartmentName=input("Enter Name")
    ListofBatches=input("Enter Class Roll Number")
    info=[DepartmentID,DepartmentName,ListofBatches]
    data.writerow(info)
p.close()

import csv
import matplotlib.pyplot as plt


def display_batches():
    with open("department.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==1:
                print(i)

def batch_performance():
    with open("department.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==2:
                print(i)

def line_plot():
    bname=[]
    marks=[]
    with open("department.csv", "r") as obj:
        obj.seek(0)
        robj = csv.reader(obj)
        for i in robj:
            if len(i)==2:
                bname.append(i[0])
                marks.append(int(i[1]))
    print(bname)
    print(marks)
    plt.plot(bname,marks,marker="o")
    plt.xlabel("BATCH NAME")
    plt.ylabel("% MARKS")
    plt.title("% MARKS DISTRIBUTION FOR EACH BATCH")
    plt.show()

display_batches()
batch_performance()
line_plot()