import publisherv0
import devportal
import admin
import gateway
import auth

import json


def start():
    while True:
        print("---CLI for WSO2 API Manager RESTful API---")
        print("\nYou can access following RESTful APIs.")
        print("[1] WSO2 Publisher v2\n"
              "[2] WSO2 Developer Portal v2\n"
              "[3] WSO2 Admin Portal v2\n"
              "[4] WSO2 Gateway API v2\n"
              "[5] Exit")
        choice_for_api = input("Choose the API you want to access: ")
        if choice_for_api == "1":
            run_publisher_api()
        elif choice_for_api == "2":
            runStore()
        elif choice_for_api == "3":
            runAdmin()
        elif choice_for_api == "4":
            gateway.run()
        elif choice_for_api == "5":
            break
        else:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break


def run_publisher_api():
    print("\n---WSO2 Publisher v2---\n")
    try:
        consumer_credentials = auth.register_client().json()
        view_access_token = auth.generate_access_token(consumer_credentials, 'apim:api_view').json()['access_token']
        create_access_token = auth.generate_access_token(consumer_credentials, 'apim:api_create').json()['access_token']
        delete_access_token = auth.generate_access_token(consumer_credentials, 'apim:api_delete').json()['access_token']
        publish_access_token = auth.generate_access_token(consumer_credentials, 'apim:api_publish').json()['access_token']
        print("\033[1;34mClient registration is successful\033[0;37m")
    except:
        print("\033[1;31mClient registration is unsuccessful. Check config.py file to change configurations.\033[0;37m")
    while True:
        print("[1] Retrieve/Search APIs"
              "[2] Create a New API")
        break


def runPublisher():
    try:
        global clientData
        global viewAccessToken
        global createAccessToken
        global publishAccessToken
        global api
        clientData = publisherv0.registerClient().json()
        viewAccessToken = publisherv0.generateAccessToken(clientData, 'apim:api_view').json()['access_token']
        createAccessToken = publisherv0.generateAccessToken(clientData, 'apim:api_create').json()['access_token']
        publishAccessToken = publisherv0.generateAccessToken(clientData, 'apim:api_publish').json()['access_token']
        status = True
        print("\033[1;34mClient registration is successful\033[0;37m")
    except:
        status = False
        api = "wait"
        print("\033[1;31mClient registration is unsuccessful. Check wheather apim is running\033[0;37m")
    while status:
        command = input("\033[1;32mpublisher: \033[0;37m").strip()

        if command == "":
            continue

        elif command == "exit":
            api = "exit"
            break

        elif command == "refresh":
            response = refresh()
            print(response)

        elif command.startswith("view apis"):
            response = publisherv0.viewApis(viewAccessToken)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("delete api @"):
            apiId = command.split("@")[1]
            response = publisherv0.deleteApi('c53b2e64-9df3-36a7', apiId)
            print(response)

        elif command.startswith("view api @"):
            apiId = command.split("@")[1]
            response = publisherv0.viewApi(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("update api @"):
            apiId = command.split("@")[1]
            jsonFileName = input("Enter json file name containing the payload: ")
            response = publisherv0.updateApi(createAccessToken, apiId, jsonFileName)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view resource policies @"):
            apiId = command.split("@")[1]
            response = publisherv0.viewResourcePolicyDefinitions(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view resource policy @"):
            apiId = command.split("@")[1]
            resourceId = input("Enter resource id: ")
            response = publisherv0.viewResourcePolicyDefinition(viewAccessToken, apiId, resourceId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("update resource policy @"):
            apiId = command.split("@")[1]
            resourceId = input("Enter resource id: ")
            resourcePolicyDefinitionFileName = input("Enter file name containing the resource policy definition: ")
            response = publisherv0.updateResourcePolicyDefinition(createAccessToken, apiId, resourceId,
                                                                  resourcePolicyDefinitionFileName)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view swagger @"):
            apiId = command.split("@")[1]
            response = publisherv0.viewSwaggerDefinition(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("update swagger @"):
            apiId = command.split("@")[1]
            swaggerDefinitionFileName = input("Enter file name containing the swagger definition: ")
            response = publisherv0.updateSwaggerDefinition(createAccessToken, apiId, swaggerDefinitionFileName)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("download thumbnail @"):
            apiId = command.split("@")[1]
            response = publisherv0.downloadThumbnailImage(viewAccessToken, apiId)
            print(response)

        elif command.startswith("upload thumbnail @"):
            apiId = command.split("@")[1]
            imgFileName = input("Enter image file name: ")
            response = publisherv0.uploadThumbnailImage(createAccessToken, apiId, imgFileName)
            print(response)

        elif command.startswith("change api status @"):
            apiId = command.split("@")[1]
            action = input("Enter status: ")
            response = publisherv0.changeApiStatus(publishAccessToken, apiId, action)
            print(response)

        elif command.startswith("create api version @"):
            apiId = command.split("@")[1]
            newVersion = input("Enter version: ")
            response = publisherv0.createApiVersion(createAccessToken, apiId, newVersion)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("create api"):
            jsonFileName = input("Enter json file name containing the payload: ")
            response = publisherv0.createApi(createAccessToken, jsonFileName)
            if response.status_code == 201:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view application @"):
            applicationId = command.split("@")[1]
            response = publisherv0.viewApplication(createAccessToken, applicationId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view certificates"):
            response = publisherv0.viewCertificates(createAccessToken)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view certificate @"):
            alias = command.split("@")[1]
            response = publisherv0.viewCertificate(createAccessToken, alias)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("upload certificate @"):
            alias = command.split("@")[1]
            certificate = input("Enter certificate file name: ")
            endpoint = input("Enter endpoint: ")
            response = publisherv0.uploadCertificate(createAccessToken, alias, certificate, endpoint)
            print(response)

        elif command.startswith("view arns @"):
            apiId = command.split("@")[1]
            response = publisherv0.viewARNs(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        else:
            print(
                "Command is not found, refer the documentation in https://github.com/binodmx/wso2-apim-restful-api-cli")

        print()


def runStore():
    return


def runAdmin():
    return


def refresh():
    try:
        global clientData
        global viewAccessToken
        global createAccessToken
        global publishAccessToken
        clientData = publisherv0.registerClient().json()
        viewAccessToken = publisherv0.generateAccessToken(clientData, 'apim:api_view').json()['access_token']
        createAccessToken = publisherv0.generateAccessToken(clientData, 'apim:api_create').json()['access_token']
        publishAccessToken = publisherv0.generateAccessToken(clientData, 'apim:api_publish').json()['access_token']
        return "System is refreshed."
    except:
        return "\033[1;31mError while refreshing.. Check wheather apim is running\033[0;37m"


start()
