#!/usr/bin/env python

import boto3

session = boto3.session.Session(profile_name = "shawn-personal")
ec2_res = session.resource(service_name = "ec2", region_name = "us-east-1")
#my_instance = ec2_res.Instance(id = "***")

# to check all vailable operations
#print dir(my_instance)

while  True:
    instance_id = raw_input("Enter your instance id ==>> ")
    my_instance = ec2_res.Instance(id = instance_id)
    print("This script will perform below actions on the ec2 instance ")
    print("1. Instance-Start")
    print("2. Instance-Stop")
    print("3. Instance-Reboot")
    print("4. Instance-Terminate")
    print("5. Exit-Menu")

    option = input("Enter the action you wish to perform ==>>")
    if option == 1:
        print("Your instance is being started...")
        my_instance.start()
    elif option == 2:
        print("Your instance is being stop...")
        my_instance.stop()
    elif option == 3:
        print("Your instance is being rebooted...")
        my_instance.reboot()
    elif option == 4:
        print("Your instance is being terminated...")
        my_instance.terminate()
    elif option == 5:
        print("Exiting...")
        break
    else:
        print "Invalid option enter. Kindly enter options between {1-5}..."
