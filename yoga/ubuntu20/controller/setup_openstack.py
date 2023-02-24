import os
import sys
from pathlib import Path
sys.path.append(Path(__file__).parent.parent.parent.parent)


def setup_openstack():
    os.system("add-apt-repository cloud-archive:yoga")
    os.system("apt -y install nova-compute")
    os.system("apt -y install python3-openstackclient<<EOF\n\nEOF")