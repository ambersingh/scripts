import boto
from boto.s3.key import Key

aws_access_key_id = "aws key"
aws_secret_key = "aws secret key"
s3_bucket_name = "awesomevivek"
file_name = 'mpsd.json'
aws_connection = boto.connect_s3(aws_access_key_id, aws_secret_key)
print('aws_connection', aws_connection)
bucket = aws_connection.get_bucket(s3_bucket_name)
key = Key(bucket)
key.key='test/2017/10/23/'+file_name
print('bucket', bucket)
print('key', key)
print('uploading to s3')
# for uploading the data from file
res = key.set_contents_from_filename(file_name)
print('res', res)

# for uploading data which is string format.
# key.set_contents_from_string('This is a test of S3')
