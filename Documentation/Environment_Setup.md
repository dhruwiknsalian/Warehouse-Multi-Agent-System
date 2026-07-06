# Environment Setup

Verified on: (add today's date)

## OS
Ubuntu 22.04.5 LTS (Jammy)

## ROS 2
Distro: Humble
Shell: zsh — sourced via `/opt/ros/humble/setup.zsh` (not setup.bash, which breaks under zsh)
Added to ~/.zshrc: `source /opt/ros/humble/setup.zsh`

## Simulation
Gazebo Sim (Harmonic) 8.13.0
Bridge: ros-humble-ros-gz, ros-humble-ros-gz-sim, ros-humble-ros-gz-bridge
Note: classic `ros-humble-gazebo-ros-pkgs` conflicts with Harmonic — do not install it.

## Navigation
ros-humble-navigation2
ros-humble-nav2-bringup

## Supporting packages
ros-humble-xacro
ros-humble-robot-state-publisher
ros-humble-teleop-twist-keyboard

## Tools
Git 2.54.0
VS Code 1.124.0
colcon (/usr/bin/colcon)

## Why Gazebo Harmonic over classic Gazebo
Classic Gazebo (11.x) is end-of-life; Harmonic (gz sim) is the actively maintained simulator going forward and is the one paired with ROS 2 Humble via ros_gz, not gazebo_ros_pkgs.
