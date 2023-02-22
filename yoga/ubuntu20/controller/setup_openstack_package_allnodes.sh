#!/bin/bash
echo "Setup openstack_package..."

add-apt-repository cloud-archive:yoga
apt -y install nova-compute
apt -y install python3-openstackclient

echo "Script run ended"