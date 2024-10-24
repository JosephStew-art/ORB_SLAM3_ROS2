from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import ExecuteProcess
import os

def generate_launch_description():
    # Define the correct paths
    vocab_path = '/home/joseph/Desktop/SLAM/colcon_ws/src/orbslam3_ros2/vocabulary/ORBvoc.txt'
    config_path = '/home/joseph/Desktop/SLAM/colcon_ws/src/orbslam3_ros2/config/monocular/brio.yaml'

    return LaunchDescription([
        # Python robot control node
        Node(
            package='orbslam3',
            executable='robot_remote_control.py',
            name='robot_remote_control',
            output='screen'
        ),

        # ORBSLAM3 C++ node
        ExecuteProcess(
            cmd=['ros2', 'run', 'orbslam3', 'mono', vocab_path, config_path],
            output='screen'
        )
    ])