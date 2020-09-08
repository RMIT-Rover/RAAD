import ikpy
import numpy as np
from ikpy.link import OriginLink, URDFLink
from ikpy.chain import Chain


left_arm_chain = Chain(name='left_arm', links=[
    OriginLink(),
     URDFLink(
      name="base",
      translation_vector=[0, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
    URDFLink(
      name="base_joint",
      translation_vector=[0, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
     URDFLink(
      name="joint1",
      translation_vector=[0, 0, 0.5],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
     URDFLink(
      name="joint2",
      translation_vector=[0.4, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="pitch",
      translation_vector=[0, 0, -0.15],
      orientation=[1, 0, 0],
      rotation=[0, 1, 0],
    ),
    URDFLink(
      name="yaw",
      translation_vector=[0, 0, 0],
      orientation=[0, 0, 1],
      rotation=[0,0,1]
    ),
     URDFLink(
      name="roll",
      translation_vector=[0.1, 0, 0],
      orientation=[1, 0, 0],
      rotation=[1,0,0]
    ),
  
  
])


"""
target_position = [ 0.1, -0.2, 0.1]

print("The angles of each joints are : ", left_arm_chain.inverse_kinematics(target_position))


import matplotlib.pyplot as plt
fig, ax = plot_utils.init_3d_figure()
left_arm_chain.plot(left_arm_chain.inverse_kinematics(target_position), ax, target=target_position)


plt.show()
"""

from ikpy.utils import plot
from mpl_toolkits.mplot3d import Axes3D

fig, ax = plot.init_3d_figure()
left_arm_chain.plot([0] * (len(left_arm_chain)),ax)

target_position = [0.6,0,0]
target_orientation = np.eye(3)
#orientation_mode = "X"
#ik = left_arm_chain.inverse_kinematics(target_position)

ik = left_arm_chain.inverse_kinematics(
target_position,
target_orientation = target_orientation,
orientation_mode="all")
print("The angles of each joints are : ", left_arm_chain.inverse_kinematics(target_position))
ax.legend()
left_arm_chain.plot(ik,ax,target_position,True)



