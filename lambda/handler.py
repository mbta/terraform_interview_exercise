# hello world Lambda function
# should be called as handler.hello_world

def hello_world(event, context):
    return {
        'statusCode': 200,
        'body': 'Hello world!'
    }
