import os
from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch.actions import ExecuteProcess, SetEnvironmentVariable
from launch.substitutions import EnvironmentVariable

def generate_launch_description():
    pkg_share = get_package_share_directory('warehouse_world')
    world_path = os.path.join(pkg_share, 'worlds', 'warehouse_v0_2.world')
    models_path = os.path.join(pkg_share, 'models')

    return LaunchDescription([
        SetEnvironmentVariable(
            name='GZ_SIM_RESOURCE_PATH',
            value=models_path
        ),
        ExecuteProcess(
            cmd=['gz', 'sim', '-r', world_path],
            output='screen'
        )
    ])