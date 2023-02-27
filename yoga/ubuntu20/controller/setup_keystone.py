#!/bin/bash
import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.gen_cfg import gen_cfg_info


def setup_keystone():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    cmd_ = '''
    mysql -u root -p{} <<EOF
    GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'localhost' IDENTIFIED BY 'keystone';
    GRANT ALL PRIVILEGES ON keystone.* TO 'keystone'@'%' IDENTIFIED BY 'keystone';
    EOF
    '''.format(
        controller_cfg_info["mysql_password"]
    )
    os.system(cmd_)
    os.system("apt -y install keystone")


if __name__ == "__main__":
    setup_keystone()