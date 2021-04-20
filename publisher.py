import json
import requests
import config
import auth

requests.packages.urllib3.disable_warnings(requests.packages.urllib3.exceptions.InsecureRequestWarning)

oas = None
base_path = None
tags = []

with open('open-api-specifications/publisher-v2.json') as json_file:
    oas = json.load(json_file)

    # defining base path
    base_path = "/api/am/publisher/v2"

    # listing tags
    for path in oas["paths"]:
        for method in oas["paths"][path]:
            for tag in oas["paths"][path][method]["tags"]:
                if tag not in tags:
                    tags.append(tag)


def run():
    while True:
        print("\n---WSO2 Publisher v2---\n")
        i = 1
        for tag in tags:
            print("[%i] %s" % (i, tag))
            i += 1
        print("[%i] Back" % i)
        try:
            choice_for_tag = int(input("\nChoose an option to continue: "))
            if choice_for_tag < 1 or choice_for_tag > len(tags) + 1:
                raise ValueError
        except ValueError:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break
            else:
                continue
        if choice_for_tag == i:
            break
        print("\nOperations under '%s'" % tags[choice_for_tag - 1])
        ops = []
        j = 1
        for path in oas["paths"]:
            for method in oas["paths"][path]:
                for tag in oas["paths"][path][method]["tags"]:
                    if tag == tags[choice_for_tag - 1]:
                        print("[%i] %s" % (j, oas["paths"][path][method]["summary"]))
                        ops.append({"path": path, "method": method})
                        j += 1
        print("[%i] Back" % j)
        try:
            choice_for_op = int(input("\nChoose an option to continue: "))
            if choice_for_op < 1 or choice_for_op > len(ops) + 1:
                raise ValueError
        except ValueError:
            exit_response = input("Invalid option. Do you want to exit (y/n)? ")
            if exit_response == "y" or exit_response == "Y":
                break
        if choice_for_op == j:
            continue
        print("\nDefine parameters under '%s'" % oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["summary"])
        url = config.host + base_path + ops[choice_for_op - 1]["path"]
        params = {}
        for param in oas["paths"][ops[choice_for_op - 1]["path"]][ops[choice_for_op - 1]["method"]]["parameters"]:
            if list(param.keys())[0] == "$ref":
                param = oas["components"]["parameters"][param["$ref"].split("/")[-1]]
            is_required = True if "required" in param.keys() and param["required"] == True else False
            params[param["name"]] = input("Enter %s%s (%s): " % (param["name"], "*" if is_required else "", param["schema"]["type"]))
        param_keys = list(params.keys())
        for param in param_keys:
            if params[param] == '':
                del params[param]
            elif param in url:
                url = url.replace("{" + param + "}", params[param])
        scopes = " ".join(oas["paths"][path][method]["security"][0]["OAuth2Security"])
        headers = {
            "Authorization": "Bearer %s" % auth.get_access_token(scopes)
        }
        response = requests.request(method, url, headers=headers, params=params, verify=False)
        print()
        if response.status_code == 200:
            try:
                print(json.dumps(response.json(), indent=4, sort_keys=True))
            except:
                print("\033[1;31mError occured while decoding json object. Check whether you are using correct API version.\033[0;37m")
        else:
            print(response)
        input("\nPress enter to continue...")
