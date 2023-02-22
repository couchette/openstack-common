#!/bin/bash
echo "Set networkplan..."

apt -y install chrony
mv /etc/chrony/chrony.conf /etc/chrony/chrony.conf.bak
cat /dev/null >> /etc/chrony/chrony.conf
cat >/etc/chrony/chrony.conf<<END
server controller iburst
END
service chrony restart
chronyc sources

echo "Script run ended"