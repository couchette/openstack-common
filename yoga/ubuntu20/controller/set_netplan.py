import os
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).parent.parent.parent.parent))
from utils.gen_cfg import gen_cfg_info
from utils.file_modify import rewrite_file

def set_netplan():
  controller_cfg_info = gen_cfg_info()["controller_info"]
  content = '''
  network:
    version: 2
    renderer: NetworkManager
    ethernets:
      ens33:   #配置的网卡名称，自己根据情况修改
        dhcp4: no    #dhcp4关闭
        dhcp6: no    #dhcp6关闭
        addresses: [{}/24]   #设置本机IP及掩码
        gateway4: {}   #设置网关
        nameservers:
            addresses: {} 
      ens34:   #配置的网卡名称，自己根据情况修改
        dhcp4: no    #dhcp4关闭
        dhcp6: no    #dhcp6关闭
        addresses: [{}/24]   #设置本机IP及掩码
        gateway4: {}   #设置网关
        nameservers:
            addresses: [{}] 
  '''.format(controller_cfg_info["ip1"],
            controller_cfg_info["gateway1"],
            controller_cfg_info["gateway1"],
            controller_cfg_info["ip2"],
            controller_cfg_info["gateway2"],
            controller_cfg_info["gateway2"],)
  rewrite_file("/etc/hosts", content)
  os.system("netplan apply")
  

if __name__ == "__main__":
    set_netplan()