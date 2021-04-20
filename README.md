# cli-apim
CLI to call RESTful APIs of WSO2 API Manager

You can use this Python CLI tool to consume following APIs exposed from WSO2 API Manager.
* WSO2 Publisher v2
* WSO2 Developer Portal v2
* WSO2 Admin Portal v2
* WSO2 Gateway API v2

## System Requirements
You need the latest versions of `Python` and `PIP` installed in your machine. Then run these commands using pip to install required python packages.

`pip install json`  
`pip install base64`  
`pip install requests`  

## Getting Started

1. Download the source code using the command `git clone https://github.com/binodmx/cli-apim.git`
2. Check `config.py` file to change configurations if the APIM is not deployed in localhost
3. Run `python cli-apim.py` command to start the CLI

> This is an interactive CLI, so you don't need to remember any command. Just follow the instructions.