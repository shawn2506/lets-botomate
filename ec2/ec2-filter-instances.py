#!/usr/bin/env boto3

import boto3
session = boto3.session.Session(profile_name="user")
ec2_res = session.resource(service_name="ec2", region_name="us-east-1")

#print(dir(ec2_res))

'''
started = {
    "Name": "instance-state-name",
    "Values": [
        "stopped","running"
        ]
}

zone = {
    "Name": "availability-zone",
    "Values": [
        "us-east-1d"
    ]
}

ins_type = {
    "Name": "instance-type",
    "Values": [
        "t2.micro"
    ]
}

for each_instance in ec2_res.instances.filter(Filters=[started,zone,ins_type]):
    print(each_instance.state['Name'], each_instance.id)
'''


tags = {
    "Name": 'tag:Name',
    "Values": ['boto-mate-1','boto-mate-2'

    ]
}
for each_instance in ec2_res.instances.filter(Filters=[tags]):
    print(each_instance.state['Name'], each_instance.id)
