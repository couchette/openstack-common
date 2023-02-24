import os
import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.parent.parent)
from utils.gen_cfg import gen_cfg_info
from utils.file_modify import read_file, rewrite_file


def setup_etcd():
    controller_cfg_info = gen_cfg_info()["controller_info"]
    os.system("apt -y install etcd")
    content = read_file("/etc/default/etcd")
    content += '''

    ETCD_NAME="{}"
    ETCD_DATA_DIR="/var/lib/etcd"
    ETCD_INITIAL_CLUSTER_STATE="new"
    ETCD_INITIAL_CLUSTER_TOKEN="etcd-cluster-01"
    ETCD_INITIAL_CLUSTER="controller=http://{}:2380"
    ETCD_INITIAL_ADVERTISE_PEER_URLS="http://{}:2380"
    ETCD_ADVERTISE_CLIENT_URLS="http://{}:2379"
    ETCD_LISTEN_PEER_URLS="http://0.0.0.0:2380"
    ETCD_LISTEN_CLIENT_URLS="http://{}:2379"
    '''.format(
        controller_cfg_info["name"],
        controller_cfg_info["ip1"],
        controller_cfg_info["ip1"],
        controller_cfg_info["ip1"],
        controller_cfg_info["ip1"]
    )
    rewrite_file("/etc/default/etcd", content)
    os.system("systemctl restart etcd")
    os.system("systemctl enable etcd")