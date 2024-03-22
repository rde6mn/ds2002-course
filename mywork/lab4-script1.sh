#!/bin/bash


curl 
https://greatbigphotographyworld.com/wp-content/uploads/2014/11/Landscape-Photography-steps.jpg 
> photo.jpg

aws s3 cp photo.jpg s3://ds2002-rde6mn/

aws s3 presign --expires-in 604800 s3://ds2002-rde6mn/photo.jpg

# presigned url:   
https://ds2002-rde6mn.s3.us-east-1.amazonaws.com/photo.jpg?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=ASIA5FTZEYWXWG2X2T6G%2F20240322%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20240322T235609Z&X-Amz-Expires=604800&X-Amz-SignedHeaders=host&X-Amz-Security-Token=FwoGZXIvYXdzEEcaDB9zuCn2lkZ17iJq2CLEAbpBoz%2FBVRZgppjX86NZw5CAi3EMsUGzSvg1slOzGVYvzhOYPV6q03AwXXSxMzalagPLyw94lV4hdW%2Bg9TCgwsqNx2xCaQuXh0OKljB1FsYu1hi4ARbA7dVDwg62CZFgCFxYMRJ2osve%2BjSPol14%2F%2F0vavkUe8C72SgmbdIwV4aCqLfWxZs90drWsqE%2BHETKIV0N4NsQMriPd1S%2BUmrgaxI06ClBKq8XJSmOWJkFfdTmnj5Cy2jm4mTqbRoni86lWY%2Bx2M4oo%2Fn3rwYyLfYBJOEiz%2B%2BfpB9CYvEp8F1UEmOGVR5GN4TTIAYMrR8UgKtYd86rcDbnNrnYmA%3D%3D&X-Amz-Signature=bdcaa3c6801cfada852f245850b31021f760e551ab047c8dcf0dae8e71a038ee
#the url is in the first comment
