import boto3
from botocore.exceptions import ClientError, WaiterError
import base64

session = boto3.Session(
aws_access_key_id = 'xxxxxx',
aws_secret_access_key = 'xxxxxx'
)

ecr = session.client('ecr', region_name='us-east-1')

resp = ecr.get_authorization_token()
auth_code = base64.b64decode(resp['authorizationData'][0]['authorizationToken']).split(':')[1]
docker_login = 'docker login -u AWS -p ' + auth_code + ' ' + resp['authorizationData'][0]['proxyEndpoint']

print docker_login
