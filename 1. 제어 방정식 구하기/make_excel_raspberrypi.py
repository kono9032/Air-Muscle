import serial
import matplotlib.pyplot as plt
import time
import sys
from itertools import count
import matplotlib.animation as animation
import numpy as np
import matplotlib.ticker as ticker
import pandas as pd

print('serial ' + serial.__version__)
PORT = 'COM7' 
BaudRate = 9600 
ARD= serial.Serial(PORT,BaudRate)

alist = []
x_val=[]

press = []
lengh = []
normalize = []

index = count()

start = time.time()

while (True):
    sys.stdout.write("<---Timer \r{} ".format(str(round(time.time() - start,3))))

    if ARD.readable():
        res = ARD.readline()
        original_sig = res.decode()[:len(res)-2]

        if(round(time.time() - start,3)>=5.0):
            alist.append(original_sig)
            print(original_sig)

        if (round(time.time() - start,3)>=10.0):
            print(len(alist))
            print("fin", time.time() - start)
            break

for ii in range(len(alist)-1):
    split_list_or = alist[ii].split(',')
    split_list_or2 = alist[ii+1].split(',')

    if float(split_list_or[0]) == float(split_list_or2[0]):
        normalize.append(float(split_list_or[1]))

    elif float(split_list_or[0]) != float(split_list_or2[0]):
        if not normalize:
            press.append(float(split_list_or[0]))
            lengh.append(float(split_list_or[1]))

        elif normalize:
            press.append(float(split_list_or[0]))

            normalize.append(float(split_list_or[1]))
            nomal = np.mean(normalize)
            lengh.append(nomal)

            normalize.clear()

for n in count(1):
    x_val.append(next(index))
    if len(x_val) == len(press):
        break

raw_data = {'press' : press, 'lengh' : lengh}
raw_data = pd.DataFrame(raw_data)
raw_data.to_excel(excel_writer='original_sig333.xlsx', index=False)

print('x_val:',x_val)
print('press:',press)
print('len(x_val):',len(x_val))
print('len(press):',len(press))
print('len(lengh):',len(lengh))

plt.cla()
plt.plot(press, lengh, label='lengh-press')

plt.xlabel=('press')
plt.ylabel('lengh')

plt.legend(loc='upper left')

plt.tight_layout()
plt.show()