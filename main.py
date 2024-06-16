import time
import numpy as np
import matplotlib.pyplot as plt
import math

# get the local time, store hour and minute
t = time.localtime()
hour = t.tm_hour%12
minute = t.tm_min

# calculate angle of both hour hand and minute hand
hour_angle = 90 - ((hour * 30) + (minute * 0.5)) % 360
min_angle = 90 - ((minute * 6) %360)
print(hour_angle)
print(min_angle)

# draw circle for clock
theta = np.linspace( 0 , 2 * np.pi , 150 )
radius = 0.4
a = radius * np.cos( theta )
b = radius * np.sin( theta )
figure, axes = plt.subplots( 1 )
axes.plot( a, b )
axes.set_aspect( 1 )



def drawLine(len, angle, x1, y1):
    # calculate x and y coordinates
    x2 = len * math.cos((angle) * math.pi/180) 
    y2 = len * math.sin((angle) * math.pi/180)

    # plot the hour hand line
    plt.plot([x1,x2], [y1, y2])


# set an hour and minute hand length
hour_len = 0.15
min_len = hour_len*2

drawLine(hour_len, hour_angle, 0, 0)
drawLine(min_len, min_angle, 0, 0)


for i in range(0, 59):
    if(i%5 == 0):
        len = .01
    else:
        len = 0.005
    angle = i * 6
    x1 = 0.001*math.cos(angle * math.pi/180)
    y1 = 0.001*math.sin(angle * math.pi/180)
    drawLine(len, angle, x1, y1)









plt.title("Analog Clock Display")
plt.show()
