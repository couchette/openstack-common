import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.gen_cfg import gen_cfg_info


def setup_rabbitmq():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    os.system("apt -y install rabbitmq-server")
    os.system("rabbitmqctl add_user {} {}".format(controller_cfg_info["rabbitmq_user"], controller_cfg_info["rabbitmq_password"]))
    os.system('rabbitmqctl set_permissions openstack ".*" ".*" ".*"')
    
    
if __name__ == "__main__":
    setup_rabbitmq()