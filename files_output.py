#!/usr/bin/python3

import os

start = 0
end = 2
step = 1
data_points='data_points'
istep = '{istep = 1}'

os.system('mkdir Averages')

for x in range(start, end, step):
    converted_num = str(x)
    out_data=f'Averages/out_data{x}'
    os.system(
        f"gerris3D -e 'OutputLocation {istep} {out_data} {data_points} ' snapshot-0.{converted_num.zfill(3)}.gfs > /dev/null")
