import boto3
          import cfnresponse
          import os

          def handler(event, context):
              ssm = boto3.client('ssm')
              s3 = boto3.client('s3')

              if event['RequestType'] == 'Delete':
                  cfnresponse.send(event, context, cfnresponse.SUCCESS, {})
                  return

              try:
                  parameter = ssm.get_parameter(Name='UserName', WithDecryption=True)
                  s3.put_object(Body=parameter['Parameter']['Value'], Bucket='dxchomeassignment', Key='UserName.txt')
                  responseData = {'Success': 'SSM parameter stored in S3.'}
                  cfnresponse.send(event, context, cfnresponse.SUCCESS, responseData)
              except Exception as e:
                  responseData = {'Error': str(e)}
                  cfnresponse.send(event, context, cfnresponse.FAILED, responseData)