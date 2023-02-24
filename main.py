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
            
def run_script(openstack_version:str, sys="ubuntu20"):
    workdir = os.getcwd()
    scriptsdir = workdir + "/" + openstack_version + "/" + sys + "/"
    
    # set_hostsname
    # sudo
    os.system("python3 " + scriptsdir + "set_hostsname.py")
    os.system("python3 " + scriptsdir + "set_netplan.py")
    os.system("python3 " + scriptsdir + "set_npt.py")
    os.system("python3 " + scriptsdir + "setup_openstack.py")
    os.system("python3 " + scriptsdir + "setup_mysql.py")
    os.system("python3 " + scriptsdir + "set_rabbitmq.py")
    os.system("python3 " + scriptsdir + "setup_memcache.py")
    os.system("python3 " + scriptsdir + "setup_etcd.py")
    os.system("python3 " + scriptsdir + "setup_keystone.py")
    os.system("python3 " + scriptsdir + "set_keystone.py")
    os.system("python3 " + scriptsdir + "set_apache.py")
    os.system("python3 " + scriptsdir + "final_set.py")
    
    pass
    
def main_func():
    init_check()
    install_dev()
    
if __name__ == "__main__":
    
    main_func()
    


    