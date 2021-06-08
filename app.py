import config, requests


# Description: Demo of Jasper API
# Author: Jim Rentschler
# Date: 6/8/2021



JASPER_USERNAME = config.APP_JASPER_USERNAME
JASPER_PASSWORD = config.APP_JASPER_PASSWORD
JASPER_ADDRESS = config.APP_JASPER_SERVER_URI


# Create folder named Jim
try:
    jasper_session = requests.session()
    jasper_session.verify = False # https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
    folder_address = JASPER_ADDRESS + "/rest_v2/resources/Jim"
    headers = {'Content-Type': 'application/repository.folder+json'}
    resource = {"uri": "/Jim", "label": "Jim",
                "description": "Demo folder", "permissionMask": "0",
                "creationDate": "2021-06-08T12:00:0", "updateDate": "2021-06-04T12:00:0", "version": "6"}
    put_folder = jasper_session.put(url=folder_address,
                                    json=resource,
                                    auth=(JASPER_USERNAME,JASPER_PASSWORD),
                                    headers=headers)

    if (put_folder.status_code == 200):
        print("Folder appears to have been created correctly.")
    else:
        print("An error occurred: " + str(put_folder.text))
        put_folder.raise_for_status()
except Exception as e:
    print("An error occurred while trying to create this resource: " + str(e))


# Create test user
try:
    jasper_session = requests.session()
    jasper_session.verify = False  # https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
    user_address = JASPER_ADDRESS + "/rest_v2/users/TestUser001"
    headers = {'Content-Type': 'application/json'}
    resource = {
        "fullName": "TestUser001",
        "emailAddress": "jrentschler123@gmail.com",
        "enabled": "true",
        "password": "password",
        "roles": [
            {"name": "ROLE_ADMINISTRATOR"}]
    }
    put_user = jasper_session.put(url=user_address,
                                    json=resource,
                                    auth=(JASPER_USERNAME, JASPER_PASSWORD),
                                    headers=headers)
    if (put_user.status_code == 200):
        print("User appears to have been created correctly.")
    else:
        print("An error occurred: " + str(put_user.text))
        put_user.raise_for_status()
except Exception as e:
    print("An error occurred while trying to create this resource: " + str(e))


# Create test user
try:
    jasper_session = requests.session()
    jasper_session.verify = False  # https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
    user_address = JASPER_ADDRESS + "/rest_v2/users/TestUser001"
    headers = {'Content-Type': 'application/json'}
    resource = {
        "fullName": "TestUser001",
        "emailAddress": "jrentschler123@gmail.com",
        "enabled": "true",
        "password": "password",
        "roles": [
            {"name": "ROLE_ADMINISTRATOR"}]
    }
    put_user = jasper_session.put(url=user_address,
                                    json=resource,
                                    auth=(JASPER_USERNAME, JASPER_PASSWORD),
                                    headers=headers)
    if (put_user.status_code == 200):
        print("User appears to have been created correctly.")
    else:
        print("An error occurred: " + str(put_user.text))
        put_user.raise_for_status()
except Exception as e:
    print("An error occurred while trying to create this resource: " + str(e))


def put_resource(JASPER_USERNAME,JASPER_PASSWORD, JASPER_ADDRESS, resource, headers, resource_address):
    jasper_session = requests.session()
    jasper_session.verify = False # https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
    address = JASPER_ADDRESS + resource_address
    response = jasper_session.put(url=user_address,
                                    json=resource,
                                    auth=(JASPER_USERNAME, JASPER_PASSWORD),
                                    headers=headers)






