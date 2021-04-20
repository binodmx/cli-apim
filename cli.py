import publisher
import gateway
import auth


import json

def start():
    print("---CLI for WSO2 API Manager RESTful API---")
    while True:
        print("\nYou can access following RESTful APIs.")
        print("[1] WSO2 Publisher v2\n"
              "[2] WSO2 Developer Portal v2\n"
              "[3] WSO2 Admin Portal v2\n"
              "[4] WSO2 Gateway API v2\n")
        api = input("Choose the API you want to access: ")
        if api == "1":
            run_publisher_api()
        elif api == "2":
            runStore()
        elif api == "3":
            runAdmin()
        elif api == "4":
            run_gateway_api()
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
        print("")
        break


def run_gateway_api():
    while True:
        print("\n---WSO2 Gateway API v2---\n")
        print("[1] Redeploy API\n"
              "[2] Undeploy API\n"
              "[3] Get API artifact from the storage\n"
              "[4] Get local entry from the storage\n"
              "[5] Get sequences from the storage\n"
              "[6] Get end-points from the storage for the API\n")
        action = input("Choose an action to continue: ")
        if action == "1":
            print("\nRedeploying API...")
            apiName = input("Enter API name: ")
            version = input("Enter version: ")
            tenantDomain = input("Enter tenant domain (Press enter to skip): ")
            response = gateway.redeploy_api(apiName, version, tenantDomain)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)
        elif action == "2":
            print("\nUndeploying API...")
            apiName = input("Enter API name: ")
            version = input("Enter version: ")
            tenantDomain = input("Enter tenant domain (Press enter to skip): ")
            response = gateway.undeploy_api(apiName, version, tenantDomain)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)
        elif action == "3":
            print("\nGetting API artifact from the storage...")
            apiName = input("Enter API name: ")
            version = input("Enter version: ")
            tenantDomain = input("Enter tenant domain (Press enter to skip): ")
            response = gateway.get_api_artifact_from_the_storage(apiName, version, tenantDomain)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)
        elif action == "4":
            print("\nGetting local entry from the storage...")
            apiName = input("Enter API name: ")
            version = input("Enter version: ")
            tenantDomain = input("Enter tenant domain (Press enter to skip): ")
            response = gateway.get_local_entry_from_the_storage(apiName, version, tenantDomain)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)
        elif action == "5":
            print("\nGetting sequences from the storage...")
            apiName = input("Enter API name: ")
            version = input("Enter version: ")
            tenantDomain = input("Enter tenant domain (Press enter to skip): ")
            response = gateway.get_sequence_from_the_storage(apiName, version, tenantDomain)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)
        elif action == "6":
            print("\nGetting end-points from the storage for the API...")
            apiName = input("Enter API name: ")
            version = input("Enter version: ")
            tenantDomain = input("Enter tenant domain (Press enter to skip): ")
            response = gateway.get_endpoints_from_the_storage_for_the_api(apiName, version, tenantDomain)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)
        else:
            exit_response = input("Invalid option. Do you want to go back to the main menu (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break


def runPublisher():
    try:
        global clientData
        global viewAccessToken
        global createAccessToken
        global publishAccessToken
        global api
        clientData = publisher.registerClient().json()
        viewAccessToken = publisher.generateAccessToken(clientData, 'apim:api_view').json()['access_token']
        createAccessToken = publisher.generateAccessToken(clientData, 'apim:api_create').json()['access_token']
        publishAccessToken = publisher.generateAccessToken(clientData, 'apim:api_publish').json()['access_token']
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
            response = publisher.viewApis(viewAccessToken)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("delete api @"):
            apiId = command.split("@")[1]
            response = publisher.deleteApi('c53b2e64-9df3-36a7', apiId)
            print(response)

        elif command.startswith("view api @"):
            apiId = command.split("@")[1]
            response = publisher.viewApi(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("update api @"):
            apiId = command.split("@")[1]
            jsonFileName = input("Enter json file name containing the payload: ")
            response = publisher.updateApi(createAccessToken, apiId, jsonFileName)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view resource policies @"):
            apiId = command.split("@")[1]
            response = publisher.viewResourcePolicyDefinitions(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view resource policy @"):
            apiId = command.split("@")[1]
            resourceId = input("Enter resource id: ")
            response = publisher.viewResourcePolicyDefinition(viewAccessToken, apiId, resourceId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("update resource policy @"):
            apiId = command.split("@")[1]
            resourceId = input("Enter resource id: ")
            resourcePolicyDefinitionFileName = input("Enter file name containing the resource policy definition: ")
            response = publisher.updateResourcePolicyDefinition(createAccessToken, apiId, resourceId,
                                                                resourcePolicyDefinitionFileName)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view swagger @"):
            apiId = command.split("@")[1]
            response = publisher.viewSwaggerDefinition(viewAccessToken, apiId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("update swagger @"):
            apiId = command.split("@")[1]
            swaggerDefinitionFileName = input("Enter file name containing the swagger definition: ")
            response = publisher.updateSwaggerDefinition(createAccessToken, apiId, swaggerDefinitionFileName)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("download thumbnail @"):
            apiId = command.split("@")[1]
            response = publisher.downloadThumbnailImage(viewAccessToken, apiId)
            print(response)

        elif command.startswith("upload thumbnail @"):
            apiId = command.split("@")[1]
            imgFileName = input("Enter image file name: ")
            response = publisher.uploadThumbnailImage(createAccessToken, apiId, imgFileName)
            print(response)

        elif command.startswith("change api status @"):
            apiId = command.split("@")[1]
            action = input("Enter status: ")
            response = publisher.changeApiStatus(publishAccessToken, apiId, action)
            print(response)

        elif command.startswith("create api version @"):
            apiId = command.split("@")[1]
            newVersion = input("Enter version: ")
            response = publisher.createApiVersion(createAccessToken, apiId, newVersion)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("create api"):
            jsonFileName = input("Enter json file name containing the payload: ")
            response = publisher.createApi(createAccessToken, jsonFileName)
            if response.status_code == 201:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view application @"):
            applicationId = command.split("@")[1]
            response = publisher.viewApplication(createAccessToken, applicationId)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view certificates"):
            response = publisher.viewCertificates(createAccessToken)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("view certificate @"):
            alias = command.split("@")[1]
            response = publisher.viewCertificate(createAccessToken, alias)
            if response.status_code == 200:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            else:
                print(response)

        elif command.startswith("upload certificate @"):
            alias = command.split("@")[1]
            certificate = input("Enter certificate file name: ")
            endpoint = input("Enter endpoint: ")
            response = publisher.uploadCertificate(createAccessToken, alias, certificate, endpoint)
            print(response)

        elif command.startswith("view arns @"):
            apiId = command.split("@")[1]
            response = publisher.viewARNs(viewAccessToken, apiId)
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
        clientData = publisher.registerClient().json()
        viewAccessToken = publisher.generateAccessToken(clientData, 'apim:api_view').json()['access_token']
        createAccessToken = publisher.generateAccessToken(clientData, 'apim:api_create').json()['access_token']
        publishAccessToken = publisher.generateAccessToken(clientData, 'apim:api_publish').json()['access_token']
        return "System is refreshed."
    except:
        return "\033[1;31mError while refreshing.. Check wheather apim is running\033[0;37m"


start()
