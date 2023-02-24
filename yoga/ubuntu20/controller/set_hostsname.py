import os
import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.parent.parent)
from utils.file_modify import read_file, rewrite_file
from utils.gen_cfg import gen_cfg_info


def sethostsname():
    content = read_file("/etc/hosts")
    for node_dict in gen_cfg_info().items():
        content += "\n" + node_dict["ip"]
        content += " " + node_dict["name"]
    content += "\n"
    rewrite_file("/etc/hosts", content)
    
if __name__ == "__main__":
    sethostsname()