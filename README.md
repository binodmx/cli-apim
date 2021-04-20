# cli-apim
CLI to call RESTful APIs of WSO2 API Manager

You can use this Python CLI tool to consume following APIs exposed from WSO2 API Manager.
* [WSO2 Publisher v1](#wso2-publisher-v1)
* [WSO2 Developer Portal v1](#wso2-developer-portal-v1)
* [WSO2 Admin Portal v1](#wso2-admin-portal-v1)
* [WSO2 Gateway API v1](#wso2-gateway-api-v1)

### System Requirements
You need the latest versions of `Python` and `PIP` installed in your machine. Then run these commands using pip to install required python packages.

`pip install json`  
`pip install base64`  
`pip install requests`  

### Getting Started

Run `python cli.py` in terminal to start the CLI. 

>Access tokens are auto-generated and handled by itself when CLI 
starts, you don't need to copy and paste tokens for each api call. If you want to generate new access tokens just 
type `refresh` and press enter. To close the CLI type `exit` and press enter. 

## WSO2 Publisher v1
#### API (Collection)
- `view apis`
#### API (Individual)
- `delete api @apiId`
- `view api @apiId`
- `update api @apiId`
- `view resource policies @apiId`
- `view resource policy @apiId`
- `update resource policy @apiId`
- `view swagger @apiId`
- `update swagger @apiId`
- `download thumbnail @apiId`
- `upload thumbnail @apiId`
- `change api status @apiId`
- `create api version @apiId`
- `create api`
#### Application (Individual)
#### Certificates (Collection)
#### Certificates (Individual)
#### ClientCertificates (Collection)
#### ClientCertificates (Individual)
#### Document (Collection)
#### Document (Individual)
#### Environment (Collection)
#### MediationPolicy (Collection)
#### MediationPolicy (Individual)
#### Subscription (Collection)
#### Subscription (Individual)
#### ThrottlingTier (Collection)
#### ThrottlingTier (Individual)
#### Workflows (Individual)
#### WSDL (Individual)
## WSO2 Developer Portal v1
## WSO2 Admin Portal v1
## WSO2 Gateway API v1