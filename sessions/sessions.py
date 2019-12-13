import boto3
session = boto3.session.Session(profile_name="*==*")
ec2_conn_res = session.resource(service_name="ec2", region_name="us-east-1")
for each_in in ec2_conn_res.instances.all():
    print each_in.id
