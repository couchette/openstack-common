import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.gen_cfg import gen_cfg_info
from utils.file_modify import rewrite_file


def set_npt():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    os.system("apt -y install chrony")
    os.system("mv /etc/chrony/chrony.conf /etc/chrony/chrony.conf.bak")
    content = '''
    server ntp.aliyun.com iburst
    allow {}/24
    '''.format(
        controller_cfg_info["network1"]
    )
    rewrite_file("/etc/chrony/chrony.conf", content)
    os.system("service chrony restart")
    os.system("chronyc sources")


if __name__ == "__main__":
    set_npt()