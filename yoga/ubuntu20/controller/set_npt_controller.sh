#!/bin/bash
echo "Set networkplan..."

apt -y install chrony
mv /etc/chrony/chrony.conf /etc/chrony/chrony.conf.bak
cat /dev/null >> /etc/chrony/chrony.conf
cat >/etc/chrony/chrony.conf<<END
server ntp.aliyun.com iburst
allow 10.0.0.0/24
END
service chrony restart
chronyc sources

echo "Script run ended"