#!/bin/bash
echo "Setup keystone..."

./setup_keystone_.sh < setup_keystone.data
apt -y install keystone

echo "Script run ended"