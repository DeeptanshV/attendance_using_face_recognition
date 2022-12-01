import boto3
from boto3.dynamodb.conditions import Key, Attr

def get_all_students_in_a_section(c):
    client = boto3.resource("dynamodb")
    table = client.Table("student-details")

    response = table.scan(FilterExpression=Attr("ClassId").eq(c))
    print(response["Items"])


def set_present(name):
    client = boto3.resource("dynamodb")
    table = client.Table("student-details")

    response = table.get_item(Key={"Name": name})
    print(response["Item"]["Present"])
    present = response["Item"]["Present"]
    total = response["Item"]["Total_Classes"]

    response = table.update_item(
        Key={"Name": name},
        UpdateExpression="set Present = :present + :val, Total_Classes = :total + :val, Absent=Absent",
        ExpressionAttributeValues={":present": present, ":val": 1, ":total": total},
    )


def set_absent(name):
    client = boto3.resource("dynamodb")
    table = client.Table("student-details")

    response = table.get_item(Key={"Name": name})
    print(response["Item"]["Absent"])
    absent = response["Item"]["Absent"]
    total = response["Item"]["Total_Classes"]

    response = table.update_item(
        Key={"Name": name},
        UpdateExpression="set Absent = :absent + :val, Total_Classes = :total + :val, Present=Present",
        ExpressionAttributeValues={":absent": absent, ":val": 1, ":total": total},
    )


if __name__ == "__main__":
    get_all_students_in_a_section("N2")
