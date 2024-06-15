import time
import numpy as np
import matplotlib.pyplot as plt
import math

# get the local time, store hour and minute
t = time.localtime()
hour = t.tm_hour%12
minute = t.tm_min

# calculate angle of both hour hand and minute hand
hour_angle = ((hour * 30) + (minute * 0.5)) % 360
min_angle = minute * 6
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

# set an hour hand length
hour_len = 0.15

# calculate x and y coordinates 
hour_x = hour_len * math.cos((hour_angle%90) * math.pi/180) 
hour_x = hour_x * -1 if (hour_angle/90) > 1 else hour_x
hour_y = hour_len * math.sin((hour_angle%90) * math.pi/180)
hour_y = hour_y * -1 if (hour_angle/90) == 1 or (hour_angle/90) == 2 else hour_y

print(hour_x)
print(hour_y)

# plot the hour hand line
plt.plot([0,hour_x], [0, hour_y])

min_len = hour_len*2

min_x = min_len * math.cos((min_angle%90) * math.pi/180) 
min_x = min_x * -1 if (minute%15) > 1 else min_x
min_y = min_len * math.sin((min_angle%90) * math.pi/180)
min_y = min_y * -1 if (minute%15) == 1 or (minute%15) == 2 else min_y

# plot the minute hand line
plt.plot([0,min_x], [0, min_y])



plt.title("Analog Clock Display")
plt.show()
