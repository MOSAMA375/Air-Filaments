#!/usr/bin/python3

import os
import csv

start_x=-122800
stop_x=125256
step_x=2456

start_n_x=-122800
stop_n_x=125256
step_n_x=2456

file_number=8

start_y=-200
stop_y=200
step_y=4

one=float(1.0)
zero=float(0.0)
output1=f'out_data{file_number}'
average1=f'averages'
output=f'averages{file_number}'

with open(average1,'w') as f:
    with open(output1, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ")
        for x in range(start_x, stop_x, step_x):
            for y in range(start_y, stop_y, step_y):
                sum=0
                sum_d=0
                conv_x=str(x/1000000)
                conv_y=str(y/10000)
                csvfile.seek(0)
                for row in csvreader:
                    if conv_x==row[1] and conv_y==row[2]:
                        conv_f=float(row[14])
                        conv_u=float(row[11])
                        fir_aver_n=(one-conv_f)*conv_u
                        sum+=fir_aver_n
                        fir_aver_d=(one-conv_f)
                        sum_d+=fir_aver_d

                    else:
                        pass
                f.write(f'{x/1000000} {y/10000} {sum/100} {sum_d/100}\n')
                print(f'{x/1000000} {y/10000} {sum/100} {sum_d/100}')
                
input=f'averages'

with open(output,'w') as f:
    with open(input, 'r') as csvfile:
        csvreader = csv.reader(csvfile, delimiter=" ")
        for x in range(start_n_x, stop_n_x, step_n_x):
            sum1=0
            sum2=0
            conv_x=str(x/1000000)
            csvfile.seek(0)
            for row in csvreader:
                if conv_x==row[0]:
                    new_conv_f=float(row[3])
                    new_conv_u=float(row[2])
                    sec_aver_u=(one-new_conv_f)*new_conv_u
                    sum1+=sec_aver_u
                    sec_aver_f=(one-new_conv_f)
                    sum2+=sec_aver_f
                else:
                    pass
            if sum2==zero:
                f.write(f'{x/1000000} {sum1/100} {1/1000000000}\n')
                print(f'{x/1000000} {sum1/100} {1/1000000000}')
            else:
                f.write(f'{x/1000000} {sum1/100} {sum2/100}\n')
                print(f'{x/1000000} {sum1/100} {sum2/100}')

os.system(f'rm  averages')
