#!/usr/bin/env python

import boto3
session    = boto3.session.Session(profile_name="shawn")
ec2_client = session.client(service_name="ec2", region_name="us-east-1")
all_regions = []
for each_region in (ec2_client.describe_regions().get('Regions')):
    all_regions.append(each_region['RegionName'])
print "All regions that support ec2 service are ==>> \n", all_regions