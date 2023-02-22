#!/bin/bash
echo "Setup mysql..."

apt -y install mariadb-server python3-pymysql
touch /etc/mysql/mariadb.conf.d/99-openstack.cnf
cat /dev/null >> /etc/mysql/mariadb.conf.d/99-openstack.cnf
cat >/etc/mysql/mariadb.conf.d/99-openstack.cnf<<END
[mysqld]
bind-address = 10.0.0.11
default-storage-engine = innodb
innodb_file_per_table = on
max_connections = 4096
collation-server = utf8_general_ci
character-set-server = utf8
END
service mysql restart

echo "Script run ended"