#!/usr/bin/env python
import pprint
import boto3
session = boto3.session.Session(profile_name="shawn")
ec2_client = session.client(service_name = "ec2", region_name = "us-east-1")

#pprint.pprfor each_instance inc2_client.describe_instances()['Reservations'])
for each_info in ec2_client.describe_instances()['Reservations']:
    for each_instance in each_info['Instances']:
        print each_instance['InstanceId'], each_instance['InstanceType']
