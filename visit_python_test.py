#!/usr/bin/python
import os
import sys
import time



#sys.path.append('C:\Program Files\LLNL\VisIt 3.1.4')
#sys.path.insert(0,"C:\Program Files\LLNL\VisIt 3.1.4\lib\site-packages")
#os.getcwd()
os.chdir('C:\Program Files\LLNL\VisIt 3.1.4')
visit_path=r"C:\Program Files\LLNL\VisIt 3.1.4\lib\site-packages\visit"
#print(visit_path)
os.chdir(visit_path)
print('1')
import visit
print('1')

visit.Launch()

print('1')
print(sys.argv[1])
print(sys.argv[2])
print(sys.argv[3])
print(sys.argv[4])


visit_file_path=str(sys.argv[1])
slice_begin=float(sys.argv[2])
slice_stop=float(sys.argv[3])
slice_single=float(sys.argv[4])


"""
visit_file_path=(r"C:\Users\zhouweitian\Desktop\test\visit_file")
slice_begin=20
slice_stop=40
slice_single=2
"""
visit_file_all=os.listdir(visit_file_path)
print(visit_file_all)

visit.CloseComputeEngine
visit.OpenComputeEngine("localhost", ("-np", "4", "-nn", "1"))
visit.DeleteActivePlots()

file_count=0
while file_count<len(visit_file_all):
    #file_open_path="localhost:C:\\Users\\zhouweitian\\Desktop\\test\\visit_file\\"+visit_file_all[file_count]
    file_open_path=r"localhost:"+visit_file_path+"\\"+visit_file_all[file_count]
    #visit.OpenDatabase("localhost:C:\\Users\\zhouweitian\\Desktop\\test\\visit_file\\010", 0)
    #visit.OpenDatabase(str("localhost:C:\\Users\\zhouweitian\\Desktop\\test\\visit_file\\",sys.argv[1]), 0)
    visit.OpenDatabase(file_open_path, 0)
    visit.AddPlot("Pseudocolor", "data/state", 1, 1)
    visit.DrawPlots()
    visit.SetActivePlots(0)
    visit.SetActivePlots(0)
    i=slice_begin
    

    while i<slice_stop:
        visit.AddOperator("Slice", 1)
        visit.SliceAtts = visit.SliceAttributes()
        visit.SliceAtts.originType = visit.SliceAtts.Percent  # Point, Intercept, Percent, Zone, Node
        visit.SliceAtts.originPoint = (0, 0, 0)
        visit.SliceAtts.originIntercept = 0
        visit.SliceAtts.originPercent = i #slice percent
        visit.SliceAtts.originZone = 0
        visit.SliceAtts.originNode = 0
        visit.SliceAtts.normal = (-1, 0, 0)
        visit.SliceAtts.axisType = visit.SliceAtts.XAxis  # XAxis, YAxis, ZAxis, Arbitrary, ThetaPhi
        visit.SliceAtts.upAxis = (0, 1, 0)
        visit.SliceAtts.project2d = 1
        visit.SliceAtts.interactive = 1
        visit.SliceAtts.flip = 0
        visit.SliceAtts.originZoneDomain = 0
        visit.SliceAtts.originNodeDomain = 0
        visit.SliceAtts.meshName = "data/mesh1"
        visit.SliceAtts.theta = 90
        visit.SliceAtts.phi = 0
        visit.SetOperatorOptions(visit.SliceAtts, 0, 1)
        visit.DrawPlots()

        visit.IconifyAllWindows()
        visit.DeIconifyAllWindows()
        visit.ExportDBAtts = visit.ExportDBAttributes()
        visit.ExportDBAtts.allTimes = 0
        
        visit.ExportDBAtts.dirname = "C:/Users/zhouweitian/Desktop/test//slice_file"
        fname="slice"+"_"+visit_file_all[file_count]+"_"+str(i)
        #fname="slice"+str(i)
        
        visit.ExportDBAtts.filename = fname
        
        visit.ExportDBAtts.timeStateFormat = "_%04d"
        visit.ExportDBAtts.db_type = "Xmdv"
        visit.ExportDBAtts.db_type_fullname = "Xmdv_1.0"
        visit.ExportDBAtts.variables = ()
        visit.ExportDBAtts.writeUsingGroups = 0
        visit.ExportDBAtts.groupSize = 48
        visit.DBExportOpts = {'Export coordinates?': 1}
        visit.ExportDatabase(visit.ExportDBAtts, visit.DBExportOpts)
        visit.RemoveOperator(0, 1)
        i=i+slice_single
        print(i)
    visit.DeleteActivePlots()
    file_count=file_count+1
visit.CloseComputeEngine

