#!/usr/bin/env python

import boto3
session = boto3.session.Session(profile_name='shawn')
ec2_res = session.resource(service_name="ec2", region_name="us-east-1")

# filter-variables

tags = {"Name": "tag:Name", "Values": ["boto-mate-1","boto-mate-2"]}
for each_instance in ec2_res.instances.filter(Filters=[tags], DryRun=True):
    print(each_instance.state['Name'], each_instance.id)


