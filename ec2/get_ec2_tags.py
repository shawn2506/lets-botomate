#!/usr/local/env python

import boto3
session = boto3.session.Session(profile_name="shawn")
ec2_res = session.resource(service_name="ec2",region_name="us-east-1")
instance_id = raw_input("Enter the instance_id ==> ")
my_instance = ec2_res.Instance(id = instance_id)
#print dir(my_instance)

print(my_instance.tags)
