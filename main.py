import os
import sys


def init_check():
    print(sys.version) 
    if sys.version_info.major < 3 and sys.version_info.minor < 7:
        print("Error: please make sure your python version >= 3.7")
        exit()

def install_dev():
    workdir = os.getcwd()
    pkgsdir = workdir + "/python/pkg/"
    pkgs_names = os.listdir(pkgsdir)
    for pkg_name in pkgs_names:
        pkg_path = pkgsdir + pkg_name
        if os.path.isfile(pkg_path):
            os.system("pip install " + pkg_path)
    
def main_func():
    init_check()
    install_dev()
    
if __name__ == "__main__":
    
    main_func()


    