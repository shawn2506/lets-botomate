#!/usr/bin/env python

import boto3

# creating a session for aws_profile
session = boto3.session.Session(profile_name="shawn")

# creating resource & client for ec2
ec2_res = session.resource(service_name= "ec2", region_name = "us-east-1")
ec2_cli = session.client(service_name= "ec2", region_name = "us-east-1")

# creating resource & client for s3
s3_res = session.resource(service_name = "s3", region_name = "us-east-1")
s3_cli = session.resource(service_name = "s3", region_name = "us-east-1")
