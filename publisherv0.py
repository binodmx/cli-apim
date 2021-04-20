import requests
import base64
import config


requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)


def retrieve_apis(view_access_token):
    url = config.protocol + config.host + ":" + config.servlet_port + config.publisher_path + "/apis"
    headers = {
        "Authorization": "Bearer %s" % view_access_token,
        "Accept": "application/json",
        "Content-Type": "application/json",
        "If-None-Match": ""
    }
    params = {
        "limit": 25,
        "offset": 0,
        "query": "",
        "expand": False
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response


# API (Individual)


def deleteApi(createAccessToken, apiId):
    url = host + basePath + "/apis/%s" % apiId
    headers = {
        "Authorization": "Bearer %s" % createAccessToken
    }
    response = requests.delete(url, headers=headers, verify=False)
    return response


def viewApi(viewAccessToken, apiId):
    url = host + basePath + "/apis/%s" % apiId
    headers = {
        "Authorization": "Bearer %s" % viewAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


def updateApi(createAccessToken, apiId, jsonFileName):
    url = host + basePath + "/apis/%s" % apiId
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "Content-Type": "application/json"
    }
    try:
        with open(jsonFileName) as jsonFile:
            payload = json.dumps(json.load(jsonFile))
    except:
        payload = "{}"
    response = requests.put(url, headers=headers, data=payload, verify=False)
    return response


def viewResourcePolicyDefinitions(viewAccessToken, apiId):
    url = host + basePath + "/apis/%s/resource-policies" % apiId
    headers = {
        "Authorization": "Bearer %s" % viewAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


def viewResourcePolicyDefinition(viewAccessToken, apiId, resourceId):
    url = host + basePath + "/apis/%s/resource-policies/%s" % apiId, resourceId
    headers = {
        "Authorization": "Bearer %s" % viewAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


def updateResourcePolicyDefinition(createAccessToken, apiId, resourceId, resourcePolicyDefinitionFileName):
    url = host + basePath + "/apis/%s/resource-policies/%s" % apiId, resourceId
    headers = {
        "Authorization": "Bearer %s" % createAccessToken
    }
    try:
        with open(resourcePolicyDefinitionFileName, "r") as resourcePolicyDefinitionFile:
            files = {"apiDefinition": resourcePolicyDefinitionFile.read()}
    except:
        files = {}
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def viewSwaggerDefinition(viewAccessToken, apiId):
    url = host + basePath + "/apis/%s/swagger" % apiId
    headers = {
        "Authorization": "Bearer %s" % viewAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


def updateSwaggerDefinition(createAccessToken, apiId, swaggerDefinitionFileName):
    url = host + basePath + "/apis/%s/swagger" % apiId
    headers = {
        "Authorization": "Bearer %s" % createAccessToken
    }
    try:
        with open(swaggerDefinitionFileName, "r") as swaggerDefinitionFile:
            files = {"apiDefinition": swaggerDefinitionFile.read()}
    except:
        files = {}
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def downloadThumbnailImage(viewAccessToken, apiId):
    url = host + basePath + "/apis/%s/thumbnail" % apiId
    headers = {
        "Authorization": "Bearer %s" % viewAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        with open("thumbnail.jpg", 'wb') as imgFile:
            imgFile.write(response.content)
    return response


def uploadThumbnailImage(createAccessToken, apiId, imgFileName):
    url = host + basePath + "/apis/%s/thumbnail" % apiId
    headers = {
        "Authorization": "Bearer %s" % createAccessToken
    }
    try:
        files = {"file": open(imgFileName, "rb")}
    except:
        files = {}
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


def changeApiStatus(publishAccessToken, apiId, action):
    url = host + basePath + "/apis/change-lifecycle"
    headers = {
        "Authorization": "Bearer %s" % publishAccessToken
    }
    params = {
        "apiId": apiId,
        "action": action
    }
    response = requests.post(url, headers=headers, params=params, verify=False)
    return response


def createApiVersion(createAccessToken, apiId, newVersion):
    url = host + basePath + "/apis/copy-api"
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "Content-Type": "application/json"
    }
    params = {
        "apiId": apiId,
        "newVersion": newVersion
    }
    response = requests.post(url, headers=headers, params=params, verify=False)
    return response


def createApi(createAccessToken, jsonFileName):
    url = host + basePath + "/apis"
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "Content-Type": "application/json"
    }
    try:
        with open(jsonFileName) as jsonFile:
            payload = json.dumps(json.load(jsonFile))
    except:
        payload = "{}"
    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response


# Application (Individual)


def viewApplication(createAccessToken, applicationId):
    url = host + basePath + "/applications/%s" % applicationId
    headers = {
        "Authorization": "Bearer %s" % createAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


# Certificates (Collection)


def viewCertificates(createAccessToken):
    url = host + basePath + "/certificates"
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "Content-Type": "application/json"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


# Certificates (Individual)


def downloadCertificate(createAccessToken, alias):
    url = host + basePath + "/certificates/%s/content" % alias
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers, verify=False)
    if response.status_code == 200:
        with open(alias + 'cer', 'wb') as cert:
            cert.write(response.content)
    return response


def deleteCertificate(createAccessToken, alias):
    url = host + basePath + "/certificates/%s" % alias
    headers = {
        "Authorization": "Bearer %s" % createAccessToken
    }
    response = requests.delete(url, headers=headers, verify=False)
    return response


def viewCertificate(createAccessToken, alias):
    url = host + basePath + "/certificates/%s" % alias
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "accept": "application/json"
    }
    response = requests.get(url, headers=headers, verify=False)
    return response


def updateCertificate(createAccessToken, alias, certificate):
    url = host + basePath + "/certificates/%s" % alias
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "Content-Type": "multipart/form-data"
    }
    files = {
        "certificate": certificate,
    }
    response = requests.put(url, headers=headers, files=files, verify=False)
    return response


def uploadCertificate(createAccessToken, alias, certificate, endpoint):
    url = host + basePath + "/certificates"
    headers = {
        "Authorization": "Bearer %s" % createAccessToken,
        "Content-Type": "multipart/form-data"
    }
    files = {
        "alias": alias,
        "certificate": certificate,
        "endpoint": endpoint
    }
    response = requests.post(url, headers=headers, files=files, verify=False)
    return response


# ClientCertificates (Collection)


# ClientCertificates (Individual)


# Document (Collection)


# Document (Individual)


# Environment (Collection)


# Mediation Policy (Collection)


# Mediation Policy (Individual)


# Subscription (Collection)


# Subscription (Individual)


# Throttling Tier (Collection)


# Throttling Tier (Individual)


# Workflow (Individual)


# Wsdl (Individual)


# AWS Lambda (Individual)


def viewARNs(viewAccessToken, apiId):
    url = host + basePath + "/apis/%s/arns" % apiId
    headers = {
        "Authorization": "Bearer %s" % viewAccessToken
    }
    response = requests.get(url, headers=headers, verify=False)
    return response
