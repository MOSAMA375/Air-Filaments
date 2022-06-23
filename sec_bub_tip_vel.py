#!/usr/bin/python3

import os
import csv

# csv file name
istep = '{istep = 1}'
filename = "Interface/2r_min.dat"
# collect names
start = 4
start1=4
end = 8
# initialize rows

with open(filename, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=" ") 
    for row in csvreader:
        converted_num = str(start)
        output = f'test/output{start}'
        data_points = f'{row[0]} {row[1]} {row[2]}'
        os.system(f"gerris3D -e 'OutputLocation {istep} {output} {data_points} ' snapshot-0.{converted_num.zfill(3)}.gfs > /dev/null")
        start= start+1  

file = '1output'
if(os.path.exists(file)):
    os.remove(file)

for n in range(start1, end , 1):
    with open(file, 'a') as output1:
        with open(f'test/output{n}', 'r') as f:
            output1.write(f.readlines()[1])
