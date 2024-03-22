#!/usr/local/bin/python3

import boto3
import urllib
import urllib.request

s3 = boto3.client('s3', region_name="us-east-1")

urllib.request.urlretrieve('https://compote.slate.com/images/697b03b-64a5-49a0-8059-27b963453fb1.gif', 
'mygif.gif')

bucket = 'ds2002-rde6mn'
local_file = 'mygif.gif'

resp = s3.put_object(
    Body = 'mygif.gif',
    Bucket = 'ds2002-rde6mn',
    Key = 'mygif.gif',
    ACL = 'public-read',
)


bucket_name = 'ds2002-rde6mn'
object_name = 'mygif.gif'
expires_in = 604800

response = s3.generate_presigned_url(
    'get_object',
    Params={'Bucket': bucket_name, 'Key': object_name},
    ExpiresIn=expires_in
    )


#url: 
https://ds2002-rde6mn.s3.us-east-1.amazonaws.com/mygif.gif?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA5FTZEYWXWG2X2T6G%2F20240322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240322T234726Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEEcaDB9zuCn2lkZ17iJq2CLEAbpBoz%2FBVRZgppjX86NZw5CAi3EMsUGzSvg1slOzGVYvzhOYPV6q03AwXXSxMzalagPLyw94lV4hdW%2Bg9TCgwsqNx2xCaQuXh0OKljB1FsYu1hi4ARbA7dVDwg62CZFgCFxYMRJ2osve%2BjSPol14%2F%2F0vavkUe8C72SgmbdIwV4aCqLfWxZs90drWsqE%2BHETKIV0N4NsQMriPd1S%2BUmrgaxI06ClBKq8XJSmOWJkFfdTmnj5Cy2jm4mTqbRoni86lWY%2Bx2M4oo%2Fn3rwYyLfYBJOEiz%2B%2BfpB9CYvEp8F1UEmOGVR5GN4TTIAYMrR8UgKtYd86rcDbnNrnYmA%3D%3D&X-Amz-Signature=77ea238b2548ef43c3815bcae7bb3f6153b46626d4ade4c5cd58fe95b9b86eae
#url above extends past visible page
