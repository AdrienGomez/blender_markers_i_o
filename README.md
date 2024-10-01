# blender_markers_i_o
2 scripts. First, export timeline markers to csv. Second, import csv to timeline markers

## How To
### 1) Export markers

Open the blender file where you have timeline markers you want to export.

Go to the scripting workspace and open save_markers_to_csv.py

If you're not in the default 'Scene', change to your current scen in the python script. this line:     for marker in bpy.data.scenes['Scene'].timeline_markers:

A csv file with you markers data should have been created in the same directory as your blend file, with the same name.

### 2) Open the other blend file where you want to import marker

Go to the scripting workspace and open read_markers_from_csv.py

Chnage the path to your file in this line: csvfile = '/home/tests/markers.csv'

Markers should have been add to your timeline
