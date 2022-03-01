#!/usr/bin/python
import matlab
import matlab.engine
import time
import os
import sys

print("1")

#print("press any key")
eng=matlab.engine.start_matlab()
#print(sys.argv[1])
#pname_in,fname_in,pname_out_polefig,pname_out_grainfig
pname_in=str(sys.argv[1])

#pname_in=r"C:\Users\zhouweitian\Desktop\test\xlsx"
#fname_in="C:\Users\zhouweitian\Desktop\test\test.xlsx"
xlsx_file_all=os.listdir(pname_in)
file_count=0
while file_count<len(xlsx_file_all):
    fname_in=str(xlsx_file_all[file_count])
    print(fname_in)
    time.sleep(1)
    pname_out_polefig=str(r"C:\Users\zhouweitian\Desktop\test\polefig\\"+"p_"+xlsx_file_all[file_count][:-5]+".jpg")
    pname_out_grainfig=str(r"C:\Users\zhouweitian\Desktop\test\grainfig\\"+"g_"+xlsx_file_all[file_count][:-5]+".jpg")
    output=eng.plotebsd(pname_in,fname_in,pname_out_polefig,pname_out_grainfig,nargout=1)
    file_count=file_count+1
    print("2")
