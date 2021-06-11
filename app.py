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
    folder_address = JASPER_ADDRESS + "/rest_v2/resources/organizations/organization_1/Jim"
    headers = {'Content-Type': 'application/repository.folder+json'}
    resource = {"uri": "/organizations/organization_1/Jim", "label": "Jim",
                "description": "Demo folder", "permissionMask": "0",
                "creationDate": "2021-06-08T12:00:0", "updateDate": "2021-06-04T12:00:0", "version": "0"}
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
    user_address = JASPER_ADDRESS + "/rest_v2/organizations/organization_1/users/TestUser001"
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



# Apply read, write, delete access to new folder
try:
    jasper_session = requests.session()
    jasper_session.verify = False  # https://stackoverflow.com/questions/15445981/how-do-i-disable-the-security-certificate-check-in-python-requests
    permission_address = JASPER_ADDRESS + "/rest_v2/permissions"
    headers = {'Content-Type': 'application/json'}
    resource = {
        "uri": "/organizations/organization_1/Jim",
        #"recipient": "user:/TestUser001",
        "recipient": "user:/organization_1/TestUser001",
        "mask": "30" # Mask defines what level permission https://community.jaspersoft.com/wiki/repository-resource-permission
    }
    post_permission = jasper_session.post(url=permission_address,
                                    json=resource,
                                    auth=(JASPER_USERNAME, JASPER_PASSWORD),
                                    headers=headers)
    if (post_permission.status_code == 201):
        print("Permission appears to have been added correctly.")
    else:
        print("An error occurred: " + str(post_permission.text))
        post_permission.raise_for_status()
except Exception as e:
    print("An error occurred while trying to add this resource: " + str(e))








