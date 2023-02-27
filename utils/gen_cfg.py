

def gen_cfg_info():
    info = {}
    controller_info = {}
    controller_info["name"] = "controller"
    controller_info["network1"] = "192.168.100.0"
    controller_info["ip1"] = "192.168.100.10"
    controller_info["gateway1"] = "192.168.100.1"
    controller_info["network2"] = "192.168.100.0"
    controller_info["ip2"] = "192.168.200.10"
    controller_info["gateway2"] = "192.168.200.1"
    controller_info["mysql_password"] = "1234"
    controller_info["rabbitmq_user"] = "openstack"
    controller_info["rabbitmq_password"] = "1234"
    # computer_info = {}
    
    info["controller_info"] = controller_info
    # info["computer_info"] = computer_info
    
    return info

