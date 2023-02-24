import os


def set_final():
    os.system("export OS_USERNAME=admin")
    os.system("export OS_PASSWORD=admin")
    os.system("export OS_PROJECT_NAME=admin")
    os.system("export OS_USER_DOMAIN_NAME=Default")
    os.system("export OS_PROJECT_DOMAIN_NAME=Default")
    os.system("export OS_AUTH_URL=http://controller:5000/v3")
    os.system("export OS_IDENTITY_API_VERSION=3")

    os.system('openstack domain create --description "An Example Domain" example')
    os.system('openstack project create --domain default --description "Service Project" service')
    os.system('openstack project create --domain default --description "Demo Project" myproject')
    os.system("openstack user create --domain default --password-prompt myuser")
    os.system("openstack role create myrole")
    os.system("openstack role add --project myproject --user myuser myrole")
    
if __name__ == "__main__":
    set_final()