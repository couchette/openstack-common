from data_struction import Password


def gen_cfg_info():
    ADMIN_PASS = Password(name="ADMIN_PASS", info ="", intro="Password of user admin")
    CINDER_DBPASS = Password(name="CINDER_DBPASS", info="", intro="Database password for the Block Storage service")
    CINDER_PASS = Password(name="CINDER_PASS", info="", intro="Password of Block Storage service user cinder")
    DASH_DBPASS = Password(name="DASH_DBPASS", info="", intro="Database password for the Dashboard")
    DEMO_PASS = Password(name="DEMO_PASS", info="", intro="Password of user demo")
    GLANCE_DBPASS = Password(name="GLANCE_DBPASS", info="", intro="Database password for Image service")
    GLANCE_PASS = Password(name="GLANCE_PASS", info="", intro="Password of Image service user glance")
    KEYSTONE_DBPASS = Password(name="KEYSTONE_DBPASS", info="", intro="Database password of Identity service")
    METADATA_SECRET = Password(name="METADATA_SECRET", info="", intro="Secret for the metadata proxy")
    NEUTRON_DBPASS = Password(name="NEUTRON_DBPASS", info="", intro="Database password for the Networking service")
    NEUTRON_PASS = Password(name="NEUTRON_PASS", info="", intro="Password of Networking service user neutron")
    NOVA_DBPASS = Password(name="NOVA_DBPASS", info="", intro="Database password for Compute service")
    NOVA_PASS = Password(name="NOVA_PASS", info="", intro="Password of Compute service user nova")
    PLACEMENT_PASS = Password(name="PLACEMENT_PASS", info="", intro="Password of the Placement service user placement")
    RABBIT_PASS = Password(name="RABBIT_PASS", info="", intro="Password of RabbitMQ user openstack")
    info = {}
    
    controller_info = {}
    controller_info["name"] = "controller"
    controller_info["network1"] = "10.0.0.0"
    controller_info["ip1"] = "10.0.0.10"
    controller_info["gateway1"] = "10.0.0.2"
    controller_info["network2"] = "10.0.0.0"
    controller_info["ip2"] = "203.0.113.10"
    controller_info["gateway2"] = "203.0.113.2"
    controller_info["mysql_password"] = "1234"
    controller_info["rabbitmq_user"] = "openstack"
    controller_info["rabbitmq_password"] = "1234"
    # computer_info = {}
    
    info["controller_info"] = controller_info
    # info["computer_info"] = computer_info
    
    return info

