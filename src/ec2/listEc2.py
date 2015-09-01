__author__ = 'jithinjustin'

#code for listing ec2 instances
import boto.ec2
import sys

access_key = ''
secret_key = ''

def get_ec2_instances(region,name):
    ec2_conn = boto.ec2.connect_to_region(region,
                aws_access_key_id=access_key,
                aws_secret_access_key=secret_key)
    reservations = ec2_conn.get_all_instances(filters={"tag:key" : name})
    instances = [i for r in reservations for i in r.instances]
    for i in instances:
        print i.public_dns_name



def main():
    region='us-east-1'
    get_ec2_instances(region,sys.argv[1])

if  __name__ =='__main__':main()