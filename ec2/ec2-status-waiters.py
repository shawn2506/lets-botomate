#!/usr/bin/env python

import boto3
from pprint import pprint
session = boto3.session.Session(profile_name="shawn")
ec2_resource = session.resource(service_name="ec2",region_name="us-east-1")
ec2_client = session.client(service_name="ec2", region_name="us-east-1")

#pprint(dir(ec2_resource.instances))

filter_boto = {
    "Name": "tag:Name",
    "Values": ['boto-mate-*']
}

instance_ids = []
for each_instance in ec2_resource.instances.filter(Filters=[filter_boto]):
    instance_ids.append(each_instance.id)

while  True:
    print("This script will perform below actions on the ec2 instance ")
    print("1. Instance-Start")
    print("2. Instance-Stop")
    print("3. Instance-Terminate")
    print("4. Exit-Menu")

    option = input("Enter the action you wish to perform ==>> ")
    if option == 1:
        print("All tagged instances are being started ==> ",instance_ids)
        running_waiter=ec2_client.get_waiter('instance_running')
        ec2_client.start_instances(InstanceIds=instance_ids)
        #ec2_resource.start(InstanceIds=instance_ids)
        running_waiter.wait(InstanceIds=instance_ids)
        break

    elif option == 2:
        print("All tagged instances are being stopped ==> ",instance_ids)
        stopped_waiter=ec2_client.get_waiter('instance_stopped')
        ec2_client.stop_instances(InstanceIds=instance_ids)
        stopped_waiter.wait(InstanceIds=instance_ids)
        break

    elif option == 3:
        print("All tagged instances are being terminated ==> ",instance_ids)
        terminated_waiter=ec2_client.get_waiter('instance_terminated')
        ec2_client.terminate_instances(InstanceIds=instance_ids)
        terminated_waiter.wait(InstanceIds=instance_ids)
        break

    elif option == 4:
        print("Exiting...")
        break
    
    else:
        print "Invalid option enter. Kindly enter options between {1-4}..."
