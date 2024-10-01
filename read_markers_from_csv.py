import bpy
import csv

#absolutepath to csv file
csvfile = '/home/tests/markers.csv'

# Open csv file  
with open(csvfile) as file_obj: 
      
    # Create reader object by passing the file  
    # object to reader method 
    reader_obj = csv.reader(file_obj) 
      
    # Iterate over each row in the csv  
    # file using reader object 
    for row in reader_obj: 
        print(row[0])
        bpy.data.scenes['Scene'].timeline_markers.new(row[0],frame=int(row[1]))
