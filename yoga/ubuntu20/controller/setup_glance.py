import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.file_modify import read_file, rewrite_file
from utils.gen_cfg import gen_cfg_info


def setup_glance():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    os.system("apt install glance")
    # TODO:
    
    
if __name__ == "__main__":
    setup_glance()