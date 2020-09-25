import math
from mpl_toolkits import mplot3d
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider, Button
import numpy as np

# Define the lengths of all the links
a1 = 0                         # Height of the base
a2 = 530                       # Length of link1
a3 = 510
a4 = 100
a5 = 100
a6 = 217

# Base point of the link
x0 = 0
y0 = 0
z0 = 0

# Calculation is done by splitting the arm into 2 parts'
# End effector positions in 3D space and the two links

x_end = 600
y_end = 100
z_end = 0

# Calculating the points for the graph
y5 = y_end
x5 = x_end
z5 = z_end
y4 = y5
x4 = x5-a6
z4 = z5
x3 = x4
y3 = y5
z3 = z4 + a5
x2 = x3
y2 = y3 + a4
z2 = z3


# Case1: When y is +ve
if (y2 >= 0):
    theta1 = math.atan2(y2, x2)                                 # Rotation angle of the base
    r1 = math.hypot(x2, y2)
    r2 = z2 - a1
    alpha2 = math.atan2(r2, r1)
    r3 = math.hypot(r1, r2)
    alpha1 = math.acos(((a3*a3)-(a2*a2)-(r3*r3))/(-2*a2*r3))
    theta2 = alpha2-alpha1
    theta2_eff = theta2 + 2*alpha1                              # Angle of Link1 w.r.t. base
    alpha3 = math.acos(((r3*r3)-(a2*a2)-(a3*a3))/(-2*a2*a3))
    theta3 = math.pi-alpha3                                     # Angle of Link2 w.r.t. base
    alpha4 = -theta3+theta2+(2*alpha1)
    theta4 = math.pi/2 + theta3
    theta5 = math.pi/2 + theta1

    angles = np.rad2deg([theta1, theta2_eff, theta3, theta4, theta5])

else:
    y2 = abs(y2)
    theta1 = math.atan2(y2, x2)  # Rotation angle of the base
    r1 = math.hypot(x2, y2)
    r2 = z2 - a1
    alpha2 = math.atan2(r2, r1)
    r3 = math.hypot(r1, r2)
    alpha1 = math.acos(((a3 * a3) - (a2 * a2) - (r3 * r3)) / (-2 * a2 * r3))
    theta2 = alpha2 - alpha1
    theta2_eff = theta2 + 2 * alpha1  # Angle of Link1 w.r.t. base
    alpha3 = math.acos(((r3 * r3) - (a2 * a2) - (a3 * a3)) / (-2 * a2 * a3))
    theta3 = math.pi - alpha3  # Angle of Link2 w.r.t. base
    alpha4 = -theta3 + theta2 + (2 * alpha1)
    theta4 = math.pi / 2 + theta3
    theta5 = math.pi / 2 + theta1
    theta1 = theta1 * (-1)
    y2 = y2*(-1)

    angles = np.rad2deg([theta1, theta2_eff, theta3, theta4, theta5])


# To plot the graphs
a2_t = a2*math.cos(theta1)
r1_t = r1*math.cos(theta1)
p_x1 = a2_t*(math.cos(theta2+alpha1+alpha1))
p_y1 = p_x1*(math.sin(theta1))
p_z1 = abs(a2*(math.sin(theta2+alpha1+alpha1)))
p_x2 = x2
p_y2 = y2
p_z2 = abs(z2)

print(theta1, theta2, theta3, theta4, theta5, alpha1, alpha2)
print(angles)

fig = plt.figure()
ax = plt.axes(projection='3d')

forward = [x0, p_x1, p_x2, x3, x4, x5]
side = [y0, p_y1, p_y2, y3, y4, y5]
upward = [z0, p_z1, p_z2, z3, z4, z5]

ax.plot(forward, side, upward, color='r', marker='o')
ax.set_xlim3d(-50, 1150)
ax.set_ylim3d(-500, 500)
ax.set_zlim3d(-500, 500)
axSlider = plt.axes([0.1, 0.1, 0.2, 0.05])

plt.show()


