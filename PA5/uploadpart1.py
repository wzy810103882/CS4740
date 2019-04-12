import boto3

s3 = boto3.resource('s3')

# Get list of objects for indexing
images=[('odumosu01.jpeg','Tolu Odumosu'),
      ('odumosu02.jpeg','Tolu Odumosu'),
      ('odumosu03.jpeg','Tolu Odumosu'),
      ('reiss01.jpeg','Charles Reiss'),
      ('reiss02.jpeg','Charles Reiss'),
      ('sid01.jpeg','Nikos Sid'),
      ('sid02.jpeg','Nikos Sid'),
      ('sid03.jpeg','Nikos Sid')
      ]

# Iterate through list to upload objects to S3   
for image in images:
    file = open(image[0],'rb')
    object = s3.Object('pa5-part1','index/'+ image[0])
    ret = object.put(Body=file,
                    Metadata={'FullName':image[1]}
                    )