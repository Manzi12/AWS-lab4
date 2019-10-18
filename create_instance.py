#!/usr/bin/env python3
import boto3
import time
import subprocess

name_bucket='manzi2019'
ec2 = boto3.resource('ec2')
instance = ec2.create_instances(
    ImageId='ami-047bb4163c506cd98',
    MinCount=1,
    MaxCount=1,
    InstanceType='t2.micro',
    KeyName='manziAssKey',
    SecurityGroupIds=['sg-0d7a4dab022b37f9d'],
    UserData='''
		#!/bin/bash
		yum update
		yum install httpd -y
		service httpd start''',
    TagSpecifications=[
	{
		'ResourceType': 'instance',
		'Tags':[
			{
				'Key': 'Name',
				'Value': 'Manzi'
			},
			]
	},
	])
print (instance[0].id)

instance[0].wait_until_running()
instance[0].reload()
print(instance[0].public_ip_address)
ip_add=instance[0].public_ip_address

time.sleep(10)

cmd1="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'pwd'"
print(cmd1)
cmd2='curl http://devops.witdemo.net/image.jpg > image.jpg'
cmd4="curl https://s3-eu-west-1.amazonaws.com/"+name_bucket+"/image.jpg > bucket_image.jpg"
cmd5="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'curl http://169.254.169.254/latest/meta-data/local-ipv4' > meta.json"

cmd_html1="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'echo \"<html>\" > index.html'"
cmd_html2="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'echo \'Private IP Address:\' >>index.html'"
cmd_html3="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'curl http://169.254.169.254/latest/meta-data/local-ipv4 >> index.html'"
cmd_html4="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'echo \"<br>Here is the image:<br> \" >> index.html'"
cmd_html5="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'echo \"<img src=\"https://s3-eu-west-1.amazonaws.com/"+name_bucket+"/image.jpg\">\" >> index.html'"
cmd_html6="ssh -o StrictHostKeyChecking=no -i manziAssKey.pem ec2-user@" + ip_add + " 'sudo cp index.html /var/www/html'"


subprocess.call(cmd2,shell=True)
subprocess.call(cmd4,shell=True)
subprocess.call(cmd5,shell=True)
subprocess.call(cmd_html1,shell=True)
subprocess.call(cmd_html2,shell=True)
subprocess.call(cmd_html3,shell=True)
subprocess.call(cmd_html4,shell=True)
subprocess.call(cmd_html5,shell=True)

time.sleep(10)

subprocess.call(cmd_html6,shell=True)
instance[0].reload()
