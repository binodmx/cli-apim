import requests
import base64
import config


def redeploy_api(apiName, version, tenantDomain):
    url = config.protocol + config.host + ":" + config.servlet_port + config.gateway_path + "redeploy-api"
    headers = {
        "Authorization": "Basic %s" % config.base64_encoded_username_and_password
    }
    params = {
        "apiName": apiName,
        "version": version,
        "tenantDomain": "carbon.super" if tenantDomain == "" else tenantDomain
    }
    response = requests.post(url, headers=headers, params=params, verify=False)
    return response


def undeploy_api(apiName, version, tenantDomain):
    url = config.protocol + config.host + ":" + config.servlet_port + config.gateway_path + "undeploy-api"
    headers = {
        "Authorization": "Basic %s" % config.base64_encoded_username_and_password
    }
    params = {
        "apiName": apiName,
        "version": version,
        "tenantDomain": "carbon.super" if tenantDomain == "" else tenantDomain
    }
    response = requests.post(url, headers=headers, params=params, verify=False)
    return response


def get_api_artifact_from_the_storage(apiName, version, tenantDomain):
    url = config.protocol + config.host + ":" + config.servlet_port + config.gateway_path + "api-artifact"
    headers = {
        "Authorization": "Basic %s" % base64.b64encode(
            str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8")
    }
    params = {
        "apiName": apiName,
        "version": version,
        "tenantDomain": "carbon.super" if tenantDomain == "" else tenantDomain
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response


def get_local_entry_from_the_storage(apiName, version, tenantDomain):
    url = config.protocol + config.host + ":" + config.servlet_port + config.gateway_path + "local-entry"
    headers = {
        "Authorization": "Basic %s" % base64.b64encode(
            str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8")
    }
    params = {
        "apiName": apiName,
        "version": version,
        "tenantDomain": "carbon.super" if tenantDomain == "" else tenantDomain
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response


def get_sequence_from_the_storage(apiName, version, tenantDomain):
    url = config.protocol + config.host + ":" + config.servlet_port + config.gateway_path + "sequence"
    headers = {
        "Authorization": "Basic %s" % base64.b64encode(
            str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8")
    }
    params = {
        "apiName": apiName,
        "version": version,
        "tenantDomain": "carbon.super" if tenantDomain == "" else tenantDomain
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response


def get_endpoints_from_the_storage_for_the_api(apiName, version, tenantDomain):
    url = config.protocol + config.host + ":" + config.servlet_port + config.gateway_path + "end-points"
    headers = {
        "Authorization": "Basic %s" % base64.b64encode(
            str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8")
    }
    params = {
        "apiName": apiName,
        "version": version,
        "tenantDomain": "carbon.super" if tenantDomain == "" else tenantDomain
    }
    response = requests.get(url, headers=headers, params=params, verify=False)
    return response
