import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.gen_cfg import gen_cfg_info
from utils.file_modify import rewrite_file


def setup_mysql():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    os.system("apt -y install mariadb-server python3-pymysql")
    content = '''
    [mysqld]
    bind-address = {}
    default-storage-engine = innodb
    innodb_file_per_table = on
    max_connections = 4096
    collation-server = utf8_general_ci
    character-set-server = utf8
    '''.format(
        controller_cfg_info["ip1"]
    )
    rewrite_file("/etc/mysql/mariadb.conf.d/99-openstack.cnf", content)
    os.system("service mysql restart")
    
    mysql_password = controller_cfg_info["mysql_password"]
    cmd_ = "\nY\n{}\n{}\nY\nY\nY\nY\n".format(mysql_password, mysql_password)
    os.system("mysql_secure_installation << EOF\n" + cmd_+ "\nEOF")
    
    
if __name__ == "__main__":
    setup_mysql()