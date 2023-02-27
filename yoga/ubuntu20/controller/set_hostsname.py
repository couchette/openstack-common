import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.file_modify import read_file, rewrite_file
from utils.gen_cfg import gen_cfg_info


def sethostsname():
    content = read_file("/etc/hosts")
    cfg_info = gen_cfg_info()
    for key in cfg_info.keys():
        content += "\n" + cfg_info[key]["ip1"]
        content += " " + cfg_info[key]["name"]
    content += "\n"
    rewrite_file("/etc/hosts", content)
    
if __name__ == "__main__":
    sethostsname()