import requests
import base64
import json
import config


def register_client():
    url = config.protocol + config.host + ":" + config.servlet_port + config.client_register_path
    headers = {
        "Authorization": "Basic %s" % base64.b64encode(
            str(config.admin_username + ":" + config.admin_password).encode()).decode("utf-8"),
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "callbackUrl": "www.google.lk",
        "clientName": "rest_api_publisher",
        "owner": "admin",
        "grantType": "password refresh_token",
        "saasApp": True
    })
    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response


def generate_access_token(consumer_credentials, scope):
    url = config.protocol + config.host + ":" + config.servlet_port + config.token_path
    headers = {
        "Authorization": "Basic " + base64.b64encode(
            str(consumer_credentials['clientId'] + ":" + consumer_credentials['clientSecret']).encode()).decode(
            "utf-8"),
        "Content-Type": "application/json"
    }
    payload = json.dumps({
        "grant_type": "password",
        "username": config.admin_username,
        "password": config.admin_password,
        "scope": scope
    })
    response = requests.post(url, headers=headers, data=payload, verify=False)
    return response
