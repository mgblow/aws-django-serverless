import boto3.exceptions
import botocore


def create_table():
    dynamodb = boto3.resource("dynamodb")

    table = dynamodb.create_table(
        TableName="TaskDevices",
        KeySchema=[{"AttributeName": "id", "KeyType": "HASH"}],
        AttributeDefinitions=[{"AttributeName": "id", "AttributeType": "S"}, ],
        ProvisionedThroughput={"ReadCapacityUnits": 5, "WriteCapacityUnits": 2},
    )
    return table


if __name__ == "__main__":
    try:
        table = create_table()
        table.meta.client.get_waiter("table_exists").wait(TableName="TaskDevices")
        print("table created successfully.")
    except botocore.exceptions.ClientError as error:
        if error.response["Error"]["Code"] == "ResourceInUseException":
            print("Error: Table with this name already exists.")
        else:
            raise error
