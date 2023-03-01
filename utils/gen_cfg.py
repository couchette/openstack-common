

def gen_cfg_info():
    info = {}
    password_info = {}
    
    controller_info = {}
    controller_info["name"] = "controller"
    controller_info["network1"] = "10.0.0.0"
    controller_info["ip1"] = "10.0.0.10"
    controller_info["gateway1"] = "10.0.0.1"
    controller_info["network2"] = "10.0.0.0"
    controller_info["ip2"] = "203.0.113.10"
    controller_info["gateway2"] = "203.0.113.1"
    controller_info["mysql_password"] = "1234"
    controller_info["rabbitmq_user"] = "openstack"
    controller_info["rabbitmq_password"] = "1234"
    # computer_info = {}
    
    info["controller_info"] = controller_info
    # info["computer_info"] = computer_info
    
    return info

