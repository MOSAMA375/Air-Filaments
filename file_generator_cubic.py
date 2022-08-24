#!/usr/bin/python3

import numpy as np

start_x=-320
stop_x=384
step_x=64

start_y=-150
stop_y=150
step_y=3

start_z=-150
stop_z=150
step_z=3

output=f'data_points'

with open (output, 'w') as f:
    for i in np.arange(start_x, stop_x, step_x):
        for j in np.arange(start_y, stop_y, step_y):
            for k in np.arange(start_z, stop_z, step_z):
                f.write(f'{i/1000} {j/10000} {k/10000}\n')
                
