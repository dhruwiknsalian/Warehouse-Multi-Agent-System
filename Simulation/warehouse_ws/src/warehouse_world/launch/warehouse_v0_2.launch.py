import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess

def generate_launch_description():
    pkg_share = get_package_share_directory('warehouse_world')
    world_path = os.path.join(pkg_share, 'worlds', 'warehouse_v0_2.world')

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', '-v', '4', world_path],
            output='screen'
        )
    ])