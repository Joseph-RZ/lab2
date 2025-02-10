from launch import LaunchDescription
from launch_ros.actions import Node


def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab2',
            executable='numeric_talker',  # Runs the numeric talker
            name='my_numeric_talker'
            
        ),
        Node(
            package='lab2',
            executable='numeric_listener',  # Runs the numeric listener
            name='my_numeric_listener'
        ),
    ])
