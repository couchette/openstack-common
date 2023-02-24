import os
import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.parent.parent)
from utils.file_modify import read_file, rewrite_file
from utils.gen_cfg import gen_cfg_info


def set_apache():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    content = read_file("/etc/apache2/apache2.conf")
    content += "\nServerName "+ controller_cfg_info["name"]
    rewrite_file("/etc/apache2/apache2.conf", content)
    os.system("service apache2 restart")
    
if __name__ == "__main__":
    set_apache()