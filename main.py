import os
import sys
import logging

FORMAT = '%(asctime)s %(clientip)-15s %(user)-8s %(message)s'
logging.basicConfig(format=FORMAT)
logger = logging.getLogger('tcpserver')


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
            os.system("apt-get install python3-pip")
            running_inquiries()
            os.system("python3 -m pip install " + pkg_path + " -i https://pypi.mirrors.ustc.edu.cn/simple/")
            logger.info("install {}".format(pkg_path))

def running_inquiries():
    content = input("continue?(Y/n)")
    if content == 'Y':
        pass
    else:
        exit()
            
def run_script(openstack_version:str, sys="ubuntu20", node="controller"):
    workdir = os.getcwd()
    scriptsdir = workdir + "/" + openstack_version + "/" + sys + "/" + node + "/"
    
    # sudo
    os.system("python3 " + scriptsdir + "set_hostsname.py")
    running_inquiries()
    logger.info("set_hostsname")
    os.system("python3 " + scriptsdir + "set_netplan.py")
    running_inquiries()
    logger.info("set_netplan")
    os.system("python3 " + scriptsdir + "set_npt.py")
    running_inquiries()
    logger.info("set_npt")
    os.system("python3 " + scriptsdir + "setup_openstack.py")
    running_inquiries()
    logger.info("setup_openstack")
    os.system("python3 " + scriptsdir + "setup_mysql.py")
    running_inquiries()
    logger.info("setup_mysql")
    os.system("python3 " + scriptsdir + "setup_rabbitmq.py")
    running_inquiries()
    logger.info("setup_rabbitmq")
    os.system("python3 " + scriptsdir + "setup_memcache.py")
    running_inquiries()
    logger.info("setup_memcache")
    os.system("python3 " + scriptsdir + "setup_etcd.py")
    running_inquiries()
    logger.info("setup_etcd")
    os.system("python3 " + scriptsdir + "setup_keystone.py")
    running_inquiries()
    logger.info("setup_keystone")
    os.system("python3 " + scriptsdir + "set_keystone.py")
    running_inquiries()
    logger.info("set_keystone")
    os.system("python3 " + scriptsdir + "set_apache.py")
    running_inquiries()
    logger.info("set_apache")
    os.system("python3 " + scriptsdir + "final_set.py")
    running_inquiries()
    logger.info("final_set")
    
    pass
    
def main_func():
    init_check()
    running_inquiries()
    install_dev()
    running_inquiries()
    run_script("yoga")
    
if __name__ == "__main__":
    
    main_func()
    


    