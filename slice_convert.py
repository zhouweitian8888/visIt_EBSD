#!/usr/bin/python
# -*- coding: cp936 -*-
import xlsxwriter
import math
import os
import time
import sys
"""
sys.argv=[0,0,0,0,0,0,0,0]
sys.argv[1]=(r"C:\Users\zhouweitian\Desktop\test\slice_file")
sys.argv[2]=49
sys.argv[3]=20
sys.argv[4]=80
sys.argv[5]=20
sys.argv[6]=80
sys.argv[7]=4
"""
time.sleep(1)
print(sys.argv[1])
print(sys.argv[2])
slice_file_path=sys.argv[1]
N_angle=int(sys.argv[2])
time.sleep(1)
x_min=float(sys.argv[3])*int(sys.argv[7])
x_max=float(sys.argv[4])*int(sys.argv[7])
y_min=float(sys.argv[5])*int(sys.argv[7])
y_max=float(sys.argv[6])*int(sys.argv[7])

#input("Press Any Key")
#slice_file_path=r"C:\Users\zhouweitian\Desktop\test\slice_file"
#N_angle=49

xlsx_file_path=r"C:\Users\zhouweitian\Desktop\test\xlsx\\"

def angle(state_in):
    #N_angle=49   #it may change rapidly,note all.py
    Pi=3.141592654
    angle_per=[0,0,0]
    dim_number=[0,0,0]
    Euler=[0,0,0]
    angle_per[0]=1.0*Pi/N_angle
    angle_per[1]=1.0*Pi/N_angle
    angle_per[2]=1.0*Pi/N_angle
    
    state_num_per=state_in-600#状态对应的一维数组位置
    if state_num_per%((N_angle+1)*(N_angle+1))==0:
        dim_number[0]=N_angle+1
        dim_number[1]=N_angle+1
        dim_number[2]=state_num_per//((N_angle+1)*(N_angle+1))-1
    else:
        dim_number[0]=state_num_per%((N_angle+1)*(N_angle+1))%(N_angle+1)-1
        dim_number[1]=state_num_per%((N_angle+1)*(N_angle+1))//(N_angle+1)
        dim_number[2]=state_num_per//((N_angle+1)*(N_angle+1))
       #计算状态对应的三维数组位置
    
    Euler[0]=dim_number[0]*angle_per[0]
    Euler[1]=dim_number[1]*angle_per[1]
    Euler[2]=dim_number[2]*angle_per[2]


    return Euler




slice_file_all=os.listdir(slice_file_path)
file_count=0
while file_count<len(slice_file_all):
    time.sleep(2)
    workbook_path=str(xlsx_file_path+str(slice_file_all[file_count][:-4])+'.xlsx')
    workbook = xlsxwriter.Workbook(workbook_path)
    worksheet1=workbook.add_worksheet("test")
    style = workbook.add_format({
        'border': 1, # 边框
        'align': 'center', # 水平居中
        'valign': 'vcenter', # 垂直居中
        'bold': False, # 加粗（默认False）
        'font': u'宋体', # 字体
        'fg_color': 'white', # 背景色
        'color': 'black' #字体颜色
    })
    worksheet1.write(0,0,"Euler1",style)
    worksheet1.write(0,1,"Euler2",style)
    worksheet1.write(0,2,"Euler3",style)
    worksheet1.write(0,3,"Phase",style)
    worksheet1.write(0,4,"x",style)
    worksheet1.write(0,5,"y",style)
    worksheet1.write(0,6,"index",style)
    worksheet1.write(0,7,"state",style)
    with open(str(slice_file_path)+"\\"+str(slice_file_all[file_count])) as f:  # 打开文件
        data = f.read()  # 读取文件
        i=0
        i_line=0
        while i_line<9:
            i_line_test=data[i]
            if ord(i_line_test)==10:
                i_line=i_line+1
            i=i+1
        i_line_xlsx=1

        #for test
        #print(data[i:i+91])
        #print(data[i+92:i+183])
        #print(data[i+92])
        #for test

        while i<len(data):
            x=round((float(data[i:i+22]))*math.pow(10,6))
            y=round((float(data[i+23:i+45]))*math.pow(10,6))
            
            #y=float(data[i+23:i+45])
            state=int(float(data[i+69:i+91]))
            euler_angle=angle(state)
            #if 160<(x*math.pow(10,6))<318)&(82<(y*math.pow(10,6))<318):#20%-80%
            if  x>x_min and x<x_max and y>y_min and y<y_max :
                worksheet1.write(i_line_xlsx,4,x,style)
                worksheet1.write(i_line_xlsx,5,y,style)
                worksheet1.write(i_line_xlsx,0,euler_angle[0],style)
                worksheet1.write(i_line_xlsx,1,euler_angle[1],style)
                worksheet1.write(i_line_xlsx,2,euler_angle[2],style)
                if state>=550:
                    worksheet1.write(i_line_xlsx,3,1,style)
                    worksheet1.write(i_line_xlsx,6,"Indexed",style)
                else:
                    worksheet1.write(i_line_xlsx,3,0,style)
                    worksheet1.write(i_line_xlsx,6,"notIndexed",style)
                worksheet1.write(i_line_xlsx,7,state,style)
                i_line_xlsx=i_line_xlsx+1
                #print(1)
            i=i+92
            #print(i_line_xlsx,(x*math.pow(10,6)),(y*math.pow(10,6)))
            #print(data[i+69:i+90],state)
        print(str(workbook_path+'.xlsx')+" "+"end")
    workbook.close()
    file_count=file_count+1


