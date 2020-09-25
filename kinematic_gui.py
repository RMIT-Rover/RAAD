from geometric_ik import ik_angles
# import msvcrt
import keyboard
import time


frequency = 0.5               # Time to wait before reading another keyboard input

# Size of end effector steps
step_x_value = 30
step_y_value = 5
step_z_value = 5

# Define initial start position after homing
x_start = 500
y_start = 0
z_start = 0

end_position = ik_angles(x_start, y_start, z_start)                  # Initiate start position

x_eff = x_start
y_eff = y_start
z_eff = z_start

while True:
    # Keyboard character retrieval method is called and saved
    # into variable
    # char = msvcrt.getch()

    # The arm will extend when the "w" key is pressed
    if keyboard.is_pressed("w"):
        x_eff = x_eff + step_x_value
        end_position = ik_angles(x_eff, y_eff, z_eff)
        time.sleep(frequency)

    # The arm will retract when the "s" key is pressed
    if keyboard.is_pressed("s"):
        x_eff = x_eff - step_x_value
        end_position = ik_angles(x_eff, y_eff, z_eff)
        time.sleep(frequency)

    # The "d" key will move the arm left
    if keyboard.is_pressed("a"):
        y_eff = y_eff + step_y_value
        end_position = ik_angles(x_eff, y_eff, z_eff)
        time.sleep(frequency)

    # The "d" key will move the arm right
    if keyboard.is_pressed("d"):
        y_eff = y_eff - step_y_value
        end_position = ik_angles(x_eff, y_eff, z_eff)
        time.sleep(frequency)

    # The "q" key will move the arm up
    if keyboard.is_pressed("q"):
        z_eff = z_eff - step_z_value
        end_position = ik_angles(x_eff, y_eff, z_eff)
        time.sleep(frequency)

    # The "e" key will move the arm down
    if keyboard.is_pressed("e"):
        z_eff = z_eff - step_z_value
        end_position = ik_angles(x_eff, y_eff, z_eff)
        time.sleep(frequency)

    # The "x" key will break the loop and exit the program
    if keyboard.is_pressed("x"):
        print("Program Ended")
        break




