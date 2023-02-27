import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.file_modify import replace

def set_keystone():
    replace(r"/etc/keystone/keystone.conf", 
        "connection = sqlite:////var/lib/keystone/keystone.db",
        "connection = mysql+pymysql://keystone:keystone@controller/keystone")
    replace(r"/etc/keystone/keystone.conf", 
        "# IDs. (string value)\n#provider = fernet",
        "# IDs. (string value)\nprovider = fernet")
        
    os.system('su -s /bin/sh -c "keystone-manage db_sync" keystone')
    os.system("keystone-manage fernet_setup --keystone-user keystone --keystone-group keystone")
    os.system("keystone-manage credential_setup --keystone-user keystone --keystone-group keystone")
        
    os.system("keystone-manage bootstrap --bootstrap-password admin  \
        --bootstrap-admin-url http://controller:5000/v3/ \
        --bootstrap-internal-url http://controller:5000/v3/ \
        --bootstrap-public-url http://controller:5000/v3/ \
        --bootstrap-region-id RegionOne")
    
if __name__ == "__main__":
    set_keystone()