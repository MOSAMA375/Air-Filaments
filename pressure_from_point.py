#!/usr/bin/python3
import csv
import os

num_files=10
num_files1=10
num_lines=50

file = "pressurepoints.dat"
istep = '{istep = 1}'

os.system('mkdir Pressure')

with open(file,'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    for mytime in range(num_files):
        i = 0
        for row in csvreader:
            output=f'Pressure/pressure{mytime}_{i}'
            data_points = f'{row[0]} {row[1]} {row[2]}'            
            converted_num = str(mytime)
            print(data_points, output)
            os.system(f"gerris3D -e 'OutputLocation {istep} {output} {data_points} ' snapshot-0.{converted_num.zfill(3)}.gfs > /dev/null")
            i=i+1
            if i == num_lines:
                break

for i in range(num_files1):
    file1 = f'output{i}'
    with open (file1,'a') as j:
        for time in range(num_lines):
            output=f'Pressure/pressure{i}_{time}'
            with open(output,'r') as k:
                j.write(k.readlines()[1])
