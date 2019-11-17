import boto3
from botocore.exceptions import ClientError, WaiterError
import base64
import subprocess

session = boto3.Session(
aws_access_key_id = 'xxxxxx',
aws_secret_access_key = 'xxxxxx'
)

ecr = session.client('ecr', region_name='us-east-1')

resp = ecr.get_authorization_token()
auth_code = base64.b64decode(resp['authorizationData'][0]['authorizationToken']).split(':')[1]
docker_login = 'docker login -u AWS -p ' + auth_code + ' ' + resp['authorizationData'][0]['proxyEndpoint']

try:
    run_login = subprocess.check_output(docker_login, stderr=subprocess.STDOUT, shell=True)
except subprocess.CalledProcessError as e:
    print("Exception: %s\n" % e)
    print("Exception Output: %s\n" % e.output)
else:
    print run_login
