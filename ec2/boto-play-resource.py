#!/usr/local/env python

# ===============
# COLLECTIONS  ==>> all(), limit(), filter()
# ===============

import boto3
session = boto3.session.Session(profile_name = "user")
ec2_res = session.resource(service_name="ec2", region_name="us-east-1")
#print dir(ec2_res)

#print ec2_res.instances.all()

# will list all the instances
#for each_instance in ec2_res.instances.all():
#    print each_instance

for each_instance in ec2_res.instances.all():
    print(each_instance.hypervisor, each_instance.id, each_instance.state['Name'])
    print each_instance.hypervisor, each_instance.id, each_instance.state['Name']
