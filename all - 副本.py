# -*- coding: cp936 -*-
import os
import time


time_start=time.time()
mesh_size=4 #μm
#################################################################

def del_file(path_data):
    for i in os.listdir(path_data) :# os.listdir(path_data)#??????????????????????????
        file_data = path_data + "\\" + i#??????????????????
        if os.path.isfile(file_data) == True:
            os.remove(file_data)
        else:
            del_file(file_data)
path_data_slice_file = r"C:\Users\zhouweitian\Desktop\test\slice_file"
path_data_xlsx_file=r"C:\Users\zhouweitian\Desktop\test\xlsx"
del_file(path_data_slice_file)
del_file(path_data_xlsx_file)

#################################################################

print("slice_start")
visit_slice_begin=30
visit_slice_stop=32
visit_slice_single=1
visit_file_path=(r"C:\Users\zhouweitian\Desktop\test\visit_file\120")
#visit_file_path=(r"G:\low56%")
#visit_file_all=os.listdir(visit_file_path)

print(visit_file_path) 

os.system("visit_python_test.py %s %f %f %f" %(visit_file_path,visit_slice_begin,visit_slice_stop,visit_slice_single))
print("slice_over")

##################################################################

print("convert_start")
slice_file_path_for_convert=(r"C:\Users\zhouweitian\Desktop\test\slice_file")
N_angle_for_convert=49
# note the flip, the x is the real y,and the y is the real x
#convert_x_min=0
#convert_x_max=600/4
#convert_y_min=0
#convert_y_max=640/4


convert_x_min=0
convert_x_max=2000/4
convert_y_min=0
convert_y_max=600/4

os.system("slice_convert.py %s %d %f %f %f %f %d" %(slice_file_path_for_convert,N_angle_for_convert,convert_x_min,convert_x_max,convert_y_min,convert_y_max,mesh_size))

print("convert_stop")

##################################################################

print("EBSD_PLOT_start")
xlsx_file_path_for_ebsd=(r"C:\Users\zhouweitian\Desktop\test\xlsx")
os.system("matlab_to_python.py %s" %(xlsx_file_path_for_ebsd))
print("EBSD_PLOT_end")

time_end=time.time()
print('totally cost',time_end-time_start)


