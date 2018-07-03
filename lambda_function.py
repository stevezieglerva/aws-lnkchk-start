import boto3
from datetime import datetime

def get_bucket_file_url(record):
    #https://s3.amazonaws.com/link-checker/2018-05-27-235740.txt
    newfile = record["s3"]["object"]["key"]
    bucket_arn = record["s3"]["bucket"]["arn"]
    bucket_name = get_bucket_name_from_arn(bucket_arn)
    file_path = "https://s3.amazonaws.com/" + bucket_name + "/" + newfile
    return file_path

def get_bucket_name_from_arn(bucket_arn):
    bucket_name = bucket_arn.rsplit(":", 1)[-1]
    return bucket_name


def lambda_handler(event, context):
    # TODO implement
    print("Starting ...")
    print("\tEvent: " + str(event))
    
    files_found = {}
    count = 0

    db = boto3.resource("dynamodb")
    queue = db.Table("lnkchk-queue")

    s3 = boto3.resource('s3')
    
    for record in event["Records"]:
        count = count + 1
        newfile = record["s3"]["object"]["key"]
        bucket_arn = record["s3"]["bucket"]["arn"]
        bucket_name = get_bucket_name_from_arn(bucket_arn)
        file_url = get_bucket_file_url(record)
        print ("\t\tFile: " + file_url)
        files_found[count] = file_url

        obj = s3.Object(bucket_name, newfile)
        file_contents = obj.get()['Body'].read().decode('utf-8') 
        print("\t\t\tFile contents: " + file_contents)
        line = 0
        for url_line in file_contents.split("\n"):
            line = line + 1
            if url_line != "":
                print("\t\t\turl_line: " + url_line)
                queue.put_item(Item = {"url": url_line, "source" : "s3 upload", "main_site" : url_line, "timestamp" : str(datetime.now())})

                
                
    return files_found



    