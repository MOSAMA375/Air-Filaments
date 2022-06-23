#!/usr/bin/python3
import csv
import os

file = "pressurepoints.dat"
start =0
end = 9

istep = '{istep = 1}'

os.system('mkdir Pressure')
    
for i in range(start,end,1):
    input=f'input{i}'
    output=f'Pressure/pressure{i}'            
    converted_num = str(i)
    os.system(f"gerris3D -e 'OutputLocation {istep} {output} {input} ' snapshot-0.{converted_num.zfill(3)}.gfs > /dev/null")
