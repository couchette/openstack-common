#!/bin/bash
echo "Set networkplan..."

cat /dev/null >> /etc/netplan/01-network-manager-all.yaml
cat >/etc/netplan/01-network-manager-all.yaml<<END
network:
  version: 2
  renderer: NetworkManager
  ethernets:
    ens33:   #配置的网卡名称，自己根据情况修改
      dhcp4: no    #dhcp4关闭
      dhcp6: no    #dhcp6关闭
      addresses: [10.0.0.31/24]   #设置本机IP及掩码
      gateway4: 10.0.0.2   #设置网关
      nameservers:
          addresses: [10.0.0.2] 
    ens34:   #配置的网卡名称，自己根据情况修改
      dhcp4: no    #dhcp4关闭
      dhcp6: no    #dhcp6关闭
      addresses: [203.0.113.31/24]   #设置本机IP及掩码
      gateway4: 203.0.113.2   #设置网关
      nameservers:
          addresses: [203.0.113.2] 
END
netplan apply

echo "Script run ended"