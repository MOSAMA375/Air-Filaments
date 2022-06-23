#!/usr/bin/python3

import numpy as np

start=-5
stop=5
step=1
i=69
output=f'output{i}'

with open (output, 'w') as f:
    for i in np.arange(start, stop, step):
        f.write(f'{i*0.01} {0} {0}\n')
