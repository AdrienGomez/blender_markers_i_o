import bpy
import csv
import os

#get file name without extension
filename=bpy.path.display_name_from_filepath(bpy.data.filepath)

#get absolute path
currentfile = bpy.data.filepath

#get directory path
filedir= os.path.dirname(currentfile)+'/'

#create csv file
with open(filedir+filename+'.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    #define column
    field = ["name", "frame"]
    #write columns' names
    #writer.writerow(field)
    
    #loop through scene timeline markers and add them to csv
    for marker in bpy.data.scenes['Scene'].timeline_markers:
        writer.writerow([marker.name, marker.frame])