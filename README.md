# wanderbot
Programming Robots in ROS - wanderbot package

# Resources
* [Programming Robots with ROS](http://marte.aslab.upm.es/redmine/files/dmsf/p_drone-testbed/170324115730_268_Quigley_-_Programming_Robots_with_ROS.pdf)

# Setup
Install turtlebot simulation stack
```
sudo apt install ros-kinetic-turtlebot-gazebo 
```
# Run
Start the simulator
```
roslaunch turtlebot_gazebo turtlebot_world.launch
```
Control node
```
./src/red_light_green_light.py cmd_vel:=cmd_vel_mux/input/teleop
```
Range ahead node
```
./src/range_ahead.py
```
Wander node
```
./src/wander.py cmd_vel:=cmd_vel_mux/input/teleop
```
