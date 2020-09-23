import numpy as np
from ikpy.link import OriginLink, URDFLink
from ikpy.chain import Chain
from ikpy.utils import plot


left_arm_chain = Chain(name='left_arm', links=[
    OriginLink(),
     URDFLink(
      name="base_rotation",
      translation_vector=[0, 0, 0.1],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
    URDFLink(
      name="linear1_joint",
      translation_vector=[0.001, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
     URDFLink(
      name="linear2_joint",
      translation_vector=[0, 0, 0.5],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
     URDFLink(
      name="pitch",
      translation_vector=[0.4, 0, 0],
      orientation=[0, 0, 0],
      rotation=[0, 1, 0],
    ),
      URDFLink(
      name="offset",
      translation_vector=[0, -0.05, 0],
      orientation=[0, 0, 0],
      rotation=[0, 0, 0],
    ),
    URDFLink(
      name="yaw",
      translation_vector=[0, 0, -0.05],
      orientation=[0, 0, 0],
      rotation=[0, 0, 1],
    ),
     URDFLink(
      name="roll",
      translation_vector=[0.05, 0, 0],
      orientation=[1, 0, 0],
      rotation=[1,0,0]
    ),
  
])

fig, ax = plot.init_3d_figure()
left_arm_chain.plot([0] * (len(left_arm_chain)),ax)

target_position = [0.5, -0.2, 0.3]
target_orientation = np.eye(3)
#orientation_mode = "X"
ik = left_arm_chain.inverse_kinematics(target_position)

ik = left_arm_chain.inverse_kinematics(
target_position,
target_orientation = target_orientation,
orientation_mode="all",
initial_position=ik)

print("The angles of each joints are : ", left_arm_chain.inverse_kinematics(target_position))
ax.legend()
left_arm_chain.plot(ik,ax,target_position,True)



