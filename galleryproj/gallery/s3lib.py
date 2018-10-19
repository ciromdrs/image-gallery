import json, boto3, os
import string, random

def sign(file_name, file_type):
    S3_BUCKET = os.environ['BUCKET']
    s3 = boto3.client('s3')
    presigned_post = s3.generate_presigned_post(
    Bucket = S3_BUCKET,
    Key = file_name,
    Fields = {"acl": "public-read", "Content-Type": file_type},
    Conditions = [
        {"acl": "public-read"},
        {"Content-Type": file_type}
    ],
    ExpiresIn = 3600
    )

    return json.dumps({
      'data': presigned_post,
      'url': 'https://%s.s3.amazonaws.com/%s' % (S3_BUCKET, file_name)
    })

def generate_id():
    # TODO: implement sequential controlled id generation
    return ''.join(random.choices(string.ascii_uppercase + string.digits, k=20))
