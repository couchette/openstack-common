#!/bin/bash
echo "Set hostsname..."

cat /dev/null >> /etc/hosts
cat >/etc/hosts<<END
127.0.0.1	localhost

# controller
10.0.0.11 controller
# compute1
10.0.0.31 compute1
# block1
10.0.0.41 block1
# object1
10.0.0.51 object1
# object2
10.0.0.52 object2

# The following lines are desirable for IPv6 capable hosts
::1     ip6-localhost ip6-loopback
fe00::0 ip6-localnet
ff00::0 ip6-mcastprefix
ff02::1 ip6-allnodes
ff02::2 ip6-allrouters
END

echo "Script run ended"