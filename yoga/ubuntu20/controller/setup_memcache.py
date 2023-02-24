import os
import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.parent.parent)
from utils.gen_cfg import gen_cfg_info
from utils.file_modify import replace


def setup_memcache():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    os.system("apt -y install memcached python3-memcache")
    replace("/etc/memcached.conf", "-l 127.0.0.1", "-l {}".format(controller_cfg_info["ip1"]))
    os.system("service memcached restart")