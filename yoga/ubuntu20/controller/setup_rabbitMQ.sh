#!/bin/bash
echo "Setup rabbitMQ..."

apt -y install rabbitmq-server
rabbitmqctl add_user openstack 123456
rabbitmqctl set_permissions openstack ".*" ".*" ".*"

echo "Script run ended"