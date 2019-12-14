#!/usr/local/env python

import boto3
session = boto3.session.Session(profile_name = "user")
ec2_res = session.resource(service_name="ec2", region_name="us-east-1")

#print dir(ec2_res)
instance_id = raw_input("Enter your instance-id ==> ")
my_instance = ec2_res.Instance(id = instance_id)
print(my_instance.state['Name'])
