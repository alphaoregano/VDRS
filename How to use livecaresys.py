'''
livecaresys is a python file to detect and recognize cars in real time.
To use livecaresys, you need to call livecaresysfunc().

How to use livecaresysfunc()?

Syntax:
res = livecaresysfunc(arg1, arg2, arg3, arg4)

arg1 = url of live video image(eg: "http://sample1.jpg")
arg2 = delay between two frames in seconds (eg: 1)
arg3 = name of .py file without extension of the
function in which you want the output (eg: 'test')
arg4 = name of the function (eg: 'testing')
arg5 = 'us' or 'in'

livecaresysfunc() returns a list of lists of each frame details.
The list of each frame contains one or more tuples which carry details of vechicles.

'IP Webcam' is the android app which is used for this purpose.

Example:
from livecaresys import *
livecaresysfunc("http://192.168.43.1:7080/shot.jpg?rnd=557137", 0, 'test', 'testing', 'us')
'''
from livecaresys import *
livecaresysfunc("http://192.168.43.1:7000/stream.mjpeg",5,'How to use livecaresys','testing','us')

def testing(vehicles):
    print(vehicles)

#run this file to get the output printed in the shell
#the output will be passed on as a parameter to the function mentioned in arg4 which is present in the file mentioned in arg3 of the livecaresysfunc() function.
